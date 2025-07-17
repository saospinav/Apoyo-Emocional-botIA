from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Llave OpenAI (puedes pegar la tuya aquí directamente)
openai.api_key = "your_secretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.json
    mensaje = data.get("mensaje")

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un chatbot de apoyo emocional para jóvenes. Sé empático, escucha, da consejos, ejercicios de respiración y detecta señales de alerta (como autolesiones o suicidio)."},
                {"role": "user", "content": mensaje}
            ]
        )
        contenido = respuesta["choices"][0]["message"]["content"]
        return jsonify({"respuesta": contenido})
    except Exception as e:
        return jsonify({"respuesta": f"Ocurrió un error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
