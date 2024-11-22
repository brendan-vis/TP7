import asyncio
import redis.asyncio as redis  # On utilise la version asynchrone de la lib
import uuid  # Pour générer des IDs uniques

async def get_or_create_user(client, username):
    # Vérifiez si l'utilisateur existe déjà
    user_id = await client.hget("users", username)
    
    if user_id:
        # Si l'utilisateur existe, on retourne son ID existant
        return user_id.decode()
    else:
        # Sinon, on génère un nouvel ID pour l'utilisateur
        print(f"{username} est un nouvel utilisateur")
        new_id = str(uuid.uuid4())
        await client.hset("users", username, new_id)  # On ajoute l'utilisateur dans Redis
        return new_id

async def remove_user(client, username):
    user_id = await client.hget("users", username)
    await client.hdel("users", username)
    print(f"Utilisateurs déconnectés")
    print(f"Utilisateur {username} avec ID {user_id.decode()} supprimé.")
    return True

async def main():
    # Connexion au serveur Redis
    client = redis.Redis(host="10.1.1.11", port=6379)

    # Exemple d'utilisateurs
    usernames = ["alice", "bob", "charlie", "alice"]  # Alice apparaît deux fois pour tester

    for username in usernames:
        user_id = await get_or_create_user(client, username)
        print(f"Utilisateur {username} : ID {user_id}\n")

    await remove_user(client, "bob")

    # Fermeture propre de la connexion
    await client.aclose()

if __name__ == "__main__":
    asyncio.run(main())