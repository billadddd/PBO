import sqlite3
import pandas as pd

from konfigurasi import DB_PATH


def get_db_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def execute_query(query, params=None):

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()

        return cursor.lastrowid

    except sqlite3.Error as e:

        print("Error:", e)

        conn.rollback()

        return None

    finally:

        conn.close()


def fetch_query(query, params=None, fetch_all=True):

    conn = get_db_connection()

    cursor = conn.cursor()

    try:

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()

        return result

    except sqlite3.Error as e:

        print("Error:", e)

        return None

    finally:

        conn.close()


def get_dataframe(query, params=None):

    conn = get_db_connection()

    try:

        df = pd.read_sql_query(
            query,
            conn,
            params=params
        )

        return df

    except Exception as e:

        print("Error:", e)

        return pd.DataFrame()

    finally:

        conn.close()