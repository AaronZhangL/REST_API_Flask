import sqlite3
import json


class Order1Model:

    def __init__(self, id, date, time, people, firstname, lastname, telnumber):
        self.id = id
        self.date = date
        self.time = time
        self.people = people
        self.firstname = firstname
        self.lastname = lastname
        self.telnumber = telnumber

    @classmethod
    def find_by_telnumber(cls, telnumber):
        orders = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT id, date(date), time(time), people, firstname, lastname, telnumber FROM az_example_01 WHERE telnumber=?;'
        result = cursor.execute(query, (telnumber,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                orders.append(Order1Model(
                    row[0], row[1], row[2], row[3], str(row[4]), str(row[5]), row[6]))
            return orders
        connection.close()

    @classmethod
    def find_all_orders(cls):
        orders = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT id, date(date), time(time), people, firstname, lastname, telnumber FROM az_example_01;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                orders.append(Order1Model(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            return orders
        connection.close()

    @classmethod
    def add_order_by_fullname(self, firstname, lastname):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO az_example_01 (firstname, lastname) VALUES(?,?);'
        result = cursor.execute(query, (firstname, lastname,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Insert Date
    ###################
    @classmethod
    def add_date_by_telnumber(self, date, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO az_example_01 (date, telnumber) VALUES(?,?);'
        result = cursor.execute(
            query, (date, telnumber,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Insert Time
    ###################
    @classmethod
    def add_time_by_telnumber(self, time, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO az_example_01 (time, telnumber) VALUES(?,?);'
        result = cursor.execute(
            query, (time, telnumber,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Insert People
    ###################
    @classmethod
    def add_people_by_telnumber(self, people, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO az_example_01 (people, telnumber) VALUES(?,?);'
        result = cursor.execute(
            query, (people, telnumber,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Update Date
    ###################
    @classmethod
    def update_date_by_telnumber(self, date, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'UPDATE az_example_01 SET date=? where telnumber = ?;'
        result = cursor.execute(query, (date, telnumber,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Update Time
    ###################
    @classmethod
    def update_time_by_telnumber(self, time, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'UPDATE az_example_01 SET time=? where telnumber = ?;'
        result = cursor.execute(query, (time, telnumber,))
        connection.commit()
        connection.close()
        return result

    ###################
    # Update People
    ###################
    @classmethod
    def update_people_by_telnumber(self, people, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'UPDATE az_example_01 SET people=? where telnumber = ?;'
        result = cursor.execute(query, (people, telnumber,))
        connection.commit()
        connection.close()
        return result

    def json(self):
        return {'id': self.id,
                'date': self.date,
                'time': self.time,
                'people': self.people,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'telnumber': self.telnumber
                }

    def getId(self):
        return self.id

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getPeople(self):
        return self.people

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getTelnumber(self):
        return self.telnumber
