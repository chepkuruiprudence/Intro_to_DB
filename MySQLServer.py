#!/usr/bin/python3
"""
Script that creates the database alx_book_store in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # <-- Replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection properly
    if connection.is_connected():
        cursor.close()
        connection.close()
