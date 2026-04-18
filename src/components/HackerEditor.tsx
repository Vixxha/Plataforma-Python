import React, { useState, useEffect, useRef } from 'react';
import { Terminal, Play, Eye, EyeOff, CheckCircle, Code, Trash2, Lightbulb } from 'lucide-react';
import type { Exercise } from '../hooks/useExerciseLoader';
import { usePythonExecutor } from '../hooks/usePythonExecutor';
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
  const { loading, runCode } = usePythonExecutor();
  const consoleRef = useRef<HTMLDivElement>(null);

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

    // Admin override bypass
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
        setTimeout(() => {
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

  const handleClearCode = () => {
    setCode(`# Escribe tu código aquí\n\n`);
    setHasError(false);
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

      {hintsEnabled && exercise.hint && (
        <div style={{ marginBottom: '1.5rem' }}>
          {!showHintText ? (
            <button 
              className="glitch-btn" 
              onClick={() => setShowHintText(true)}
              style={{ padding: '0.3rem 0.6rem', fontSize: '0.8rem', borderColor: 'var(--accent-secondary)', color: 'var(--accent-secondary)' }}
            >
              <Lightbulb size={14} /> DECODIFICAR PISTA
            </button>
          ) : (
            <div style={{ padding: '0.75rem', borderLeft: '3px solid var(--accent-secondary)', background: 'rgba(14, 165, 233, 0.1)', color: 'var(--accent-secondary)', fontStyle: 'italic', fontSize: '0.9rem' }}>
              <Lightbulb size={14} style={{ display: 'inline', marginBottom: '-2px', marginRight: '0.5rem' }} />
              {exercise.hint}
            </div>
          )}
        </div>
      )}

      <div className="editor-workspace">
        <div className="code-pane">
          <div className="pane-header">
            <Code size={16} /> script.py
            {hasError && (
              <button
                onClick={handleClearCode}
                style={{
                  display: 'flex', alignItems: 'center', gap: '0.25rem',
                  background: 'rgba(239, 68, 68, 0.1)', border: '1px solid var(--text-error)',
                  color: 'var(--text-error)', cursor: 'pointer', padding: '0.2rem 0.5rem',
                  fontSize: '0.75rem', textTransform: 'uppercase', marginLeft: '1rem',
                  transition: 'all 0.2s', borderRadius: '2px'
                }}
              >
                <Trash2 size={14} /> Borrar código
              </button>
            )}
          </div>
          <textarea
            className="code-textarea"
            value={code}
            onChange={e => setCode(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isSuccess}
            spellCheck={false}
          />
          <button
            className={`run-button ${loading ? 'loading' : ''} ${isSuccess ? 'success-btn' : ''}`}
            onClick={isSuccess ? (onNextExercise ? () => onNextExercise() : undefined) : handleRun}
            disabled={loading || (isSuccess && !onNextExercise)}
          >
            {loading ? <span className="spinner">⏳</span> : isSuccess ? <CheckCircle size={18} /> : <Play size={18} />}
            {loading ? 'Inicializando...' : isSuccess ? 'Siguiente Ejercicio' : 'Ejecutar'}
          </button>
        </div>

        <div className="console-pane">
          <div className="pane-header">
            <Terminal size={16} /> stdout
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
