from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        mood = "Positive"
    elif sentiment < 0:
        mood = "Negative"
    else:
        mood = "Neutral"
    return jsonify({"sentiment": sentiment, "mood": mood})

if __name__ == '__main__':
    app.run(debug=True)
