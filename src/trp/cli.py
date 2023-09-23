import typer
import uvicorn
from pydantic import ValidationError
from tabulate import tabulate

from . import __version__
from .config import settings


app = typer.Typer(help="Test ReactPy Commands")


@app.command("server")
def run_server(
    host: str = "0.0.0.0",
    port: int = settings.port,
    workers: int = settings.workers,
    reload: bool = settings.reload,
    log_level: str = settings.log_level.lower(),
):
    config = uvicorn.Config(
        "trp.main:app",
        host=host,
        port=port,
        workers=workers,
        reload=reload,
        log_level=log_level,
    )
    print(config.__dict__)
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    app()
