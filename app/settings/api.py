from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
  api = Api(app)

  from app.views.users_view import Users
  api.add_resource(Users, "/api/v1/users")

