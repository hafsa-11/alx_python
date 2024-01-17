#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, database, and state name from command line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = """
        SELECT GROUP_CONCAT(name SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))

    # Fetch the row and print the result
    row = cursor.fetchone()
    if row[0]:
        print(row[0])
    else:
        print("")

    # Close the cursor and database connection
    cursor.close()
    db.close()
