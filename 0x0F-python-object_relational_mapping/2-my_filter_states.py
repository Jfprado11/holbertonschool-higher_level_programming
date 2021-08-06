#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    root = sys.argv[1]
    passw = sys.argv[2]
    data = sys.argv[3]
    name_search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=root, passwd=passw,
                         db=data, port=3306)

    cursor = db.cursor()

    sql = """SELECT * FROM states
    WHERE name LIKE '{}' ORDER BY 'states.id' ASC""".format(name_search)

    cursor.execute(sql)

    result = cursor.fetchall()

    for x in result:
        print(x)

    cursor.close()
    db.close()
