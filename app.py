from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 "gpt-4" 등
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    message = response.choices[0].message['content'].strip()
    return jsonify({"response": message})

if __name__ == '__main__':
    app.run(debug=True)