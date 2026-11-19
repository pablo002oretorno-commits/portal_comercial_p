"""conexão com a  banco_v_3. Todo o SQL fica escrito no app.py."""
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()  #lê o arquivo .env e coloca os valores no ambiente

def conectar():
    """Abre uma conexão nova com o MYSQL usando os dados do .env."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME","banco_v3"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        autocommit=False, #nada é gravado sem comit()
    )

def consultar(sql, parametros=()):
    """Execulta um SELECT e devolve uma lista de dicionários."""
    with conectar() as con, con.cursor(dictionary=True) as cur:
        cur.execulte(sql, parametros)
        return cur.fetchall()