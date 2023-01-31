from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/operasBas", methods=["GET"])
def operasBas():
    return render_template("operasbas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")

    res = int(n1) * int(n2)
    i = 0
    suma = 0
    impSuma = ""
    while i < int(n2):
        suma = suma + int(n1)
        if impSuma == "":
            impSuma = impSuma + n1
        else:
            impSuma = impSuma +" + "+ n1
        i += 1

    return render_template("/resultado.html", res = res,impSuma = impSuma, suma = suma)


if __name__ =="__main__":
    app.run(debug=True, port=3000)