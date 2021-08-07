#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    root = sys.argv[1]
    passw = sys.argv[2]
    data = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=root, passwd=passw,
                         db=data, port=3306)

    cursor = db.cursor()

    sql = """SELECT * FROM states
    WHERE name LIKE 'N%' ORDER BY 'states.id';"""

    cursor.execute(sql)

    result = cursor.fetchall()

    for x in result:
        print(x)

    cursor.close()
    db.close()
