import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('VAPI_CALL_URL_ASSISTANT')

payload = {
    "transcriber": {
        "provider": "deepgram",
        "model": "nova-2",
        "language": "de"
    },
    "model": {
        "provider": "openai",
        "model": "gpt-3.5-turbo-0613",
        "semanticCachingEnabled": True,
        "temperature": 0.5,
        "maxTokens": 300,
        "messages": [
            {
                "content": "As a Pizza Order Assistant at PizzaPal, you'll be the cheerful voice on the other end of the line, guiding customers through our tantalizing menu offerings and ensuring their pizza cravings are satisfied to perfection. With a focus on efficiency, accuracy, and outstanding customer service, you'll play a key role in making every order experience a slice of pizza paradise.  Key Responsibilities:  Order Management:  1. Assist customers in selecting from our mouthwatering array of pizzas, including Pepperoni Pizza, Garlic Pizza, and Veggie Pizza. 2. Expertly record customer preferences for pizza size, crust type, and additional toppings to create their perfect pie. 3. Process orders swiftly and accurately, ensuring all details are captured to guarantee a delightful dining experience.  Customer Interaction: Engage with customers in a friendly and enthusiastic manner, offering recommendations and answering questions about our menu items. Provide information about our three delectable sides: French Fries, Garlic Bread, and Chicken Wings, to complement their pizza order.{{customerOrder}} Address customer inquiries and resolve any concerns with professionalism and empathy, ensuring customer satisfaction is always the top priority.  Upselling and Promotion: Highlight current specials and promotions to customers, encouraging them to take advantage of our irresistible deals. Suggest add-on items such as sides or drinks to enhance the dining experience and increase order value. Utilize persuasive communication skills to upsell premium toppings or larger-sized pizzas to meet customer preferences.  Send Order: Please confirm Customer Order once more and send then call 'CustomerOrder' function.",
                "role": "system",
                "tool_calls": [None],
                "function_call": {"OrderFunction": {
                        "customerOrder": "name",
                        "purpose": "purpose"
                    }}
            }
        ]
    },
    "voice": {
        "provider": "playht",
        "voiceId": "melissa",
        "temperature": 0.5,
        "emotion": "female_happy",
        "styleGuidance": 1,
        "textGuidance": None,
        "speed": None
    },
    "recordingEnabled": True,
    "endCallFunctionEnabled": True,
    "hipaaEnabled": True,
    "serverMessages": ["function-call"],
    "silenceTimeoutSeconds": 30,
    "responseDelaySeconds": 0.4,
    "llmRequestDelaySeconds": 0.1,
    "numWordsToInterruptAssistant": 2,
    "maxDurationSeconds": 600,
    "backgroundSound": "office",
    "name": "Jenifer",
    "forwardingPhoneNumbers": [{"number": os.getenv('TWILLIO_FORWARDING_NUMBER')}],
    "firstMessage": "Hallo,ich bin Jenifer, wie kann ich ihnen hilfen?",
    "voicemailDetectionEnabled": True,
    "endCallMessage": "aufwiedersehen",
    "endCallPhrases": ["schuss!!"],
    "serverUrl": "https://hook.eu2.make.com/otlk4lxjkdryewwkqu1r5meldlvaxig5",
    "forwardingPhoneNumber": os.getenv('TWILLIO_FORWARDING_NUMBER')
}
headers = {
    "Authorization": "Bearer dd62f3f4-c965-4a9c-9c0b-a8da4165b617",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)