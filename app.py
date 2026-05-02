from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

archivo = "invitados.xlsx"

# Crear Excel si no existe
if not os.path.exists(archivo):
    df = pd.DataFrame(columns=["Familia", "Cantidad", "Asistencia"])
    df.to_excel(archivo, index=False)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/confirmar", methods=["POST"])
def confirmar():
    familia = request.form["familia"]
    cantidad = request.form["cantidad"]
    asistencia = request.form["asistencia"]

    df = pd.read_excel(archivo)

    nuevo = pd.DataFrame([[familia, cantidad, asistencia]],
                         columns=["Familia", "Cantidad", "Asistencia"])

    df = pd.concat([df, nuevo], ignore_index=True)
    df.to_excel(archivo, index=False)

    return redirect("/gracias")

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

app.run(debug=True)
