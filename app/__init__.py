from flask import Flask, jsonify, request
from app.settings.api import init_app
from app.settings.database import Base, engine, init_db, session
from sqlalchemy import select
from app.models.users_model import User


def create_app():
  app = Flask(__name__)

  # init_db()
  init_app(app)



  def create_user(data):
    with session() as s:
      u = User(**data)
      s.add(u)
      s.commit()
    return u

  # @app.get("/users")
  # def bla():
  #   result = get_all_users()
  #   return jsonify(result)
  #
  # @app.post("/users")
  # def create_users():
  #   data_request = request.json
  #   create_user(data_request)
  #   return data_request

  return app
