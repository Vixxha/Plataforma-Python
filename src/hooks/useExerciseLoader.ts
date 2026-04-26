import { useState, useEffect } from 'react';

export interface Exercise {
  id: string | number;
  title: string;
  description: string;
  difficulty?: string;
  expected_output: string;
  solution_code: string;
  tests_code: string;
  hint?: string;
}

const parsePythonExercise = (content: string, id: string): Exercise => {
  const sections = content.split(/#\s*===\s*(METADATA|SOLUTION|TESTS)\s*===.*(?:\r?\n|$)/);

  let title = "Sin Título";
  let description = "Sin descripción";
  let difficulty = "Básico";
  let expected_output = "";
  let solution_code = "";
  let tests_code = "";
  let hint = undefined;

  for (let i = 1; i < sections.length; i += 2) {
    const sectionName = sections[i];
    const sectionBody = sections[i + 1].trim();

    if (sectionName === "METADATA") {
      const lines = sectionBody.split(/\r?\n/);
      for (const line of lines) {
        const match = line.replace(/^#\s*/, '').match(/^([^:]+):\s*(.*)$/);
        if (match) {
          const key = match[1].trim().toLowerCase();
          const value = match[2].trim();
          if (key === "title") title = value;
          if (key === "description") description = value;
          if (key === "difficulty") difficulty = value;
          if (key === "expected_output") expected_output = value;
          if (key === "hint") hint = value;
        }
      }
    } else if (sectionName === "SOLUTION") {
      solution_code = sectionBody;
    } else if (sectionName === "TESTS") {
      tests_code = sectionBody;
    }
  }

  return { id, title, description, difficulty, expected_output, solution_code, tests_code, hint };
};

const MAX_EXERCISES = 60;

export const useExerciseLoader = () => {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;

    const fetchExercises = async () => {
      try {
        setLoading(true);

        const results = await Promise.allSettled(
          Array.from({ length: MAX_EXERCISES }, (_, i) =>
            fetch(`/exercises/${i + 1}.py`).then(async (r) => {
              if (!r.ok) return null;
              const text = await r.text();
              if (text.trim().startsWith('<')) return null;
              return { index: i + 1, text };
            })
          )
        );

        const loadedExercises: Exercise[] = [];
        for (const result of results) {
          if (result.status === 'fulfilled' && result.value !== null) {
            const { index, text } = result.value;
            loadedExercises.push(parsePythonExercise(text, index.toString()));
          } else {
            break;
          }
        }

        if (isMounted) {
          setExercises(loadedExercises);
          setLoading(false);
        }
      } catch (err: unknown) {
        if (isMounted) {
          const errorMessage = err instanceof Error ? err.message : String(err);
          setError(errorMessage || 'Error cargando los ejercicios');
          setLoading(false);
        }
      }
    };

    fetchExercises();

    return () => {
      isMounted = false;
    };
  }, []);

  return { exercises, loading, error };
};
