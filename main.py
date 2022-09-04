import typer
import uvicorn

cli = typer.Typer()


@cli.command()
def server(command: str):
    uvicorn_handler(command, "server")


@cli.command()
def client(command: str):
    uvicorn_handler(command, "client")


def uvicorn_handler(command, side: str):
    if command == "start":
        print(f"starting {side} side")
        if side == "server":
            uvicorn.run("server:Server", host="127.0.0.1", port=5000, log_level="info")
        else:
            uvicorn.run("client:Client", host="127.0.0.1", port=5050, log_level="info")


if __name__ == "__main__":
    cli()
