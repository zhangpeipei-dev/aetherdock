from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AetherDock"
    APP_ENV: str = "dev"

    DB_URL: str = "sqlite:///./aetherdock.db"

    JWT_SECRET: str = "aetherdock"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()