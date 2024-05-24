import sqlite3
import json

def get_all_metals():
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                id,
                metal,
                price
            FROM metals
        """)

        query_results = db_cursor.fetchall()

        metals = []
        for row in query_results:
            metals.append(dict(row))
        
        serialized_metals = json.dumps(metals)
    
    return serialized_metals


def get_single_metal(url):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                id,
                metal,
                price
            FROM metals
            WHERE id = ?
        """, (url['pk'],))

        query_results = db_cursor.fetchone()
        metal_dictionary = dict(query_results)

        serialized_metal = json.dumps(metal_dictionary)

    return serialized_metal


def update_metal(pk, metal_data):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE metals
                SET
                    metal = ?,
                    price = ?
            WHERE id = ?
        """, (metal_data['metal'], metal_data['price'], pk))
        
        rows_affected = db_cursor.rowcount
        
    return True if rows_affected > 0 else False