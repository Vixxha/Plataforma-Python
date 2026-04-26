import React, { useState, useEffect, useRef } from 'react';
import { Terminal, Play, Eye, EyeOff, CheckCircle, Code, Trash2, Lightbulb, Download } from 'lucide-react';
import type { Exercise } from '../hooks/useExerciseLoader';
import { usePythonExecutor } from '../hooks/usePythonExecutor';
import { explainCodeWithGemini } from '../services/gemini';
import confetti from 'canvas-confetti';
import './HackerEditor.css';

interface Props {
  exercise: Exercise | null;
  userName: string;
  onForceExercise?: (id: string) => void;
  onNextExercise?: () => void;
  hintsEnabled?: boolean;
}

export const HackerEditor: React.FC<Props> = ({ exercise, userName, onForceExercise, onNextExercise, hintsEnabled }) => {
  const [code, setCode] = useState('');
  const [attempts, setAttempts] = useState(0);
  const [outputLines, setOutputLines] = useState<{ text: string, type: 'info' | 'error' | 'success' }[]>([]);
  const [showSolution, setShowSolution] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [hasError, setHasError] = useState(false);
  const [showHintText, setShowHintText] = useState(false);
  const [explainLoading, setExplainLoading] = useState(false);
  const { loading, runCode } = usePythonExecutor();
  const consoleRef = useRef<HTMLDivElement>(null);
  const nextExerciseTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    return () => {
      if (nextExerciseTimerRef.current) clearTimeout(nextExerciseTimerRef.current);
    };
  }, []);

  useEffect(() => {
    if (exercise) {
      setCode(`# Escribe tu código aquí\n\n`);
      setAttempts(0);
      setOutputLines([
        { text: `[SYSTEM] Conexión establecida. User: ${userName || 'GUEST'}.`, type: 'info' },
        { text: `[SYSTEM] Cargado ejercicio: ${exercise.title}.`, type: 'info' }
      ]);
      setShowSolution(false);
      setIsSuccess(false);
      setHasError(false);
      setShowHintText(false);
    }
  }, [exercise, userName]);

  useEffect(() => {
    if (consoleRef.current) {
      consoleRef.current.scrollTop = consoleRef.current.scrollHeight;
    }
  }, [outputLines]);

  const handleRun = async () => {
    if (!exercise || loading || isSuccess) return;
    const adminMatch = code.match(/#admin\s+load\s+(\w+)/i);
    if (adminMatch && adminMatch[1]) {
      const targetId = adminMatch[1];
      if (onForceExercise) {
        onForceExercise(targetId);
        setOutputLines([{ text: `[SYSTEM] ACCESS OVERRIDE. Forzando ejercicio id_${targetId}...`, type: 'info' }]);
        setCode(`# Escribe tu código aquí\n\n`);
        return;
      }
    }

    setOutputLines(prev => [...prev, { text: `> Ejecutando script_`, type: 'info' }]);
    const result = await runCode(code, exercise.tests_code);

    if (result.success) {
      const splits = (result.stdout || '').split('\n').filter(Boolean);
      const mappedOut = splits.map((t: string) => ({ text: t, type: 'info' as const }));
      setOutputLines(prev => [...prev, ...mappedOut, { text: `[SUCCESS] ACCESS GRANTED. Prueba superada. 🎉`, type: 'success' }]);
      setIsSuccess(true);
      setHasError(false);
      confetti({
        particleCount: 150,
        spread: 80,
        origin: { y: 0.6 },
        colors: ['#10b981', '#0ea5e9', '#ffffff']
      });

      if (onNextExercise) {
        nextExerciseTimerRef.current = setTimeout(() => {
          onNextExercise();
        }, 5000);
      }
    } else {
      setAttempts(a => a + 1);
      const errParts = (result.stderr || result.error || '').split('\n').filter(Boolean);
      const mappedErr = errParts.map((t: string) => ({ text: t, type: 'error' as const }));
      setOutputLines(prev => [...prev, ...mappedErr, { text: `[ERROR] ACCESS DENIED. Intento fallido (${attempts + 1}/3).`, type: 'error' }]);
      setHasError(true);
    }
  };

  const handleExplainCode = async () => {
    if (!exercise || !code.trim() || explainLoading) return;
    setExplainLoading(true);
    setOutputLines(prev => [...prev, { text: `> Consultando IA de Gemini...`, type: 'info' }]);
    
    try {
      const explanation = await explainCodeWithGemini(code, exercise.description);
      const explanationLines = explanation.split('\n');
      const mappedLines = explanationLines.map(t => ({ text: t, type: 'info' as const }));
      setOutputLines(prev => [...prev, { text: `[IA] Análisis Completado:`, type: 'success' }, ...mappedLines]);
    } catch (err: unknown) {
      const errorMessage = err instanceof Error ? err.message : String(err);
      setOutputLines(prev => [...prev, { text: `[ERROR IA] ${errorMessage}`, type: 'error' }]);
    } finally {
      setExplainLoading(false);
    }
  };

  const handleClearCode = () => {
    setCode(`# Escribe tu código aquí\n\n`);
    setHasError(false);
  };

  const handleDownloadCode = () => {
    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ejercicio_${exercise.id}.py`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handleDownloadLog = () => {
    const logText = outputLines.map(l => l.text).join('\n');
    const blob = new Blob([logText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `terminal_log_${exercise.id}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handleDownloadSolution = () => {
    const blob = new Blob([exercise.solution_code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `solucion_${exercise.id}.py`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const target = e.target as HTMLTextAreaElement;
      const start = target.selectionStart;
      const end = target.selectionEnd;
      setCode(code.substring(0, start) + '    ' + code.substring(end));
      setTimeout(() => {
        target.selectionStart = target.selectionEnd = start + 4;
      }, 0);
    }
  };

  if (!exercise) return null;

  return (
    <div className="hacker-editor">
      <div className="hacker-header">
        <h2 className="glitch" data-text={exercise.title}>{exercise.title}</h2>
        <span className="exercise-id">id_{exercise.id}</span>
      </div>

      <p className="exercise-description">&gt; {exercise.description}</p>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem', flexWrap: 'wrap' }}>
        <div 
          className="glitch-btn" 
          style={{ 
            padding: '0.3rem 0.6rem', 
            fontSize: '0.8rem', 
            borderColor: (exercise.difficulty || '').toLowerCase().includes('dificil') || (exercise.difficulty || '').toLowerCase().includes('avanz') ? '#EF4444' : (exercise.difficulty || '').toLowerCase().includes('medio') || (exercise.difficulty || '').toLowerCase().includes('inter') ? '#F59E0B' : '#10B981', 
            color: (exercise.difficulty || '').toLowerCase().includes('dificil') || (exercise.difficulty || '').toLowerCase().includes('avanz') ? '#EF4444' : (exercise.difficulty || '').toLowerCase().includes('medio') || (exercise.difficulty || '').toLowerCase().includes('inter') ? '#F59E0B' : '#10B981',
            cursor: 'default',
            pointerEvents: 'none'
          }}
        >
          LVL: {exercise.difficulty || 'BÁSICO'}
        </div>

        {hintsEnabled && exercise.hint && (
          <div>
            {!showHintText ? (
              <button 
                className="glitch-btn" 
                onClick={() => setShowHintText(true)}
                style={{ padding: '0.3rem 0.6rem', fontSize: '0.8rem', borderColor: 'var(--accent-secondary)', color: 'var(--accent-secondary)' }}
              >
                <Lightbulb size={14} /> DECODIFICAR PISTA
              </button>
            ) : (
              <div style={{ padding: '0.45rem 0.75rem', borderLeft: '3px solid var(--accent-secondary)', background: 'rgba(14, 165, 233, 0.1)', color: 'var(--accent-secondary)', fontStyle: 'italic', fontSize: '0.85rem' }}>
                <Lightbulb size={14} style={{ display: 'inline', marginBottom: '-2px', marginRight: '0.5rem' }} />
                {exercise.hint}
              </div>
            )}
          </div>
        )}
      </div>

      <div className="editor-workspace">
        <div className="code-pane">
          <div className="pane-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Code size={16} /> script.py
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <button
                onClick={handleDownloadCode}
                style={{
                  display: 'flex', alignItems: 'center', gap: '0.25rem',
                  background: 'rgba(16, 185, 129, 0.1)', border: '1px solid var(--accent-primary)',
                  color: 'var(--accent-primary)', cursor: 'pointer', padding: '0.2rem 0.5rem',
                  fontSize: '0.75rem', textTransform: 'uppercase',
                  transition: 'all 0.2s', borderRadius: '2px'
                }}
                title="Descargar código"
              >
                <Download size={14} /> Descargar
              </button>
              {hasError && (
                <button
                  onClick={handleClearCode}
                  style={{
                    display: 'flex', alignItems: 'center', gap: '0.25rem',
                    background: 'rgba(239, 68, 68, 0.1)', border: '1px solid var(--text-error)',
                    color: 'var(--text-error)', cursor: 'pointer', padding: '0.2rem 0.5rem',
                    fontSize: '0.75rem', textTransform: 'uppercase',
                    transition: 'all 0.2s', borderRadius: '2px'
                  }}
                >
                  <Trash2 size={14} /> Borrar código
                </button>
              )}
            </div>
          </div>
          <textarea
            className="code-textarea"
            value={code}
            onChange={e => setCode(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isSuccess}
            spellCheck={false}
          />
          <div style={{ display: 'flex' }}>
            <button
              className={`run-button ${loading ? 'loading' : ''} ${isSuccess ? 'success-btn' : ''}`}
              onClick={isSuccess ? (onNextExercise ? () => onNextExercise() : undefined) : handleRun}
              disabled={loading || (isSuccess && !onNextExercise) || explainLoading}
              style={{ flex: 1 }}
            >
              {loading ? <span className="spinner">⏳</span> : isSuccess ? <CheckCircle size={18} /> : <Play size={18} />}
              {loading ? 'Inicializando...' : isSuccess ? 'Siguiente Ejercicio' : 'Ejecutar'}
            </button>
            <button
              className="run-button explain-button"
              onClick={handleExplainCode}
              disabled={loading || explainLoading || code.trim().length < 5}
              style={{ flex: 1, borderLeft: '1px solid var(--border-color)', color: '#0ea5e9' }}
            >
              {explainLoading ? <span className="spinner">⏳</span> : <Terminal size={18} />}
              {explainLoading ? 'Analizando...' : 'Explicar Código (IA)'}
            </button>
          </div>
        </div>

        <div className="console-pane">
          <div className="pane-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Terminal size={16} /> stdout (Terminal / IA)
            </div>
            <button
              onClick={handleDownloadLog}
              style={{
                display: 'flex', alignItems: 'center', gap: '0.25rem',
                background: 'rgba(14, 165, 233, 0.1)', border: '1px solid #0ea5e9',
                color: '#0ea5e9', cursor: 'pointer', padding: '0.2rem 0.5rem',
                fontSize: '0.75rem', textTransform: 'uppercase',
                transition: 'all 0.2s', borderRadius: '2px'
              }}
              title="Descargar registro de terminal e IA"
            >
              <Download size={14} /> Descargar Log
            </button>
          </div>
          <div className="console-output" ref={consoleRef}>
            {outputLines.map((line, idx) => (
              <div key={idx} className={`output-line log-${line.type}`}>{line.text}</div>
            ))}
            {!isSuccess && <div className="blinking-cursor">_</div>}
          </div>
        </div>
      </div>

      {attempts >= 3 && !isSuccess && (
        <div className="solution-section">
          <button
            className="toggle-solution-btn glitch-btn"
            onClick={() => setShowSolution(!showSolution)}
          >
            {showSolution ? <EyeOff size={18} /> : <Eye size={18} />}
            {showSolution ? 'Ocultar Rescate' : 'Desencriptar Solución'}
          </button>

          {showSolution && (
            <div className="solution-content animate-slide-down">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Código de la solución:</span>
                <button
                  onClick={handleDownloadSolution}
                  style={{
                    display: 'flex', alignItems: 'center', gap: '0.25rem',
                    background: 'rgba(16, 185, 129, 0.1)', border: '1px solid var(--accent-primary)',
                    color: 'var(--accent-primary)', cursor: 'pointer', padding: '0.2rem 0.5rem',
                    fontSize: '0.75rem', textTransform: 'uppercase',
                    transition: 'all 0.2s', borderRadius: '2px'
                  }}
                  title="Descargar solución"
                >
                  <Download size={14} /> Descargar Solución
                </button>
              </div>
              <pre className="code-block solution-code">
                <code>{exercise.solution_code}</code>
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
