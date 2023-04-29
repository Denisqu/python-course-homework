from abc import ABC, abstractmethod

class LoginNotFound(Exception):
    pass

class LengthError(Exception):
    pass
class Authorizator(ABC):
    @abstractmethod
    def login(self, login, pswd):
        pass

    @abstractmethod
    def check_password(self, login, pswd):
        pass

    @abstractmethod
    def check_login(self, login):
        pass

class UserAuthorizator(Authorizator):
    database = {}
    def login(self, login, pswd):
        if self.check_login(login) and self.check_password(login, pswd):
            print("Доступ разрешен!")

    def check_password(self, login, pswd):
        if len(pswd) < 8:
            raise LengthError()
        if self.database[login] == pswd:
            return True

    def check_login(self, login):
        if self.database.get(login, None) is None:
            raise LoginNotFound()
        else:
            return True

authorizator = UserAuthorizator()
authorizator.database["user"] = "password"
authorizator.database["admin"] = "admin_password"

login = input("login: ")
pswd = input("password: ")
authorizator.login(login, pswd)