from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.controller import Controller
from voice.commands import CommandProcessor

app = Flask(__name__)
CORS(app)

controller = Controller()
processor = CommandProcessor()


@app.route("/api/voice/command", methods=["POST"])
def voice_command():
    data = request.get_json()
    text = data.get("text", "")

    result = processor.process(text)
    controller.speak(result["response"])

    return jsonify(result)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "backend running"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)