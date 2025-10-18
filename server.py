'''server.py file'''
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    ''' emotionDetector get operation with text query string parameter'''
    text = request.args.get('text')
    scores = emotion_detector(text)

    if scores['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return scores

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
