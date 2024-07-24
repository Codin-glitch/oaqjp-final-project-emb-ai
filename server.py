from EmotionDetection.emotion_detector import emotion_detector
from flask import Flask,request,render_template

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host = "0.0.0.0" , port = 5000)