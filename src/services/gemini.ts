export async function explainCodeWithGemini(code: string, exerciseDescription: string): Promise<string> {
  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001';
  const url = `${API_URL}/api/explain`;

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code, exerciseDescription })
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`Error del servidor: ${errorData.error || response.statusText}`);
    }

    const data = await response.json();
    return data.explanation;
  } catch (error) {
    if (error instanceof Error) {
      throw error;
    }
    throw new Error('Error desconocido al comunicarse con el backend.');
  }
}
