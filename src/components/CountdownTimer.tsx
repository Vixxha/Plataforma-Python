import React from 'react';
import { Clock } from 'lucide-react';
import './CountdownTimer.css';

interface Props {
  timeRemaining: number;
}

export const CountdownTimer: React.FC<Props> = ({ timeRemaining }) => {
  const hours = Math.floor(timeRemaining / (1000 * 60 * 60));
  const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

  const format = (val: number) => val.toString().padStart(2, '0');

  return (
    <div className="countdown-container">
      <div className="countdown-badge">
        <Clock className="countdown-icon" size={18} />
        <span className="countdown-text">
          Próximo ejercicio en: <span className="countdown-time">{format(hours)}:{format(minutes)}:{format(seconds)}</span>
        </span>
      </div>
    </div>
  );
};
