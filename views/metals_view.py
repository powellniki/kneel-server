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