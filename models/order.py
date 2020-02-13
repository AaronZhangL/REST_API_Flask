import sqlite3
from models.user import UserModel
from models.purchase_history import PurchaseHistoryModel


class OrderModel:

    def __init__(self, id, date, time, people, firstname, lastname, telnumber):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
	self.people = people
	self.firstname = firstname
	self.lastname = lastname
	self.telnumber = telnumber

    @classmethod
    def find_by_firstname(cls, firstname):
        orders = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT id, date(date), time(time), people, firstname, lastname, telnumber FROM az_example_01 WHERE firstname=?;'
        result = cursor.execute(query, (orders,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                orders.append(OrderModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
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
                orders.append(OrderModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
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


    @classmethod
    def update_datetime_by_telnumber(self, date, time, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'UPDATE az_example_01 SET date=?, time=? where telnumber = ?;'
        result = cursor.execute(query, (date, time, telnumber,))
        connection.commit()
        connection.close()

    @classmethod
    def update_people_by_telnumber(self, people, telnumber):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'UPDATE az_example_01 SET people=? where telnumber = ?;'
        result = cursor.execute(query, (people, telnumber,))
        connection.commit()
        connection.close()


    def json(self):
        return {'id': self.id,
        'date': self.date,
        'time': self.time,
	'people': self.people,
	'firstname': self.firstname,
	'lastname': self.lastname,
	'telnumber': self.telnumber
        }


#class ShoppingStore:

#    # def __init__(id, product, user_id, product_id):
#    #     self.id = id
#    #     self.product = product
#    #     self.user_id = user_id
#    #     self.product_id = product_id

#    @classmethod
#    def buy_product(cls, username, product):
#        user = UserModel.find_by_name(username)
#        if user:
#            products = StoreModel.find_by_product(product)
#            if products:
#                connection = sqlite3.connect('./db/datashop.db')
#                cusrsor = connection.cursor()
#               query = 'INSERT INTO purchase_history VALUES(NULL, ?, ?, ?);'
#                result = cusrsor.execute(query, (product, user.id, products[0].id,))
#                connection.commit()
#                connection.close()
#                return {'message': 'Selected product was bought!'}, 200
#            else:
#                return {'message': 'No product in database!'}, 404
#        else:
#            return {'message': 'Shopping impossible, no user in database!'}, 404
