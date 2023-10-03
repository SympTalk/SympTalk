from enum import Enum
from types import DynamicClassAttribute


class OpenAIAPIURL(str, Enum):
    _BASE_URL: str = "https://api.openai.com/v1"
    CHAT_COMPLETION: str = "/chat/completions"

    @DynamicClassAttribute
    def value(self) -> str:
        return "".join([OpenAIAPIURL._BASE_URL, self._value_])
    

class OpenAIModel(str, Enum):
    GPT_4: str = "gpt-4"
    GPT_3_5_TURBO: str = "gpt-3.5-turbo"


class OpenAIMessageAuthorRole(str, Enum):
    SYSTEM: str = "system"
    USER: str = "user"
    ASSISTANT: str = "assistant"
    FUNCTION: str = "function"
    