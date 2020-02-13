from flask import Flask, jsonify
from flask_restful import Api
from resources.user import User, UserList, UserRegister
from resources.store import Store, StoreProductList, Shopping
from resources.purchase_history import PurchaseHistory
from db.database import create_database
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, JWTError

from resources.order import OrderList, Order
from resources.order1 import OrderDate, OrderTelnumber, OrderId

app = Flask(__name__)
api = Api(app)
app.secret_key = 'test'
jwt = JWT(app, authenticate, identity)

api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/product/<string:product>')
api.add_resource(StoreProductList, '/products')
api.add_resource(PurchaseHistory, '/history/<string:name>')
api.add_resource(Shopping, '/shopping')

api.add_resource(OrderList, '/orders')
api.add_resource(Order, '/order/<string:telnumber>')

api.add_resource(OrderId, '/orderid/<string:telnumber>')
api.add_resource(OrderDate, '/orderdate/<string:telnumber>')
api.add_resource(OrderDate, '/orderdate', methods=['GET', 'POST'])
api.add_resource(OrderTelnumber, '/ordertelnumber/<string:telnumber>')


@app.errorhandler(JWTError)
def auth_error_handler(err):
    return jsonify({'message': 'Could not authorize user.'}), 400


if __name__ == '__main__':

    # create_database('./db/datashop.db')
    app.run(debug=True, host='0.0.0.0', port=5000)
