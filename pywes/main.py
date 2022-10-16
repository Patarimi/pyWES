import typer
import uvicorn
from enum import Enum

cli = typer.Typer()


class CmdList(str, Enum):
    start = 'start'
    stop = 'stop'


@cli.command()
def server(command: CmdList):
    """
    Control the simulation server.
    """
    uvicorn_handler(command, "server")


@cli.command()
def client(command: CmdList):
    """
    Control the simulation client.
    """
    uvicorn_handler(command, "client")


def uvicorn_handler(command: CmdList, side: str):
    if command == "start":
        print(f"starting {side} side")
        if side == "server":
            uvicorn.run("pywes.server:Server", host="127.0.0.1", port=5000, log_level="info")
        else:
            uvicorn.run("pywes.client:Client", host="127.0.0.1", port=5050, log_level="info")


if __name__ == "__main__":
    cli()
