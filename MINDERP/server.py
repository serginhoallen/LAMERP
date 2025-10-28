from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        url = "http://localhost:11434/api/chat"
        
        response = requests.post(url, json={
            "model": "llama3",
            "messages": data.get('messages', []),
            "stream": False
        })
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Erro ao comunicar com Ollama"}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            return jsonify({"status": "online"})
        return jsonify({"status": "offline"}), 500
    except:
        return jsonify({"status": "offline"}), 500

if __name__ == '__main__':
    print("🚀 Servidor MINDERP rodando em http://localhost:5000")
    print("📡 Conectando ao Ollama em http://localhost:11434")
    app.run(host='0.0.0.0', port=5000, debug=True)

