import { useState, useEffect, useCallback } from 'react';

declare global {
  interface Window {
    loadPyodide?: (config: { indexURL: string }) => Promise<any>;
  }
}

const EXECUTION_TIMEOUT_MS = 10_000;

// Module-level singletons: Pyodide is initialized once per page load
let pyodideInstance: any = null;
let pyodideLoadPromise: Promise<any> | null = null;

const loadPyodideOnce = (): Promise<any> => {
  if (pyodideInstance) return Promise.resolve(pyodideInstance);
  if (pyodideLoadPromise) return pyodideLoadPromise;

  pyodideLoadPromise = new Promise<any>((resolve, reject) => {
    const init = async () => {
      try {
        const py = await window.loadPyodide!({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });
        pyodideInstance = py;
        resolve(py);
      } catch (err) {
        pyodideLoadPromise = null;
        reject(err);
      }
    };

    if (window.loadPyodide) {
      init();
      return;
    }

    const existing = document.getElementById('pyodide-script') as HTMLScriptElement | null;
    if (existing) {
      existing.addEventListener('load', init, { once: true });
      return;
    }

    const script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
    script.id = 'pyodide-script';
    script.addEventListener('load', init, { once: true });
    script.addEventListener('error', () => {
      pyodideLoadPromise = null;
      reject(new Error('Error cargando el script de Pyodide'));
    }, { once: true });
    document.head.appendChild(script);
  });

  return pyodideLoadPromise;
};

export const usePythonExecutor = () => {
  const [pyodide, setPyodide] = useState<any>(pyodideInstance);
  const [loading, setLoading] = useState(!pyodideInstance);

  useEffect(() => {
    if (pyodideInstance) return;

    loadPyodideOnce()
      .then((py) => {
        setPyodide(py);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error loading Pyodide:", err);
        setLoading(false);
      });
  }, []);

  const runCode = useCallback(async (userCode: string, testCode: string) => {
    if (!pyodide) return { success: false, error: "Pyodide no está cargado." };

    try {
      await pyodide.runPythonAsync(`
import sys
import io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
`);

      const fullCode = `${userCode}\n\n${testCode}`;

      const timeout = new Promise<never>((_, reject) =>
        setTimeout(
          () => reject(new Error(`[TIMEOUT] Ejecución cancelada tras ${EXECUTION_TIMEOUT_MS / 1000}s. ¿Hay un loop infinito?`)),
          EXECUTION_TIMEOUT_MS
        )
      );

      await Promise.race([pyodide.runPythonAsync(fullCode), timeout]);

      const stdout = pyodide.runPython("sys.stdout.getvalue()");
      return { success: true, stdout };
    } catch (error: any) {
      const stderr = pyodide.runPython("sys.stderr.getvalue()");
      return { success: false, error: error.toString(), stderr };
    }
  }, [pyodide]);

  return { loading, runCode };
};
