from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, fullname="",rol="") -> None:
        self.id = id
        self.username = username

        self.password = password
        self.fullname = fullname
        self.rol=rol
        print('imprimir role')
        print(self.rol)
        

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
