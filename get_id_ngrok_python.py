from pyngrok import ngrok
import yaml, os
from yaml.loader import SafeLoader


https_tunnel = ngrok.connect()

network_process = ngrok.get_ngrok_process()

try:
    ngrok_url = str(https_tunnel).split("->")[0].split("NgrokTunnel:")[-1].strip().replace("\"","")

    configuration_dictionary = {
        "telegram": {
            "access_token": "5326339686:AAE6B4VM2vUK69eDegKkmIWFa24Ki1ZwH5M",
            "verify": "IneuronHctnRasaKmkbot",
            "webhook_url": "a/webhooks/telegram/webhook"
        },
        "socketio": {
            "user_message_evt": "user_uttered",
            "bot_message_evt": "bot_uttered",
            "session_persistence": "true/false"
        },
        "rasa": {
            "url": "http://localhost:5002/api"
        }
    }

    configuration_dictionary["telegram"]["webhook_url"] = ngrok_url + "/webhooks/telegram/webhook"

    print("updated URL.")
    with open('/home/khyati/Desktop/hackathon_part2/rasa-bot-final/credentials.yml', 'w') as outfile:
        yaml.dump(configuration_dictionary, outfile)
    print(configuration_dictionary)


    os.system("rasa run")
    network_process.proc.wait()
except KeyboardInterrupt:
    print(" Shutting down server.")

    ngrok.kill()