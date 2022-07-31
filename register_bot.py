import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = '5598727208:AAFHWGuk9vXaPl31rmhT9DftrZ73AyhgKjE'
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
WEBHOOK_URL = 'https://1725-51-195-169-104.eu.ngrok.io'


def register_webhook():
    response = requests.get(
        f'https://api.telegram.org/bot{API_TOKEN}/setWebhook?url={WEBHOOK_URL}'
    )
    print("Запуск бота:", response.status_code, response.text)


if __name__ == '__main__':
    register_webhook()