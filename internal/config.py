from dotenv import load_dotenv
import os

from pydantic import SecretStr


class Config:
    def __init__(self, db_url: str, yookassa_base_url: str, shop_id: str, secret_key: SecretStr):
        self.db_url = db_url
        self.yookassa_base_url=yookassa_base_url
        self.shop_id = shop_id
        self.secret_key = secret_key

def load_config() -> Config:
    load_dotenv()
    return Config(os.getenv("DB_URL"), os.getenv("YOOKASSA_BASE_URL"), os.getenv("YOOKASSA_SHOP_ID"), SecretStr(os.getenv("YOOKASSA_SECRET_KEY")))