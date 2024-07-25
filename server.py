'''Importing necessary modules'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detector import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emo_detector():
    ''' This function will analyze the text given by users and give the emotion score '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid test! Please try again!."
    return f"For the given statement, the system response is \
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \
    'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route('/')
def render_index_page():
    '''To render the home page'''
    return render_template('index.html')

if __name__=='__main__':
    app.run(host = "0.0.0.0" , port = 5000)
