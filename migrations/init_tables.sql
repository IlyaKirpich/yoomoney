CREATE TABLE IF NOT EXISTS orders (
    id SERIAL NOT NULL PRIMARY KEY,
    order_id VARCHAR(255) NOT NULL,
    yookassa_id VARCHAR(255),
    amount INT NOT NULL,
    description TEXT NOT NULL,
    is_paid BOOL NOT NULL DEFAULT False,
    payment_method_id VARCHAR(255)
);