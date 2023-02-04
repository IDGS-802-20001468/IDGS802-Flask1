from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("Cinepolis.html")

@app.route("/layout")
def cargar():
    return render_template("layoutCinepolis.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    numBol = int(request.form.get("txtCBoletos"))
    rbt = request.form.get("rbt")
    resultado = 0
    if(numBol < 8):
        if(rbt == 'rbtSi'):
            if(numBol > 5):
                resultado = (12*numBol)-(12*numBol)*0.25
            elif(numBol > 2):
                resultado = (12*numBol)-(12*numBol)*0.20
            elif(numBol <= 2):
                resultado = (12*numBol)-(12*numBol)*0.10
        else:
            if(numBol > 5):
                resultado = (12*numBol)-(12*numBol)*0.15
            elif(numBol > 2):
                resultado = (12*numBol)-(12*numBol)*0.10
            elif(numBol <= 2):
                resultado = 12*numBol
    else:
        resultado = "No es posible comprar esa cantidad de boletos"
                
    return render_template("/Cinepolis.html", resultado = resultado, numBol = numBol)
    
if __name__ =="__main__":
    app.run(debug=True, port=3000)