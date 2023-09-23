import os
from enum import Enum

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # uvicorn
    reload: bool = True
    workers: int = 1
    port: int = 8000
    log_level: str = "DEBUG"

    class Config:
        env_prefix = "TRP_"


# settings instance
settings = Settings()


# loguru settings
# fmt = "{time:YYYY-MM-DD HH:mm:ss.SSS zz} <lvl>[{level}]</lvl> {name}:{line} <lvl>{message}</lvl>"
# logger.remove()
# logger.add(sys.stdout, level=settings.log_level, colorize=True, format=fmt)
# logger.debug(f"{env} settings loaded.")
