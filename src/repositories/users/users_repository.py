from src.domain.models.users import UsersModel
from src.infrastructure.mysql.mysql_infrastructure import MySQLInfrastructure


class UsersRepository:
    @staticmethod
    def insert_user(name: str):
        with MySQLInfrastructure() as db:
            user = UsersModel(name=name)
            db.session.add(user)
            db.session.commit()
