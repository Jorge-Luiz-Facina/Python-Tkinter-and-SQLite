import sqlite3
connection = sqlite3.connect('DataBase\infos.db')
cursor = connection.cursor()

TABLE_NAME = "info"
COLUMN_NAME = "name"
COLUMN_DESCRIPTION = "description"

class BankController:

    def __init__(self):
        global connection
        global cursor
        connection = sqlite3.connect('infos.db')
        cursor = connection.cursor()
        self.create_database()

    def create_database(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" + COLUMN_NAME + " text, " + COLUMN_DESCRIPTION + " text)")
        connection.commit()

    def insert(self, name, description):
        cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES(?,?)", (name, description))
        connection.commit()

    def update(self, name, description):
        cursor.execute("UPDATE info SET " + COLUMN_DESCRIPTION + " = ? WHERE " + COLUMN_NAME + " = ? ", (description, name))
        connection.commit()

    def delete(self, name):
        cursor.execute("DELETE FROM " + TABLE_NAME + " WHERE " + COLUMN_NAME + " = ?", (name,))
        connection.commit()

    def getNames(self):
        sql = "SELECT * FROM " + TABLE_NAME
        listNames = []
        try:
            for row in cursor.execute(sql):
                listNames.insert(0, row[0])
        except:
           listNames.insert(0, "void")
        return listNames

    def getDescription(self, name):
        description = ""
        sql = "SELECT * FROM " + TABLE_NAME + " WHERE " + COLUMN_NAME + " = ?"
        for row in cursor.execute(sql, (name,)):
            description = row[1]
        return description

    def close(self):
        cursor.close()
        connection.close()