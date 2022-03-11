from flask_restful import Resource
from app.services.users_service import UsersServices
from flask import jsonify


class Users(Resource):
  def get(self):
    result = UsersServices.get_all_users()
    print(result)
    return jsonify(result)
