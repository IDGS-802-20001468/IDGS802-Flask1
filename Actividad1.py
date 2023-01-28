from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    if request.method=="POST":
        num1 = request.form.get("num1") 
        num2 = request.form.get("num2")
        operacion = request.form.get("operasB")
        if(operacion == "suma"):
            return "<h1> La suma es: {} </h1>".format(str(int(num1) + int(num2)))
        elif(operacion == "resta"):
            return "<h1> La resta es: {} </h1>".format(str(int(num1) - int(num2)))
        elif(operacion == "multi"):
            return "<h1> La multiplicación es: {} </h1>".format(str(int(num1) * int(num2)))
        elif(operacion == "division"):
            return "<h1> La división es: {} </h1>".format(str(int(num1) / int(num2)))

    else:
        return '''
        <form action = "/operasBas" method = "POST">
        <label> N1: </label>
        <input type = "text" name = "num1" /> </br> </br>
        <label> N2: </label>
        <input type = "text" name = "num2" /> </br> </br>
        <input type="radio" id="suma" name="operasB" value="suma">
        <label for="suma">Sumar</label>
        <input type="radio" id="resta" name="operasB" value="resta">
        <label for="resta">Restar</label>
        <input type="radio" id="multi" name="operasB" value="multi">
        <label for="multi">Multiplicar</label>
        <input type="radio" id="division" name="operasB" value="division">
        <label for="division">Dividir</label></br> </br>
        <input type = "submit" value = "calcular"/>
        </form>
        '''


if __name__ =="__main__":
    app.run(debug=True, port=3000)

    
        