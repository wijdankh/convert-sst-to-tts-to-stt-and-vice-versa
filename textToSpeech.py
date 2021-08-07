# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:07:44 2021

@author: BH
"""

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator("YN-F10efu6L-NdjpB1OKBA7rCNKR4WXq8daXTr_JKGdp")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/de4a9ec4-27f4-40ce-867b-3f72bb0c5f8a")

with open ("hi.mp3","wb") as audiofile:
    audiofile.write(
        text_2_speech.synthesize (" hello world", accept="audio/mp3").get_result().content
        )