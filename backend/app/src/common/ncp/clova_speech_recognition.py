from typing import Optional

from fastapi import status
from requests import Session, Response
from pydantic import HttpUrl

from src.constant import NCPAPIURL, NCPLanguageCode


class ClovaSpeechRecognitionAPI:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.session: Session = Session()
        self.session.headers: dict[str, str | bytes] = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
            "Content-Type": "application/octet-stream"
        }

    def recognize(self, language_code: Optional[NCPLanguageCode] = NCPLanguageCode.KOREAN) -> str:
        url: HttpUrl = NCPAPIURL.CLOVA_SPEECH_RECOGNITION.value + f"?lang=/{language_code.value}"
        response: Response = self.session.post(url=url, data=...)
        if response.status_code != status.HTTP_200_OK:
            raise

        return response.text
        