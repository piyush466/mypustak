import configparser

config = configparser.RawConfigParser()
config.read("/Users/user/Documents/Projects/test/Logs/pytest.ini")

class Read_proeprties:

    @staticmethod
    def user_email():
        enter_user_email = config.get("user inputs","user_email")
        return enter_user_email

    @staticmethod
    def user_password():
        enter_user_password = config.get("user inputs", "password")
        return enter_user_password


