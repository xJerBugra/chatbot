from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Hugging Face Gradio Client - Buraya Kendi Modelinin ID'sini Gir
client = Client("rishikasharma/Chatbot") 

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message cannot be empty."}), 400

        # API ile Gradio Modeline Mesaj Gönderme
        response = client.predict(
            message=user_message,
            api_name="/chat"  # API endpoint'inin doğru olduğundan emin ol
        )

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
