import sqlite3
import json


def get_all_orders(url):
    #open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    if url['query_params']:
        db_cursor.execute("""
            SELECT
                o.id AS order_id,
                o.metal_id AS metal_order_id,
                o.size_id AS size_order_id,
                o.style_id AS style_order_id,
                m.id AS metal_id,
                m.metal AS metal_name,
                m.price AS metal_price,
                s.id AS size_id,
                s.carets AS size_caret,
                s.price AS size_price,
                t.id AS style_id,
                t.style AS style_style,
                t.price AS style_price
            FROM orders o
            JOIN metals m ON m.id = o.metal_id
            JOIN sizes s ON s.id = o.size_id
            JOIN styles t ON t.id = o.style_id
        """)
        query_results = db_cursor.fetchall()

        orders=[]
        for row in query_results:
            metal = {
                "id": row['metal_id'],
                "metal": row['metal_name'],
                "price": row['metal_price']
            }
            size = {
                "id": row['size_id'],
                "carets": row['size_caret'],
                "price": row['size_price']
            }
            style = {
                "id": row['style_id'],
                "style": row['style_style'],
                "price": row['style_price']
            }
            order = {
                "id": row['order_id'],
                "metal_id": row['metal_order_id'],
                "metal": metal,
                "size_id": row['size_order_id'],
                "size": size,
                "style_id": row['style_order_id'],
                "style": style
            }
            orders.append(order)
        serialized_orders = json.dumps(orders)
        return serialized_orders


    else:
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
        """, (order_data['metal_id'], order_data['size_id'], order_data['style_id'], pk))

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False