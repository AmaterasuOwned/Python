import requests
import logging

from pprint import pprint

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


url = "https://practicum.yandex.ru/api/user_api/homework_statuses/"
headers = {
    "Authorization": "OAuth y0_AgAAAAAs2JY0AAYckQAAAADRAUodKDJxu7V8Tw-XdImeZyQz3ele2FE"
}
payload = {"from_date": 1549962000}


homework_statuses = requests.get(url, headers=headers, params=payload)

pprint(homework_statuses.json())
