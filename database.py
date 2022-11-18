import sqlite3
connection = sqlite3.connect('parkinglot.db')
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS userInfo(Userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
          "username VARCHAR(10) UNIQUE NOT NULL,"
          "phonenum VARCHAR(10) NOT NULL,"
          "Password VARCHAR(10) NOT NULL)")
connection.commit()


c.execute("CREATE TABLE IF NOT EXISTS booking( bookingId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
    "username VARCHAR(10) NOT NULL,"
    "Day text NOT NULL,"
    "endTime text NOT NULL,"
    "StartTime text NOT NULL,"
    "DURATION float NOT NULL,"
    "fee INTEGER NOT NULL,"
    "spotID INTEGER NOT NULL,"
    "qrid text not null UNIQUE)")
connection.commit()