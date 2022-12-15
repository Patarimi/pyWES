import typer
import uvicorn
from enum import Enum
import wget
import zipfile
from os import getcwd, remove

cli = typer.Typer()


class CmdList(str, Enum):
    start = "start"
    stop = "stop"


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


@cli.command()
def install_ngspice():
    """
    Install ngspice executable in the correct location.
    """
    ngspice_version = 38
    ngspice_base_url = f"https://sourceforge.net/projects/ngspice/files/ng-spice-rework/{ngspice_version}/"
    ngspice_archive_name = f"ngspice-{ngspice_version}_64.zip"
    base_install = f"{getcwd()}/simulators/"
    wget.download(ngspice_base_url + ngspice_archive_name, base_install)
    with zipfile.ZipFile(base_install + ngspice_archive_name) as zip:
        zip.extractall(base_install)
    remove(base_install + ngspice_archive_name)


def uvicorn_handler(command: CmdList, side: str):
    if command == "start":
        print(f"starting {side} side")
        if side == "server":
            uvicorn.run(
                "pywes.server:Server", host="127.0.0.1", port=5000, log_level="info"
            )
        else:
            uvicorn.run(
                "pywes.client:Client", host="127.0.0.1", port=5050, log_level="info"
            )


if __name__ == "__main__":
    cli()
