from requests import Session, Response

from src.constant import NCPAPIURL


class ClovaVoiceAPI:
    def __init__(self) -> None:
        self.session: Session = Session()
        self.session.headers: dict[str, str | bytes] = {
            "Content-Type": "",

        }

    def transform(self) -> None:
        pass
