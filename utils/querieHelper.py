import pyodbc
from config import Config
from decimal import Decimal


class QueriesHelper:
    def getAll(queryString, params=None):
        conn = pyodbc.connect(
            f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes')

        # Create a cursor
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(queryString, params)

        # Fetch the results
        columns = [column[0] for column in cursor.description]

        results = []
        for rows in cursor.fetchall():
            results.append(dict(zip(columns, rows)))

        return results

    def getFirst(queryString, params=None):
        conn = pyodbc.connect(
            f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes')

        # Create a cursor
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(queryString, params)

        # Fetch the results
        columns = [column[0] for column in cursor.description]

        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        cursor.close()
        conn.close()

        return results[0] if len(results) > 0 else None

        """_summary_
        """
    def commandNonQuery(queryString, params=None):
        conn = pyodbc.connect(
            f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes')

        # Create a cursor
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(queryString, params)
        numberOfRowsEffected = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return numberOfRowsEffected
