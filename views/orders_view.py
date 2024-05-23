import sqlite3
import json


def get_all_orders():
    #open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM orders o
        """)
        query_results = db_cursor.fetchall()

        #initialize an empty list and then add each order to that list as a dictionary
        orders = []
        for row in query_results:
            orders.append(dict(row))

        #serialized Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders


def get_single_order(url):
    #open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM orders o
        WHERE o.id == ?
        """, (url['pk'],))

        query_results = db_cursor.fetchone()
        order_dictionary = dict(query_results)

        #serialized Python list to JSON encoded string
        serialized_order = json.dumps(order_dictionary)
        
    return serialized_order


def create_order(order_data):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO orders
            (metal_id, size_id, style_id)
            VALUES (?, ?, ?)
            """,
            (order_data['metal_id'], order_data['size_id'], order_data['style_id'])
        )

        rows_created = db_cursor.rowcount

    return True if rows_created > 0 else False


def delete_order(pk):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM orders WHERE id = ?
        """, (pk,)
        )

        rows_deleted = db_cursor.rowcount
    
    return True if rows_deleted > 0 else False


def update_order(pk, order_data):
    with sqlite3.connect('./kneeldiamonds.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            UPDATE orders
                SET
                    metal_id = ?,
                    size_id = ?,
                    style_id = ?
            WHERE id = ?
        """, (order_data['metal_id'], order_data['size_id'], order_data['style_id'], pk)
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False