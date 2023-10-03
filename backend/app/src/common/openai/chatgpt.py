from requests import Session, Response

from src.constant import OpenAIAPIURL, OpenAIModel


class ChatGPTAPI:
    def __init__(self, api_key: str) -> None:
        self.session: Session = Session()
        self.session.headers: dict[str, str | bytes] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def create_chat_completion(self) -> str:
        response: Response = self.session.post(
            url=OpenAIAPIURL.CHAT_COMPLETION.value,
            json={
                "model": OpenAIModel.GPT_4.value,
            
            }
        )