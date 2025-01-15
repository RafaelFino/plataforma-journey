import psycopg2

class database_conn:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname="registry",
                user="registry",
                password="registry",
                host="localhost",
                port="5432"
            )
            self.cursor = self.conn.cursor()
        except psycopg2.DatabaseError as e:
            print(f"Error {e}")

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.cursor.close()
            print("Database connection closed")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchall()
        except psycopg2.DatabaseError as e:
            print(f"Error {e}")
            return None