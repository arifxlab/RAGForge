from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "RAGForge"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "ragforge"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()