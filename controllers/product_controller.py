from flask_restx import Namespace, Resource, reqparse
from flask import request
from utils.querieHelper import QueriesHelper
import uuid

product_namespace = Namespace('products', description='Product api')
parser = reqparse.RequestParser()


@product_namespace.route('/')
class Products(Resource):
    def get(self):
        try:
            return QueriesHelper.getAll(f"""SELECT Id, ProductName, [Description], 
                                        CONVERT(varchar(20),Price,1) AS 'Price', 
                                        Banner,Manufacture,Publisher,PublishedDate,Genre FROM Products""")
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500

    def post(self):
        try:
            content_type = request.headers.get('Content-Type')
            if (content_type == "application/json"):
                json = request.json
                # parse data
                query = f"""INSERT INTO Products VALUES (NEWID(),N'{json['ProductName']}'
                ,N'{json['Description']}'
                ,{json['Price']},N'{json['Banner']}',N'{json['Manufacture']}'
                ,N'{json['Publisher']}','{json['PublishedDate']}',N'{json['Genre']}')"""
                return QueriesHelper.commandNonQuery(query), 201
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500


@product_namespace.route("/product-detail")
class ProductDetail(Resource):
    @product_namespace.doc(params={'pid': {'description': 'ProductId', 'type': 'Guid', 'default': str(uuid.uuid4())}})
    def get(self):
        try:
            id = request.args.get("pid")
            if (id == "" or id is None):
                return {
                    "Msg": "Missing product id"
                }, 401
            return QueriesHelper.getFirst(f"SELECT Id, ProductName, [Description], CONVERT(varchar(20),Price,1) AS 'Price', Banner,Manufacture,Publisher,PublishedDate,Genre FROM Products WHERE Id = '{id}'")
        except Exception as ex:
            return {
                "Msg": str(ex)
            }, 500
