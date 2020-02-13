from models.order1 import Order1Model
from flask_restful import Resource, reqparse
from flask import Flask
app = Flask(__name__)


class OrderDate(Resource):
    '''
    Insert/Update Date column
    '''

    def get(self, telnumber):
        orders = Order1Model.find_by_telnumber(telnumber)
        if orders:
            return orders[0].getDate(), 200
        else:
            return{'message': 'Order not found!'}, 404

    def post(self, date, telnumber):
        order = Order1Model.find_by_telnumber(telnumber)
        if order:
            return {'message': 'Order already in database!'}
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('date',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('telnumber',
                                type=str,
                                required=True,
                                help='This field is mandatory!')

            data_payload = parser.parse_args()

            Order1Model.add_date_by_telnumber(
                data_payload['date'], data_payload['telnumber'])
            return {'message': 'Order successfully added to database!'}, 201


class OrderTelnumber(Resource):
    '''
    Insert/Update Telnumber column
    '''

    def get(self, telnumber):
        orders = Order1Model.find_by_telnumber(telnumber)
        if orders:
            return orders[0].getTelnumber(), 200
        else:
            return{'message': 'Order not found!'}, 404

    def post(self, telnumber):
        order = Order1Model.find_by_telnumber(telnumber)
        if order:
            return {'message': 'Order already in database!'}
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('telnumber',
                                type=str,
                                required=True,
                                help='This field is mandatory!')

            data_payload = parser.parse_args()

            Order1Model.add_date_by_telnumber(data_payload['telnumber'])
            return {'message': 'Order successfully added to database!'}, 201


class OrderList(Resource):

    def get(self):
        orders = Order1Model.find_all_orders()
        app.logger.debug("--AZ-001--")
        app.logger.debug(orders)
        if orders:
            return {'orders': [order.json() for order in orders]}, 200
        else:
            return {'message': 'No order found!'}, 404
