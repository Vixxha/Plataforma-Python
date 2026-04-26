# Plataforma Hacker de Ejercicios en Python

## Descripción
Esta es una plataforma web interactiva con temática de terminal "hacker", diseñada para aprender y practicar programación en Python. Los usuarios pueden resolver decenas de ejercicios (actualmente más de 90 disponibles) directamente desde el navegador, evaluar su código y recibir retroalimentación instantánea.

## Características Principales
- 💻 **Editor Integrado:** Escribe y ejecuta código Python en tiempo real usando Pyodide (Python ejecutándose en WebAssembly), sin necesidad de instalar nada en tu computadora.
- 🤖 **Asistente de Inteligencia Artificial (Gemini):** ¿Atascado en un problema? Usa el botón de IA integrado para obtener explicaciones paso a paso de tu código, analizar errores lógicos o de sintaxis, y recibir pistas personalizadas.
- 📂 **Generación Continua de Ejercicios:** Cuenta con un flujo de trabajo (GitHub Actions) que genera y agrega automáticamente nuevos retos de Python periódicamente utilizando la API de Gemini.
- 💾 **Descargas Integradas:** Tienes la opción de descargar:
  - Tu propio código (`.py`).
  - Los registros de la terminal, incluyendo la explicación y análisis de la IA (`.txt`).
  - El código de la solución oficial del ejercicio.
- 🔐 **Sistema de Intentos:** Dispones de 3 intentos para resolver un ejercicio. Solo después de fallar 3 veces, el sistema "desencriptará" y te mostrará la solución oficial.
- 🎨 **Interfaz Ciberpunk:** Animaciones "glitch", efectos de terminal antigua y colores neón que hacen la experiencia de aprendizaje mucho más divertida e inmersiva.

## Tecnologías Utilizadas
- **Frontend:** React + TypeScript + Vite
- **Ejecución de Python:** Pyodide
- **Inteligencia Artificial:** Google Gemini API (Flash-Lite)
- **Estilos:** CSS Vanilla

## Instalación y Uso Local

Para correr este proyecto en tu propia máquina:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Vixxha/Plataforma-Python.git
   cd Plataforma-Python
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Configura las variables de entorno:
   - Copia o renombra el archivo `.env.example` a `.env`
   - Agrega tu clave de API de Google Gemini:
     ```env
     VITE_GEMINI_API_KEY=tu_clave_aqui
     ```

4. Inicia el servidor de desarrollo:
   ```bash
   npm run dev
   ```

---
*Este proyecto fue construido y automatizado para facilitar la enseñanza y el aprendizaje práctico de la programación en Python.*
