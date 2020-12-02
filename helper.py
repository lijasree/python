import mysql.connector
from mysql.connector import Error


def add_to_list(content):
    try:
        connection = mysql.connector.connect(
            host='localhost', database='tasks', user='logiuser', password='logipass')

        cursor = connection.cursor()
        query = f"insert into tasks (content, completed) values ('{content}',0)"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        return {"status": 'OK', "message": 'inserted successfully'}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        connection = mysql.connector.connect(
            host='localhost', database='tasks', user='logiuser', password='logipass')

        cursor = connection.cursor()
        query = "select * from tasks"
        cursor.execute(query)
        records = cursor.fetchall()
        return {"tasks": records, "structure": ["id", "content", "completed"]}
        connection.close()
        cursor.close()

    except Exception as e:
        print('Error: ', e)
        return None
