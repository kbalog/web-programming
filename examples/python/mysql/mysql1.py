"""
Example MySQL usage using MySQL Connector/Python

https://dev.mysql.com/doc/connector-python/en/
"""

import mysql.connector
from mysql.connector import errorcode


def drop_table(conn):
    """Drop table."""
    cur = conn.cursor()
    try:
        sql = "DROP TABLE postcodes"
        cur.execute(sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_TABLE_ERROR:
            print("Error: Table does not exist.")
        else:
            print("Error: {}".format(err.msg))
    else:
        print("Table dropped.")
    finally:
        cur.close()


def create_table(conn):
    """Create table."""
    cur = conn.cursor()
    try:
        sql = ("CREATE TABLE postcodes ("
               "postcode VARCHAR(4), "
               "location VARCHAR(20), "
               "PRIMARY KEY(postcode))")
        cur.execute(sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Error: Table already exists.")
        else:
            print("Error: {}".format(err.msg))
    else:
        print("Table created.")
    finally:
        cur.close()


def insert_data(conn):
    """Insert data to a table."""
    postcodes = {
        "0001": "Oslo",
        "4036": "Stavanger",
        "4041": "Hafrsfjord",
        "7491": "Trondheim",
        "9019": "Tromsø"
    }
    cur = conn.cursor()
    num = 0
    for k, v in postcodes.items():
        sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
        try:
            cur.execute(sql, (k, v))  # data is provided as a tuple
            conn.commit()  # commit after each row
        except mysql.connector.Error as err:
            print("Error: {}".format(err.msg))
        else:
            num += 1
    print("{:d} rows inserted.".format(num))
    cur.close()


def query_data(conn):
    """Querying data."""
    cur = conn.cursor()
    try:
        sql = ("SELECT postcode, location FROM postcodes "
               "WHERE postcode BETWEEN %s AND %s")
        cur.execute(sql, ("4000", "5000"))
        for (postcode, location) in cur:
            print("{}: {}".format(postcode, location))
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
    finally:
        cur.close()


if __name__ == "__main__":

    try:
        conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='dat310')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username/password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
    else:
        # drop_table(conn)
        create_table(conn)
        insert_data(conn)
        query_data(conn)
        conn.close()
