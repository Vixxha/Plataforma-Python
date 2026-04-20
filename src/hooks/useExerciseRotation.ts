import { useState, useEffect, useCallback } from 'react';
import type { Exercise } from './useExerciseLoader';

// 1 Hour in milliseconds
const ROTATION_INTERVAL = 60 * 60 * 1000;

export const useExerciseRotation = (exercises: Exercise[]) => {
  const [currentExercise, setCurrentExercise] = useState<Exercise | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(0);

  // Allow temporary manual override for the current user's session without breaking global sync
  const [sessionOffset, setSessionOffset] = useState<number>(0);
  const [forcedExerciseId, setForcedExerciseId] = useState<string | null>(null);

  const forceExercise = useCallback((id: string) => {
    setForcedExerciseId(id);
    setSessionOffset(0);
  }, []);

  const nextRandomExercise = useCallback(() => {
    // We just increase the offset locally so the user can keep playing if they finish early
    setSessionOffset(prev => prev + 1);
    setForcedExerciseId(null);
  }, []);

  useEffect(() => {
    if (exercises.length === 0) return;

    const updateRotation = () => {
      const now = Date.now();
      
      // Calculate global synchronized window block (everyone in the world gets same ID)
      const currentWindow = Math.floor(now / ROTATION_INTERVAL);
      
      // Select the exercise deterministically based on time window + any session local skips
      const rawIndex = currentWindow + sessionOffset;
      const exerciseIndex = rawIndex % exercises.length;
      
      if (forcedExerciseId) {
        const found = exercises.find(ex => ex.id === forcedExerciseId);
        if (found) {
          setCurrentExercise(found);
        } else {
          setCurrentExercise(exercises[exerciseIndex]);
        }
      } else {
        setCurrentExercise(exercises[exerciseIndex]);
      }

      // Calculate time remaining in the global window
      const remaining = ROTATION_INTERVAL - (now % ROTATION_INTERVAL);
      setTimeRemaining(remaining);
    };

    updateRotation();
    const intervalId = setInterval(updateRotation, 1000);

    return () => clearInterval(intervalId);
  }, [exercises, sessionOffset, forcedExerciseId]);

  return { currentExercise, timeRemaining, forceExercise, nextRandomExercise };
};
