import os

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()


def dbConnection():
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("Configura MONGO_URI en el entorno o en un archivo .env")

    client = MongoClient(
        mongo_uri,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=10000,
    )

    try:
        client.admin.command("ping")
    except PyMongoError:
        client.close()
        raise

    print("CONEXIÓN EXITOSA CON LA BDD")
    return client["dbb_products_app"]