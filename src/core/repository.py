import sqlite3
from core.credentials import getDatabaseName

# Verificar necessidade de outros campos


def userMigration(cursor):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users (id numeric PRIMARY KEY UNIQUE, nick text)''')

# Verificar necessidade de outros campos


def adminMigration(cursor):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS admins (id numeric PRIMARY KEY UNIQUE, nick text)''')


migrationsList = [userMigration, adminMigration]


class PrivateRepository:
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect(getDatabaseName())
        self.cursor = self.connection.cursor()
        for migration in migrationsList:
            migration(self.cursor)
        self.connection.commit()

    def getCursor(self):
        return self.cursor

    def queryOne(self, query, parameter):
        cursor = self.getCursor()
        cursor.execute(query, id)
        return cursor.fetchone()

    def queryAll(self, query):
        cursor = self.getCursor()
        cursor.execute(query)
        return cursor.fetchall()

    def findUser(self, id):
        return self.queryOne("SELECT * FROM users WHERE id=?", id)

    def findUserByNick(self, nick):
        return self.queryOne("SELECT * FROM users WHERE nick=?", id)

    def findAdmin(self, id):
        return self.queryOne("SELECT * FROM admins WHERE id=?", id)

    def findAdminByNick(self, nick):
        return self.queryOne("SELECT * FROM admins WHERE nick=?", id)

    def findAllAdmins(self):
        return self.queryAll("SELECT * FROM admins")

    def newAdmin(self, id, nick):
        cursor = self.getCursor()
        cursor.execute(
            """INSERT INTO admins (id, nick) VALUES(?,?);""", (id, nick))
        self.connection.commit()


Repository = PrivateRepository()
