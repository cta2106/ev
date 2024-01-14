import sqlite3
from typing import Optional

from constants import DB_NAME


def create_database(db_name: str = DB_NAME) -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY,
            street TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            country TEXT NOT NULL,
            email_consent BOOLEAN NOT NULL,
            concerns TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def read_all_customers(db_name: str = DB_NAME) -> Optional[str]:
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers")

        all_rows = cursor.fetchall()

        for row in all_rows:
            print(row)

        conn.close()
    except Exception:
        return "Table does not exist"
