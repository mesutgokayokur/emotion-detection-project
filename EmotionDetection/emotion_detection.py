import requests
import json

def emotion_detector(text_to_analyze):
    """
    Watson NLP API kullanarak metindeki duygu analizini yapar.
    """
    # Watson NLP API URL'si
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # API için gerekli başlıklar (Model ID buraya eklenir)
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Gönderilecek veri formatı
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # POST isteği gönderilmesi
    response = requests.post(url, json=myobj, headers=header)
    
    # Yanıtın JSON formatına dönüştürülmesi
    return response.text
