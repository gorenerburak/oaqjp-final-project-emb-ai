'''server.py file'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''Render the landing page'''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    ''' emotionDetector get operation with text query string parameter'''
    text = request.args.get('textToAnalyze')
    scores = emotion_detector(text)

    if scores['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {scores['anger']}, "
            f"'disgust': {scores['disgust']}, 'fear': {scores['fear']}, 'joy': {scores['joy']} and 'sadness': {scores['sadness']}. "
            f"The dominant emotion is {scores['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
