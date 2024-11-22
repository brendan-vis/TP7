import asyncio
import websockets
import aioconsole

async def async_input(websocket):
    while True:
        # Lire un message de l'utilisateur et l'envoyer via WebSocket
        msg = await aioconsole.ainput("Entrez un message : ")
        await websocket.send(msg)

async def async_receive(websocket):
    while True:
        # Recevoir un message du serveur WebSocket
        try:
            data = await websocket.recv()
            if data:
                print(f"Message reçu : {data}")
        except websockets.ConnectionClosed:
            print("Connexion fermée par le serveur.")
            break

async def main():
    uri = "ws://localhost:8765"  # Remplacez par votre URI WebSocket
    async with websockets.connect(uri) as websocket:
        # Exécuter en parallèle les tâches d'envoi et de réception
        tasks = [async_input(websocket), async_receive(websocket)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
