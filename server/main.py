import asyncio
import os

from client.model import HOST
from client.model import PORT


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


async def main(host: str, port: int, callback: object) -> None:
    server = await asyncio.start_server(
        callback, host, port)

    reader, writer = await asyncio.open_connection(
        HOST, PORT)
    callback(reader, writer)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)

    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main(
        host=HOST,
        port=os.environ.get('PORT', PORT),
        callback=handle_echo
    ))
