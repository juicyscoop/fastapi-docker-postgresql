-- Create the database
CREATE DATABASE stock_watcher_app;

-- Connect to the newly created database
\c stock_watcher_app;

-- Create the tables
CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL PRIMARY KEY
);

CREATE TABLE portfolio (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);

CREATE TABLE portfoliostock (
    id SERIAL PRIMARY KEY,
    portfolio_id INT NOT NULL,
    stock_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

CREATE TABLE watchlist (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);

CREATE TABLE watchliststock (
    id SERIAL PRIMARY KEY,
    watchlist_id INT NOT NULL,
    stock_id INT NOT NULL,
    FOREIGN KEY (watchlist_id) REFERENCES watchlist(id),
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    portfolio_id INT NOT NULL,
    stock_id INT NOT NULL,
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('buy', 'sell')),
    quantity DECIMAL(10, 2) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE entities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE aapl_daily (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE tsla_daily (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE xom_daily (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    entity_id INT NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entities(id)
);
