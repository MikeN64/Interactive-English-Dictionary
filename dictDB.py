import mysql.connector
import config

conn = mysql.connector.connect(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    database=config.DATABASE
)

cursor = conn.cursor()

def get_definitions(word):
    cursor.execute("Select Definition FROM Dictionary WHERE Expression='{}'".format(word))
    results = cursor.fetchall()
    definitions = [result[0] for result in results]
    return definitions

def get_all_words():
    cursor.execute("Select Expression FROM Dictionary")
    results = cursor.fetchall()
    words = [result[0] for result in results]
    return words