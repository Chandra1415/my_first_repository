import pyodbc
import json
import pandas as pd

# Load the configuration from the JSON file
with open("sqlex.json") as config:
    var1 = json.load(config)

def sql_Pull():
    # Construct the connection string
    connect_str = (f"Driver={var1['sql']['Driver']};"
                   f"Server={var1['sql']['Server']};"
                   f"Database={var1['sql']['Database']};"
                   f"UID={var1['sql']['Username']};"
                   f"PWD={var1['sql']['Password']};")
    try:
        # Establish the connection to the SQL server
        connection = pyodbc.connect(connect_str)
        print("Connection successful")
        return connection
    except pyodbc.Error as e:
        # Handle connection errors
        print(f"Error connecting to SQL Server: {e}")
        return None

"""def close_connection(connection):
        Closes the database connection.
            if connection:
                try:
                    connection.close()
                    print("Connection closed successfully.")
                except pyodbc.Error as e:
                    print(f"Error closing connection: {e}")
"""

def fetchdata(query):
    # Pull data from SQL
    connection = sql_Pull()

    if connection is not None:
        # Do something with the connection (e.g., querying)
        #cursor = connection.cursor()

        try:
            result= pd.read_sql_query(query,connection)
            print("data fetching is successful")
            return result
        except Exception as e:
            print("error while running the query",e)
            return None
        finally:
            connection.close()
            print("connection closed sucessfully")



if __name__ == "__main__":
    query = "select * from dbo.student"
    data = fetchdata(query)
    if data is not None:
        print(data)