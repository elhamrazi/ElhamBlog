from ibm_watson import TextToSpeechV1, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import exists

authenticator = IAMAuthenticator('A3ui7FpxMgOI2NHoWeIiWG_eQ13TKEPHDeixkLPMD1RK')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/e02d50df-3de0-4122-aec5-cdd99d8d231a')


def text2speech(text, name):
    path = 'main/static/' + name
    print(path)
    if not exists(path):
        with open(path, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    text,
                    voice='en-US_AllisonV3Voice',
                    accept='audio/wav'
                ).get_result().content)


def text_analysis(text):

    authenticator = IAMAuthenticator('guFBWnDvIRyPdh9VPiXCJ5nERkMaoA5V-TvX-tpJFWpj')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-03-25',
        authenticator=authenticator)

    natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/3512fe3f-03e6-45e8-9539-78b354d92a73')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=1),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                     limit=2))).get_result()

    return response
