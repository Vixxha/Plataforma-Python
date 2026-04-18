import { useState, useEffect, useCallback } from 'react';

declare global {
  interface Window {
    loadPyodide: (config: { indexURL: string }) => Promise<any>;
  }
}

export const usePythonExecutor = () => {
  const [pyodide, setPyodide] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let script = document.getElementById('pyodide-script') as HTMLScriptElement;
    
    if (!script) {
      script = document.createElement('script');
      script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
      script.id = 'pyodide-script';
      document.head.appendChild(script);
    }

    const initPyodide = async () => {
      try {
        if (!window.loadPyodide) {
           await new Promise(resolve => {
               if(script) script.addEventListener('load', resolve);
           });
        }
        const py = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });
        setPyodide(py);
        setLoading(false);
      } catch (err) {
        console.error("Error loading Pyodide:", err);
      }
    };

    if (!pyodide && !window.loadPyodide) {
       script.addEventListener('load', initPyodide);
    } else if (!pyodide) {
       initPyodide();
    }
  }, [pyodide]);

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
      await pyodide.runPythonAsync(fullCode);
      
      const stdout = pyodide.runPython("sys.stdout.getvalue()");
      return { success: true, stdout };
    } catch (error: any) {
      const stderr = pyodide.runPython("sys.stderr.getvalue()");
      return { success: false, error: error.toString(), stderr };
    }
  }, [pyodide]);

  return { loading, runCode };
};
