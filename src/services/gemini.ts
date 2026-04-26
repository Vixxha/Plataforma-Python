export async function explainCodeWithGemini(code: string, exerciseDescription: string): Promise<string> {
  const apiKey = import.meta.env.VITE_GEMINI_API_KEY;

  if (!apiKey) {
    throw new Error('API Key de Gemini no configurada. Por favor, añade VITE_GEMINI_API_KEY en tu archivo .env');
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

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [
              { text: prompt }
            ]
          }
        ]
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`Error de Gemini: ${errorData.error?.message || response.statusText}`);
    }

    const data = await response.json();
    const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    
    if (!generatedText) {
      throw new Error('La API de Gemini devolvió una respuesta vacía o con formato inesperado.');
    }

    return generatedText.trim();
  } catch (error) {
    console.error('Error al llamar a Gemini:', error);
    if (error instanceof Error) {
      throw error;
    }
    throw new Error('Error desconocido al comunicarse con la IA.');
  }
}
