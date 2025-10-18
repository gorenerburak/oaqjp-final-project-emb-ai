from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get('text')
    return emotion_detector(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)