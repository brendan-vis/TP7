import asyncio
import websockets

CLIENTS = set()  # Ensemble des connexions WebSocket

async def handle_client(websocket):
    # Ajouter le nouveau client à l'ensemble
    CLIENTS.add(websocket)
    client_addr = websocket.remote_address
    print(f"{client_addr} connecté.")

    try:
        async for message in websocket:
            print(f"{client_addr} : {message}")

            # Diffuser le message à tous les autres clients
            for client in CLIENTS:
                if client != websocket:
                    await client.send(f"{client_addr} : {message}")
    except websockets.ConnectionClosed:
        print(f"{client_addr} s'est déconnecté.")
    finally:
        # Nettoyer après la déconnexion
        CLIENTS.remove(websocket)
        print(f"{client_addr} a été retiré de CLIENTS.")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print(f"Serveur WebSocket en écoute sur ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
