import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('VAPI_CALL_URL')

payload = {
    "assistant": {
        "transcriber": {
            "provider": "deepgram",
            "model": "nova-2",
            "language": "de",
            "keywords": ["JoomAI"]
        },
        "model": {
            "model": "mixtral-8x7b-32768",
            "provider": "groq",
            "temperature": 0.5,
            "messages": [
                {
                    "content": "Als Call-Assistent liegt deine Aufgabe darin, Kunden oder Klienten telefonisch, per E-Mail oder im Live-Chat zu unterstützen und zu betreuen. Deine Hauptverantwortung besteht darin, exzellenten Kundenservice zu bieten, ihre Anfragen zu lösen und ihre Anliegen zeitnah und professionell anzugehen. Zu den wichtigsten Aufgaben eines Call-Assistenten können gehören:  Beantworten und Reagieren auf Kundenanfragen und -anliegen per Telefon. Bereitstellung genauer und hilfreicher Informationen an Kunden, Beantwortung ihrer Fragen und Anliegen und Lösung ihrer Probleme. Fehlerbehebung und Lösung von Kundenbeschwerden und -problemen auf faire und effiziente Weise. Aufrechterhaltung eines hohen Maßes an Kundenzufriedenheit durch exzellenten Kundenservice. Dokumentation von Kundeninteraktionen und Lösung von Problemen auf zeitnahe und genaue Weise sowie Bereitstellung hilfreicher Informationen für Kunden. Erfüllung und Übertreffen von Kundenservicemesswerten und Leistungszielen. Einhalten der Vertraulichkeit und Befolgung der Unternehmensrichtlinien und -verfahren. Als Call-Assistent bist du oft der erste Ansprechpartner für viele Kunden, und deine Rolle ist entscheidend für den Aufbau von Vertrauen, die Lösung von Problemen und die Bereitstellung einer exzellenten Kundenerfahrung",
                    "role": "assistant"
                }
            ]
        },
        "voice": {
            "provider": "11labs",
            "voiceId": "steve",
            "stability": 0.8,
            "style": 0,
            "similarityBoost": 1,
            "useSpeakerBoost": False,
            "optimizeStreamingLatency": 4,
            "model": "eleven_multilingual_v2"
        },
        "recordingEnabled": True,
        "endCallFunctionEnabled": True,
        "hipaaEnabled": False,
        "maxDurationSeconds": 599,
        "backgroundSound": "office",
        "name": "Philip",
        "forwardingPhoneNumbers": [{"number": os.getenv('TWILLIO_FORWARDING_NUMBER')}],
        "firstMessage": "Hallo Hier spricht Philip, dein KI-Assistent. Wie kann ich Ihnen heute helfen?",
        "dialKeypadFunctionEnabled": False,
        "serverMessages": ["end-of-call-report"],
        "endCallPhrases": ["schön Tag noch schau!"],
        "endCallMessage": "Vielen Dank für Ihren Anruf. Haben Sie einen schönen Tag!",
        "voicemailDetectionEnabled": True,
        "numWordsToInterruptAssistant": 2,
        "llmRequestDelaySeconds": 0.1,
        "serverUrl":os.getenv('WEBHOOK_SERVER_URL'),
        "responseDelaySeconds": 0.1,
        "forwardingPhoneNumber": os.getenv('TWILLIO_FORWARDING_NUMBER')
    },
    "maxDurationSeconds": 600,
    "phoneNumber": {
        "twilioPhoneNumber": os.getenv('TWILLIO_PHONENUMBER'),
        "twilioAccountSid": os.getenv('TWILLIO_ACCT_SID'),
        "twilioAuthToken": os.getenv('TWILLIO_AUTHTOKEN'),
        "serverUrl": os.getenv('WEBHOOK_SERVER_URL'),
        "name": "Emma"
    },
    "customer": {
        "number": os.getenv('TWILLIO_FORWARDING_NUMBER'),#using this for test purpose only
        "name": ""
    }
}
headers = {
    "Authorization": os.getenv('VAPI_BEARER_TOKEN'),
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
#print(json.dumps(response.text, indent=4))
print(response.text)
