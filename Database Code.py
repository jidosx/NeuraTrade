import mysql.connector

class Database:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.cnx = mysql.connector.connect(
      user=self.user,
      password=self.password,
      host=self.host,
      database=self.database
    )

  def retrieve_data(self, query):
    # Retrieve data from database
    cursor = self.cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

  def store_data(self, query, data):
    # Store data in database
    cursor = self.cnx.cursor()
    cursor.execute(query, data)
    self.cnx.commit()
