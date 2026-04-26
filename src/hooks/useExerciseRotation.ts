import { useState, useEffect, useCallback } from 'react';
import type { Exercise } from './useExerciseLoader';

const ROTATION_INTERVAL = 60 * 60 * 1000;
const CACHE_KEY = 'time_offset_cache';
const CACHE_TTL = 60 * 60 * 1000;

const getCachedOffset = (): number | null => {
  try {
    const raw = sessionStorage.getItem(CACHE_KEY);
    if (!raw) return null;
    const { offset, timestamp } = JSON.parse(raw);
    return Date.now() - timestamp < CACHE_TTL ? offset : null;
  } catch {
    return null;
  }
};

const setCachedOffset = (offset: number) => {
  try {
    sessionStorage.setItem(CACHE_KEY, JSON.stringify({ offset, timestamp: Date.now() }));
  } catch (err) {
    console.warn('Error cache:', err);
  }
};

export const useExerciseRotation = (exercises: Exercise[]) => {
  const [currentExercise, setCurrentExercise] = useState<Exercise | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(0);
  const [timeOffset, setTimeOffset] = useState<number | null>(() => getCachedOffset());
  const [sessionOffset, setSessionOffset] = useState<number>(0);
  const [forcedExerciseId, setForcedExerciseId] = useState<string | null>(null);

  const forceExercise = useCallback((id: string) => {
    setForcedExerciseId(id);
    setSessionOffset(0);
  }, []);

  const nextRandomExercise = useCallback(() => {
    setSessionOffset(prev => prev + 1);
    setForcedExerciseId(null);
  }, []);

  useEffect(() => {
    if (getCachedOffset() !== null) return;

    const fetchGlobalTime = async () => {
      try {
        const response = await fetch('https://worldtimeapi.org/api/timezone/Etc/UTC');
        const data = await response.json();
        const offset = new Date(data.utc_datetime).getTime() - Date.now();
        setCachedOffset(offset);
        setTimeOffset(offset);
      } catch (error) {
        console.error("Error al sincronizar la hora global. Usando la hora local de la PC:", error);
        setCachedOffset(0);
        setTimeOffset(0);
      }
    };
    fetchGlobalTime();
  }, []);

  useEffect(() => {
    if (exercises.length === 0 || timeOffset === null) return;

    const updateRotation = () => {
      const now = Date.now() + timeOffset;
      const currentWindow = Math.floor(now / ROTATION_INTERVAL);
      const exerciseIndex = (currentWindow + sessionOffset) % exercises.length;

      if (forcedExerciseId) {
        const found = exercises.find(ex => ex.id === forcedExerciseId);
        setCurrentExercise(found ?? exercises[exerciseIndex]);
      } else {
        setCurrentExercise(exercises[exerciseIndex]);
      }

      setTimeRemaining(ROTATION_INTERVAL - (now % ROTATION_INTERVAL));
    };

    updateRotation();
    const intervalId = setInterval(updateRotation, 1000);
    return () => clearInterval(intervalId);
  }, [exercises, sessionOffset, forcedExerciseId, timeOffset]);

  return { currentExercise, timeRemaining, forceExercise, nextRandomExercise };
};
