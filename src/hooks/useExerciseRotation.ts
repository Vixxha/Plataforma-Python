import { useState, useEffect, useCallback } from 'react';
import type { Exercise } from './useExerciseLoader';

// 1 Hour in milliseconds
const ROTATION_INTERVAL = 60 * 60 * 1000;

export const useExerciseRotation = (exercises: Exercise[]) => {
  const [currentExercise, setCurrentExercise] = useState<Exercise | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(0);

  const selectRandomExercise = useCallback(() => {
    if (exercises.length === 0) return null;
    const randomIndex = Math.floor(Math.random() * exercises.length);
    const selected = exercises[randomIndex];
    
    // Save state to localStorage to persist rotation logic
    const state = {
      exerciseId: selected.id,
      timestamp: Date.now(),
    };
    localStorage.setItem('exercise_rotation_state', JSON.stringify(state));
    setCurrentExercise(selected);
    return selected;
  }, [exercises]);

  const forceExercise = useCallback((id: string) => {
    const found = exercises.find((ex) => ex.id === id);
    if (found) {
      setCurrentExercise(found);
      const state = {
        exerciseId: found.id,
        timestamp: Date.now(),
      };
      localStorage.setItem('exercise_rotation_state', JSON.stringify(state));
    }
  }, [exercises]);

  useEffect(() => {
    if (exercises.length === 0) return;

    let targetTime = 0;
    
    const initializeRotation = () => {
      const savedStateStr = localStorage.getItem('exercise_rotation_state');
      const now = Date.now();
      
      if (savedStateStr) {
        try {
          const savedState = JSON.parse(savedStateStr);
          const elapsed = now - savedState.timestamp;
          
          if (elapsed >= ROTATION_INTERVAL) {
            // Need a new exercise
            selectRandomExercise();
            targetTime = Date.now() + ROTATION_INTERVAL;
          } else {
            // Restore current exercise
            const found = exercises.find((ex) => ex.id === savedState.exerciseId);
            if (found) {
              setCurrentExercise(found);
              targetTime = savedState.timestamp + ROTATION_INTERVAL;
            } else {
               selectRandomExercise();
               targetTime = Date.now() + ROTATION_INTERVAL;
            }
          }
        } catch (e) {
          selectRandomExercise();
          targetTime = Date.now() + ROTATION_INTERVAL;
        }
      } else {
        selectRandomExercise();
        targetTime = Date.now() + ROTATION_INTERVAL;
      }
    };

    initializeRotation();

    // Timer to update time remaining every second
    const intervalId = setInterval(() => {
      const now = Date.now();
      const difference = targetTime - now;

      if (difference <= 0) {
        // Rotate now!
        selectRandomExercise();
        targetTime = Date.now() + ROTATION_INTERVAL;
        setTimeRemaining(ROTATION_INTERVAL);
      } else {
        setTimeRemaining(difference);
      }
    }, 1000);

    return () => clearInterval(intervalId);
  }, [exercises, selectRandomExercise]);

  return { currentExercise, timeRemaining, forceExercise, nextRandomExercise: selectRandomExercise };
};
