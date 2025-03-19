from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Hugging Face Gradio Client
client = Client("rishikasharma/Chatbot")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Hugging Face chatbot API'yi çağır
        response = client.predict(
            message=user_message,
            system_message="You are a friendly Chatbot.",
            api_name="/chat"
        )

        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
