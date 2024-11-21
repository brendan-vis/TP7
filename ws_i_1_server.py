# from https://websockets.readthedocs.io/en/stable/howto/quickstart.html
import asyncio
import websockets

async def hello(websocket):
    msg = await websocket.recv()
    print(f"<<< {msg}")
    greeting = f"Hello client ! Received '{msg}'"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())