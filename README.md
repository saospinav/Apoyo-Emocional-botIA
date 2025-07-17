Nombre del Chatbot: Tu Asistente de Apoyo Emocional 💬
<img width="1049" height="818" alt="imagen" src="https://github.com/user-attachments/assets/3595252c-10c4-4065-8dbe-6a7cc8d98fc1" />
Descripción del proyecto

Este es un chatbot de inteligencia artificial diseñado para ofrecer apoyo emocional y un espacio seguro para la reflexión. Su objetivo es proporcionar una herramienta accesible para que las personas puedan expresar sus sentimientos y encontrar una perspectiva amable y empática. Este bot ha sido entrenado para ofrecer respuestas comprensivas, activas y que fomenten la autorreflexión.

El chatbot opera con una arquitectura de backend y frontend. El backend (escrito en Python con Flask y la API de OpenAI) maneja la lógica de inteligencia artificial y el procesamiento del lenguaje natural. El frontend (construido con HTML, CSS y JavaScript) proporciona la interfaz de usuario para la interacción.
Requerimientos

Para ejecutar este chatbot, necesitarás lo siguiente:
Para el Backend (Python con Flask y OpenAI)

    Python 3.8+

    Librerías de Python:

        Flask: Un microframework web para Python.

        Flask-CORS: Para manejar las políticas de Cross-Origin Resource Sharing (CORS) entre el frontend y el backend.

        openai: La librería oficial de OpenAI para interactuar con sus modelos.

    Clave API de OpenAI: Necesitarás una clave válida de la API de OpenAI. Esta debe configurarse como una variable de entorno (OPENAI_API_KEY) en el entorno donde se despliegue el backend por razones de seguridad.

Puedes instalar las dependencias de Python usando pip y el archivo requirements.txt:

pip install -r requirements.txt

Para el Frontend (HTML, CSS, JavaScript)

    Un navegador web moderno (Chrome, Firefox, Safari, Edge, etc.) para visualizar la interfaz de usuario.

    Conexión a internet para cargar Tailwind CSS desde CDN y para comunicarse con el backend desplegado.

Implementación

A continuación, se detalla la estructura principal del código, un diagrama de flujo de la interacción y una vista previa de la interfaz de usuario.
Código del Backend (Fragmento de app.py)

Este fragmento de código muestra cómo el backend de Flask maneja las solicitudes del frontend y se comunica con la API de OpenAI.

\documentclass{article}
\usepackage{minted} % Para resaltar código
\usepackage{xcolor} % Para colores en el código
\usepackage{geometry} % Para ajustar márgenes
\geometry{a4paper, left=1in, right=1in, top=1in, bottom=1in}

\begin{document}

\section*{Fragmento de C\'odigo del Backend (\texttt{app.py})}

\begin{minted}[
    frame=lines,
    framesep=2mm,
    linenos,
    breaklines=true,
    fontsize=\small,
    bgcolor=lightgray!10,
    fontfamily=tt,
    tabsize=4
]{python}
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    if not request.is_json:
        return jsonify({"error": "La solicitud debe ser JSON"}), 400

    data = request.get_json()
    mensaje = data.get("mensaje")

    if not mensaje:
        return jsonify({"error": "El campo 'mensaje' es requerido"}), 400

    try:
        respuesta_openai = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un chatbot de apoyo emocional para jóvenes. Sé empático, escucha, da consejos, ejercicios de respiración y detecta señales de alerta (como autolesiones o suicidio)."},
                {"role": "user", "content": mensaje}
            ]
        )
        contenido_bot = respuesta_openai["choices"][0]["message"]["content"]
        return jsonify({"respuesta": contenido_bot})

    except Exception as e:
        return jsonify({"respuesta": f"Ocurrió un error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
\end{minted}

\end{document}

Diagrama de Flujo de Interacción del Chatbot

Este diagrama ilustra el flujo de comunicación entre el usuario, el frontend y el backend del chatbot.

\documentclass{article}
\usepackage{tikz}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{geometry}
\geometry{a4paper, left=1in, right=1in, top=1in, bottom=1in}

\usetikzlibrary{shapes.geometric, arrows, positioning}

\begin{document}

\section*{Diagrama de Flujo de Interacci\'on del Chatbot}

\tikzset{
    startstop/.style={rectangle, rounded corners, minimum width=3cm, minimum height=1cm,text centered, draw=black, fill=red!30},
    process/.style={rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=orange!30},
    decision/.style={diamond, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=green!30},
    arrow/.style={thick,->,>=stealth'},
    io/.style={trapezium, trapezium left angle=70, trapezium right angle=110, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=blue!30},
    database/.style={cylinder, cylinder uses custom fill, cylinder body fill=purple!30, cylinder end fill=purple!50, minimum width=3cm, minimum height=1cm, text centered, draw=black},
    component/.style={rectangle, draw=black, fill=yellow!30, text centered, minimum width=3cm, minimum height=1cm, rounded corners},
}

\begin{figure}[h!]
    \centering
    \begin{tikzpicture}[node distance=1.5cm]

        \node (start) [startstop] {Inicio};
        \node (user_input) [io, below=of start] {Usuario escribe mensaje};
        \node (frontend) [component, below=of user_input] {Frontend (HTML/CSS/JS)};
        \node (send_request) [process, below=of frontend] {Enviar solicitud POST a Backend};
        \node (backend) [component, below=of send_request] {Backend (Flask/OpenAI)};
        \node (process_message) [process, below=of backend] {Procesar mensaje con OpenAI};
        \node (get_response) [process, below=of process_message] {Obtener respuesta de OpenAI};
        \node (send_response) [process, below=of get_response] {Enviar respuesta a Frontend};
        \node (display_message) [io, below=of send_response] {Mostrar respuesta en chat};
        \node (end) [startstop, below=of display_message] {Fin};

        \draw [arrow] (start) -- (user_input);
        \draw [arrow] (user_input) -- (frontend);
        \draw [arrow] (frontend) -- (send_request);
        \draw [arrow] (send_request) -- (backend);
        \draw [arrow] (backend) -- (process_message);
        \draw [arrow] (process_message) -- (get_response);
        \draw [arrow] (get_response) -- (send_response);
        \draw [arrow] (send_response) -- (display_message);
        \draw [arrow] (display_message) -- (end);

    \end{tikzpicture}
    \caption{Diagrama de Flujo de Interacción del Chatbot}
    \label{fig:flowchart}
\end{figure}

\end{document}

Vista Previa de la Interfaz de Usuario

Esta imagen muestra un ejemplo de cómo podría verse la interfaz de usuario del chatbot.

\documentclass{article}
\usepackage{graphicx}
\usepackage{geometry}
\geometry{a4paper, left=1in, right=1in, top=1in, bottom=1in}

\begin{document}

\section*{Vista Previa de la Interfaz de Usuario}

\begin{figure}[h!]
    \centering
    \includegraphics[width=0.8\textwidth]{imagen.png} % Asegúrate de que 'imagen.png' esté en la misma carpeta que tu archivo .tex
    \caption{Interfaz de Usuario del Chatbot (Ejemplo)}
    \label{fig:ui_preview}
\end{figure}

\end{document}

¡Importante! Descargo de Responsabilidad (Disclaimer)

Este chatbot NO es un sustituto de la ayuda profesional. El bot es una herramienta de apoyo y reflexión, pero no está calificado para diagnosticar, tratar o dar consejos médicos o psicológicos. Si te encuentras en una situación de crisis o necesitas ayuda profesional, por favor, contacta a una línea de ayuda o a un terapeuta.
