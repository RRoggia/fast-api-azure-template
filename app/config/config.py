from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    pg_username: str
    pg_password: str

    model_config = SettingsConfigDict(env_file=".env")
