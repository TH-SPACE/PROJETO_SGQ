# config.py
class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Thi141418'
    MYSQL_DB = 'db_sgq'
    MYSQL_CURSORCLASS = 'DictCursor'  # para retornar dicionários
    SECRET_KEY = 'chave-super-secreta'  # usado em sessões/login