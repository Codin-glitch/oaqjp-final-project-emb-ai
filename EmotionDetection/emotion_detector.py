import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if not text_to_analyse.strip():
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None, 
        "dominant_emotion":None
        }
    
    elif response.status_code == 200:
        d = dict(formatted_response['emotionPredictions'][0]['emotion'])

        max_score = 0
        for key in d:
            if d[key]>max_score:
                max_score=d[key]
                dominant_emotion = key
        d['dominant_emotion'] = dominant_emotion
        return d
    elif response.status_code == 400:
        d = dict(formatted_response['emotionPredictions'][0]['emotion'])
        for key in d.keys():
            d[key] = None
        d['dominant_amotion'] = None
        return d
    