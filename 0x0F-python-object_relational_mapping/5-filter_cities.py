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
    name_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=root, passwd=passw,
                         db=data, port=3306)

    cursor = db.cursor()

    sql = """SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE %s
    ORDER BY 'cities.id' ASC;"""

    cursor.execute(sql, (name_state,))

    result = cursor.fetchall()

    for x in range(len(result)):
        if x == len(result) - 1:
            print("{}".format(result[x][0]), end="")
        else:
            print("{}, ".format(result[x][0]), end="")

    print()
    cursor.close()
    db.close()
