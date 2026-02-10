import sqlite3
import os

import logging


DATABASE_PATH = os.getenv("DATABASE_PATH", "data/shortener.db")

logger = logging.getLogger(__name__)

def get_conn():
    path = os.getenv("DATABASE_PATH", DATABASE_PATH)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            code TEXT UNIQUE PRIMARY KEY,
            url TEXT NOT NULL
        );
    """)
    conn.close()
    logger.info("DB initialized at %s", os.getenv("DATABASE_PATH", DATABASE_PATH))

def create_row(url: str, code: str) -> None:
    conn = get_conn()
    with conn:
        cur = conn.execute("INSERT INTO urls (url, code) VALUES (?, ?);", (url, code))
    conn.close()

def get_by_code(code: str) -> sqlite3.Row:
    conn = get_conn()
    cur = conn.execute("SELECT code, url FROM urls WHERE code = ?;", (code,))
    row = cur.fetchone()
    conn.close()
    return row
