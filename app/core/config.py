from pydantic_settings import BaseSettings
from pydantic import validator
import os
from typing import Optional, List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Task Management API"
    DEBUG: bool = False
    
    # Database settings (for future expansion)
    DATABASE_URL: Optional[str] = None
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Allow extra fields in environment variables


settings = Settings() 