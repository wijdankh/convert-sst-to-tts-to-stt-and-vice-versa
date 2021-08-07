# -*- coding: utf-8 -*-
"""
Created on  13:23:45 2021

@author: BH
"""

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


api = IAMAuthenticator("w9y5nr-Si-YABIljMa3D0gJ3DtQmNbrz_y4vjjA0tGL0")
speech_2_text = SpeechToTextV1(authenticator=api)
speech_2_text.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/338edba0-1463-4837-8ace-1da3e1cfc62a")

with open("C:/Users/BH/Desktop/h.mp3","rb") as audio_file:
    result = speech_2_text.recognize(
        audio=audio_file,content_type="audio/mp3"
        ).get_result()

print(result)