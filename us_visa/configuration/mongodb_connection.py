import sys
import os

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URI

from pymongo import MongoClient
import certifi

ca = certifi.where()


class MongoDBClient:
    """
    Description: Creates and reuses MongoDB connection (Singleton pattern)
    """

    _client = None   # 👈 class-level variable

    def __init__(self, database_name=DATABASE_NAME):
        try:
            if MongoDBClient._client is None:
                # mongo_db_url = os.getenv(MONGODB_URI)
                mongo_db_url="mongodb+srv://dksanjay39_db_user:F9jALkbPx2awAvC0@cluster0.jnt3sao.mongodb.net/?appName=Cluster0"

                if mongo_db_url is None:
                    raise Exception(f"Environment Key: {MONGODB_URI} is not set.")

                MongoDBClient._client = MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )

                logging.info("MongoDB connection created.")

            self.client = MongoDBClient._client   # ✅ FIX
            self.database = self.client[database_name]
            self.database_name = database_name

            logging.info("MongoDB connection successful.")

        except Exception as e:
            raise USvisaException(e, sys)
