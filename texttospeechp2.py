# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:53:24 2021

@author: BH
"""


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator("YN-F10efu6L-NdjpB1OKBA7rCNKR4WXq8daXTr_JKGdp")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/de4a9ec4-27f4-40ce-867b-3f72bb0c5f8a")

with open ("C:/Users/BH/Desktop/t21.txt") as text_file:
    data = text_file.read()
    text_file.close()
    
    with open("t21A.mp3","wb") as audio:
        audio.write(text_2_speech.synthesize(data,accept="audio/mp3").get_result().content)
        