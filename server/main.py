import asyncio
import os


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def _main(host: str, port: int, callback: object) -> None:
    server = await asyncio.start_server(
        callback, host, port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)

    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


def main():
    from client.model import HOST, PORT

    asyncio.run(_main(
        host=HOST,
        port=os.environ.get('PORT', PORT),
        callback=handle_echo
    ),
        debug=True)


if __name__ == '__main__':
    # or python -m server.main
    main()
