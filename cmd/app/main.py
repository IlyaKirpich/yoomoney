import uvicorn
from fastapi import FastAPI

from internal.app.clients.http_yookassa import HTTPYookassaClient
from internal.app.handlers.http_handler import HTTPHandler
from internal.app.repositories.sql_orders import PostgresOrdersRepository
from internal.app.usecases.payments import PaymentUseCase
from internal.config import load_config

app = FastAPI()

if __name__ == '__main__':
    cfg = load_config()

    use_case = PaymentUseCase(
        PostgresOrdersRepository(cfg.db_url),
        HTTPYookassaClient(cfg.yookassa_base_url, cfg.shop_id, cfg.secret_key))

    handler = HTTPHandler(use_case)
    app.include_router(handler.router)
    uvicorn.run(app, port=8000, host="0.0.0.0")
