from config import *
# TODO
# Add logging class to allow for easy switchout of logging modes.

class Logger:

    def __init__(self):
        self.level = LOGGING_LEVEL
        self.messages = {
            'NCS': {
                'INFO': "",
                "ERROR": "No CONNECTOR_TYPE is set in the config\n"
            },
            'NAE': {
                'INFO': "",
                'ERROR': "Account does not exist\n"
            },
            'AAE': {
                'INFO': "",
                'ERROR': "This account name/number already exists\n"
            },
            'SAL': {
                'INFO': "",
                'ERROR': "Not updating due to surpassing account limit\n"
            },
            'NBRCH': {
                'INFO': "",
                'ERROR': "Not Charging due to no balance returned\n"
            },
            'NBRCR': {
                'INFO': "",
                'ERROR': "Not Crediting due to no balance returned\n"
            },
            'ICPT': {
                'INFO': "",
                'ERROR': """Incorrect parameter type, expected types
name:string, account_number:integer, balance_limit:integer\n"""
            },
            'IANB': {
                'INFO': "",
                'ERROR': """Check your parameters for invalid account number/balance limit value
(examples. negatives or non-numbers)\n"""
            },
            'NNP': {
                'INFO': "",
                'ERROR': "Check your parameters for null name\n"
            },
            'ANOZ': {
                'INFO': "",
                'ERROR': "Amount is negative or 0, value must be greater than 0\n"
            },


        }

    def log_message(self, message_code):
        print self.messages[message_code][self.level]




