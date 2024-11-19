from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to send data to the FastAPI backend
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    story_context = request.form['story_context']
    try:
        # Call FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/generate-story/",
            json={"user_input": user_input, "story_context": story_context}
        )
        response_data = response.json()
        return jsonify({"story": response_data.get('story', "Failed to get story.")})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)