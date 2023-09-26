from flask_restx import Namespace, Resource, reqparse
from flask import request
from utils.querieHelper import QueriesHelper
import uuid

cart_namespace = Namespace('carts', description='Cart api')
parser = reqparse.RequestParser()


@cart_namespace.route("/")
class Carts(Resource):
    @cart_namespace.doc(params={'uid': {'description': 'UserId', 'type': 'Guid', 'default': str(uuid.uuid4())}})
    def get(self):
        try:
            uid = request.args.get("uid") or ""
            return QueriesHelper.getAll(f"""
                                          SELECT P.ProductName, CONVERT(varchar(20),P.Price,1) AS 'Price' FROM Carts C INNER JOIN CartItems CI ON C.Id = CI.CartId
                    INNER JOIN Users u ON c.UserID = u.Id
                    INNER JOIN Products p on CI.ProductId = p.Id
                    WHERE U.Id = '{uid}'
                                        """)
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500

    @cart_namespace.doc(params={'cid': {'description': 'cart id', 'type': 'Guid', 'default': str(uuid.uuid4())},
                                'pid': {'description': 'product id', 'type': 'Guid', 'default': str(uuid.uuid4())}})
    def delete(self):
        try:
            cartId = request.args.get("cid") or ""
            productId = request.args.get("pid") or ""
            return QueriesHelper.commandNonQuery(f"""
                                                 DELETE from CartItems WHERE CartId = ? 
                                                                        AND ProductId = ?
                                                 """, (cartId, productId))
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
