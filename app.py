from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/analyze_sentiment', methods=['OPTIONS', 'POST'])
def analyze_sentiment():
    if request.method == 'OPTIONS':
        # CORS preflight request
        response = jsonify({'status': 'OK'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

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

    response = jsonify({"sentiment": sentiment, "mood": mood})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)

