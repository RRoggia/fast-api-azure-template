from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    pg_username: str
    pg_password: str
    cors: List[str]
    comp_api_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
