from flask import Flask, render_template, request, redirect, url_for
from datetime import date, timedelta

app = Flask(__name__)

# Simulación de días ocupados
dias_ocupados = { "2025-08-15", "2025-08-18", "2025-08-21" }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/agenda")
def agenda():
    hoy = date.today()
    dias = []
    for i in range(15):
        dia = hoy + timedelta(days=i)
        fecha_str = dia.strftime("%Y-%m-%d")
        ocupado = fecha_str in dias_ocupados
        dias.append({"fecha": fecha_str, "ocupado": ocupado})
    return render_template("agenda.html", dias=dias)

@app.route("/reservar", methods=["GET", "POST"])
def reservar():
    if request.method == "POST":
        fecha = request.form.get("fecha")
        dias_ocupados.add(fecha)
        return redirect(url_for("agenda"))
    return render_template("reservar.html")

if __name__ == "__main__":
    app.run(debug=True)
