#!/usr/bin/python3
"""
A simple Python script to create the MySQL database 'alx_book_store'
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure the connection is properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
