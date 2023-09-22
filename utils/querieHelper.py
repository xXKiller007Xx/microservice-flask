import pyodbc;
from config import Config;

class QueriesHelper:
    
    @staticmethod
    def getAll(queryString):
        conn = pyodbc.connect(f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes');

            # Create a cursor
        cursor = conn.cursor()



        # Execute the query
        cursor.execute(queryString)

        # Fetch the results
        columns = [column[0] for column in cursor.description]
        
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)));
            
        return results;

    
    def getFirst(queryString):
        conn = pyodbc.connect(f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes');

            # Create a cursor
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(queryString)

        # Fetch the results
        columns = [column[0] for column in cursor.description]
        
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)));
            
        cursor.close()
        conn.close()
        
        return results[0] if len(results) > 0 else None;
    
        """_summary_
        """
    def commandNonQuery(queryString):
        conn = pyodbc.connect(f'Driver={{SQL Server}};Server={Config.server};Database={Config.database};Trust_Connection=yes');

            # Create a cursor
        cursor = conn.cursor()


        # Execute the query
        cursor.execute(queryString)
        numberOfRowsEffected = cursor.rowcount;
        cursor.close()
        conn.close()
        return numberOfRowsEffected

