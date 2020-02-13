from models.order import OrderModel
from flask_restful import Resource, reqparse


class Order(Resource):

    def get(self, telnumber):
        orders = OrderModel.find_by_telnumber(telnumber)
        if orders:
            return {'order': [order.json() for order in orders]}, 200
        else:
            return{'message': 'Order not found!'}, 404

    def post(self, date, time, people, firstname, lastname, telnumber):
        order = OrderModel.find_by_telnumber(telnumber)
        if order:
            return {'message': 'Order already in database!'}
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('date',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('time',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('people',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('firstname',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('lastname',
                                type=str,
                                required=True,
                                help='This field is mandatory!')
            parser.add_argument('telnumber',
                                type=str,
                                required=True,
                                help='This field is mandatory!')

            data_payload = parser.parse_args()

            OrderModel.add_order(data_payload['date'], data_payload['time'],
                                 data_payload['people'], data_payload['firstname'],
                                 data_payload['lastname'], data_payload['telnumber'])
            return {'message': 'Order successfully added to database!'}, 201


class OrderList(Resource):

    def get(self):
        orders = OrderModel.find_all_orders()
        if orders:
            return {'orders': [order.json() for order in orders]}, 200
        else:
            return {'message': 'No order found!'}, 404


# class Shopping(Resource):

#    def post(self):
#        parser = reqparse.RequestParser()

#        parser.add_argument('username',
#                            type=str,
#                            required=True,
            #help='This field is mandatory!')

#        parser.add_argument('product',
#                            type=str,
#                            required=True,
#                            help='This field is mandatory!')

#        data_payload = parser.parse_args()

#        return ShoppingStore.buy_product(data_payload['username'],
#                                         data_payload['product'])
