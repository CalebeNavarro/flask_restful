from app.settings.database import session
from sqlalchemy import select
from app.models.users_model import User


class UsersServices:

  @staticmethod
  def get_all_users():
    with session() as s:
      query = s.execute(
        select(User)
      )
      result = query.scalars().all()
    return result
