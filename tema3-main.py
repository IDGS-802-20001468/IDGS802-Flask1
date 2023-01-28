from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Mundo!!! --Nuevo--"

@app.route("/user/<string:user>")
def user(user):
    return "Hola : "+user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {} ".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "<h1> ID: {} nombre: {} </h1>".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "La suma es: {} ".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:n>")
def default(n = "datos"):
    return "El valor de n es: "+n

if __name__ =="__main__":
    app.run(debug=True, port=3000)