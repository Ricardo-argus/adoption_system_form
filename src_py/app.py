#back end flask ou django 

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="C:\\tocadospeludos\\.env")

app = Flask(__name__, template_folder="C:\\tocadospeludos\\template")


# Função auxiliar para conectar ao banco
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Página inicial - lista de adotantes
@app.route("/")
def main_screen():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adotantes")
    adotantes = cursor.fetchall()
    conn.close()
    return render_template("main_screen.html", adotantes=adotantes)

# Página de cadastro
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

# Rota para salvar adotante
@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    ambiente = request.form["ambiente"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO adotantes (nome, cpf, email, telefone, endereco, ambiente) VALUES (%s, %s, %s, %s, %s, %s)",
        (nome, cpf, email, telefone, endereco, ambiente)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("main_screen"))

if __name__ == "__main__":
    app.run(debug=True)