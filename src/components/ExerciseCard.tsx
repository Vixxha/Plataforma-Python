import React, { useState } from 'react';
import { Terminal, Code, ChevronDown, ChevronUp } from 'lucide-react';
import type { Exercise } from '../hooks/useExerciseLoader';
import './ExerciseCard.css';

interface Props {
  exercise: Exercise | null;
}

export const ExerciseCard: React.FC<Props> = ({ exercise }) => {
  const [showSolution, setShowSolution] = useState(false);

  if (!exercise) return null;

  return (
    <div className="exercise-card">
      <div className="exercise-header">
        <h2 className="exercise-title">{exercise.title}</h2>
        <span className="exercise-id">#{exercise.id}</span>
      </div>
      
      <div className="exercise-content">
        <p className="exercise-description">{exercise.description}</p>
        
        <div className="section-block">
          <h3 className="section-title">
            <Terminal size={18} />Resultado Esperado
          </h3>
          <pre className="code-block expected-output">
            <code>{exercise.expected_output}</code>
          </pre>
        </div>

        <div className="solution-section">
          <button 
            className="toggle-solution-btn" 
            onClick={() => setShowSolution(!showSolution)}
          >
            {showSolution ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
            {showSolution ? 'Ocultar Solución' : 'Ver Solución'}
          </button>
          
          {showSolution && (
            <div className="solution-content animate-slide-down">
              <h3 className="section-title">
                <Code size={18} />Código de Solución
              </h3>
              <pre className="code-block solution-code">
                <code>{exercise.solution_code}</code>
              </pre>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
