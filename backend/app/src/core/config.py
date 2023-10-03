from functools import lru_cache

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    pass


class NCPSettings(BaseSettings):
    pass


class OpenAISettings(BaseSettings):
    pass


class ApplicationSettings(DatabaseSettings, NCPSettings, OpenAISettings):
    pass


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
