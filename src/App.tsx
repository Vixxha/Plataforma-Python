import { Terminal, Users, Lightbulb, LightbulbOff } from 'lucide-react';
import { useState } from 'react';
import { useExerciseLoader } from './hooks/useExerciseLoader';
import { useExerciseRotation } from './hooks/useExerciseRotation';
import { CountdownTimer } from './components/CountdownTimer';
import { HackerEditor } from './components/HackerEditor';
import { Footer } from './components/Footer';
import './App.css';

function App() {
  const { exercises, loading, error } = useExerciseLoader();
  const { currentExercise, timeRemaining, forceExercise, nextRandomExercise } = useExerciseRotation(exercises);
  const [userName, setUserName] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);
  const [hintsEnabled, setHintsEnabled] = useState(true);

  return (
    <>
      <div className="scanline-overlay"></div>
      <div className="app-container">
        <header className="app-header">
          <div className="logo-container">
            <img src="/logo.png" alt="Sys.Py Logo" className="logo-image glitch" onError={(e) => { e.currentTarget.style.display = 'none'; (e.currentTarget.nextElementSibling as HTMLElement).style.display = 'block'; }} />
            <Terminal size={32} className="logo-icon glitch fallback-icon" style={{ display: 'none' }} />
            <h1 className="app-title">SYS<span>.PY</span></h1>
          </div>

          <div className="user-login-form">
            {!loggedIn ? (
              <>
                <input 
                  type="text" 
                  className="user-input" 
                  placeholder="INGRESA ALIAS..." 
                  value={userName}
                  onChange={(e) => setUserName(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && userName && setLoggedIn(true)}
                />
                <button 
                  className="run-button" 
                  onClick={() => setLoggedIn(true)}
                  disabled={!userName}
                >
                  ENTER
                </button>
              </>
            ) : (
              <div className="user-display">
                <button 
                  className="glitch-btn" 
                  style={{ marginRight: '1rem', border: '1px solid var(--border-color)', padding: '0.3rem 0.6rem', gap: '0.4rem', fontSize: '0.75rem', color: hintsEnabled ? 'var(--accent-primary)' : '#666' }}
                  onClick={() => setHintsEnabled(!hintsEnabled)}
                  title={hintsEnabled ? "Desactivar Pistas (Más difícil)" : "Activar Pistas (Con ayuda)"}
                >
                  {hintsEnabled ? <Lightbulb size={14} /> : <LightbulbOff size={14} />}
                  {hintsEnabled ? 'Pistas: ON' : 'Pistas: OFF'}
                </button>
                <Users size={18} /> {userName}
              </div>
            )}
          </div>
        </header>

        <main className="app-main">
          {loading ? (
            <div className="terminal-loader">
              <Terminal className="spinner" size={48} />
              <p>INITIALIZING SECURE CONNECTION...</p>
            </div>
          ) : error ? (
            <div className="error-state">
              <p>{error}</p>
            </div>
          ) : exercises.length === 0 ? (
            <div className="empty-state">
              <h2 className="glitch">404 NOT FOUND</h2>
              <p>No valid .py targets discovered in vector /exercises.</p>
            </div>
          ) : (
            <div className="exercise-view">
              <CountdownTimer timeRemaining={timeRemaining} />
              <HackerEditor 
                exercise={currentExercise} 
                userName={userName} 
                onForceExercise={forceExercise}
                onNextExercise={nextRandomExercise}
                hintsEnabled={hintsEnabled}
              />
            </div>
          )}
        </main>
        <Footer />
      </div>
    </>
  );
}

export default App;
