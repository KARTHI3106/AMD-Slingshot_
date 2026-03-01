from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = ""

    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.1-pro"

    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:8b"

    sqlite_db_path: str = str(Path(__file__).parent / "data" / "skillgraph.db")
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"
    demo_api_key: str = "skillgraph-demo"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
