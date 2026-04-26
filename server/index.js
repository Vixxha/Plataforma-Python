import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// API Endpoint para interactuar con Gemini
app.post('/api/explain', async (req, res) => {
  try {
    const { code, exerciseDescription } = req.body;

    if (!code || !exerciseDescription) {
      return res.status(400).json({ error: 'Se requiere code y exerciseDescription.' });
    }

    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      return res.status(500).json({ error: 'La API Key de Gemini no está configurada en el servidor.' });
    }

    const prompt = `
Eres un tutor experto en Python. Tu tarea es ayudar a un estudiante que está resolviendo el siguiente ejercicio:
"${exerciseDescription}"

El estudiante ha escrito el siguiente código:
\`\`\`python
${code}
\`\`\`

Por favor, analiza el código y explica de forma clara, amigable y concisa:
1. ¿Qué hace el código actualmente?
2. Si hay errores o problemas conceptuales, señálalos amablemente sin darle la solución completa de inmediato (da pistas).
3. Si el código es correcto, explícale por qué funciona bien.

Responde en texto plano o markdown muy simple, como si estuvieras en una terminal. Evita saludos largos, ve directo al grano.
`;

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key=${apiKey}`;

    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }]
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error?.message || response.statusText);
    }

    const data = await response.json();
    const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text;

    if (!generatedText) {
      throw new Error('La API de Gemini devolvió una respuesta vacía o con formato inesperado.');
    }

    res.json({ explanation: generatedText.trim() });
  } catch (error) {
    console.error('Error en /api/explain:', error);
    res.status(500).json({ error: error instanceof Error ? error.message : 'Error desconocido en el servidor.' });
  }
});

// En producción, servir los archivos estáticos de React
if (process.env.NODE_ENV === 'production') {
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = path.dirname(__filename);
  const distPath = path.join(__dirname, '../dist');
  app.use(express.static(distPath));
  
  app.get('*', (req, res) => {
    res.sendFile(path.join(distPath, 'index.html'));
  });
}

app.listen(PORT, () => {
  console.log(`🚀 Servidor backend corriendo en http://localhost:${PORT}`);
});
