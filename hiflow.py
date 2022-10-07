""" steps
packages: requests>=2.28.1

1. login hiflow.tencent.com
2. create template (Webhook接收数据后企微群机器人实时提醒)
3. copy webhook url
"""

from datetime import datetime
from typing import Dict, Optional

import requests

URL = 'https://api.hiflow.tencent.com/engine/webhook/31/1578380950266134530'

class Bot:
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, url: Optional[str] = URL) -> None:
        self.url = url

    def send(
        self,
        message: str,
        location: Optional[str] = "",
        metadata: Optional[Dict] = "",
    ) -> None:
        payload = {
            "datetime": datetime.now().strftime(self.DATETIME_FORMAT),
            "location": location,
            "message": message,
            "metadata": metadata
        }
        try:
            _ = requests.request("POST", self.url, json=payload)
        except Exception as e:
            print(f"request failed: {e}")
