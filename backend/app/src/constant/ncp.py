from enum import Enum
from types import DynamicClassAttribute


class NCPAPIURL(str, Enum):
    _BASE_URL: str = "https://naveropenapi.apigw.ntruss.com"

    CLOVA_SPEECH_RECOGNITION: str = "/recog/v1/stt"
    CLOVA_VOICE: str = "/tts-premium/v1/tts"

    @DynamicClassAttribute
    def value(self) -> str:
        return "".join([NCPAPIURL._BASE_URL, self._value_])


class NCPLanguageCode(str, Enum):
    KOREAN: str = "Kor"
    ENGLISH: str = "Eng"
