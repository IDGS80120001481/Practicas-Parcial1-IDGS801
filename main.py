from flask import Flask, render_template, request
import forms
import math

app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def operasbas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
     if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")

        if request.form.get("rbd") == "suma":
            return "<h2> La suma es: {}</h2>".format(str(int(num1)+int(num2)))
        elif request.form.get("rbd") =="resta":
            return "<h2> La resta es: {}</h2>".format(str(int(num1)-int(num2)))
        elif request.form.get("rbd") == "mult":
            return "<h2> La multiplicacion es: {}</h2>".format(str(int(num1)*int(num2)))
        elif request.form.get("rbd") == "div":
            return "<h2> La division es: {}</h2>".format(str(int(num1)/int(num2)))


@app.route("/distancia", methods=['GET','POST'])
def alumnos():
    coordenadaX1 = ''
    coordenadaY1 = ''
    coordenadaX2 = ''
    coordenadaY2 = ''
    resultado = 0

    coordenadas = forms.Coordenadas(request.form)
    if request.method == 'POST':
        coordenadaX1 = coordenadas.coordenadaX1.data 
        print(coordenadaX1)
        print("UNO")
        coordenadaY1 = coordenadas.coordenadaY1.data 
        print(coordenadaY1)
        print("DOS")
        coordenadaX2 = coordenadas.coordenadaX2.data 
        print(coordenadaX2)
        print("Tres")
        coordenadaY2 = coordenadas.coordenadaY2.data 
        print(coordenadaY2)
        print("Cuatro")

        resta1 = coordenadaX2 - coordenadaX1
        resta1 = resta1 ** 2
        resta2 = coordenadaY2 - coordenadaY1
        resta2 = resta2 ** 2
        print(resta2)
        resultado = math.sqrt(resta1 + resta2)

    return render_template("Coordenadas.html", form=coordenadas, coordenadaX1 = coordenadaX1,
                            coordenadaY1 = coordenadaY1, coordenadaX2 = coordenadaX2,
                            coordenadaY2 = coordenadaY2, resultado = resultado)



if __name__ == "__main__":
    app.run(debug=True)