from flask import Flask, render_template, request
import forms
import math
import formsResistencia

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


@app.route("/resistencias", methods=['GET', 'POST'])
def resistencias():
    banda1 = ''
    banda2 = ''
    banda3 = ''  
    tolerancia = ''

    valor1 = 0  
    valor2 = 0 
    
    resistencias = formsResistencia.Resistencias(request.form)
    if request.method == 'POST':
       banda1 = resistencias.banda1.data
       banda2 = resistencias.banda2.data
       banda3 = resistencias.banda3.data
       tolerancia = resistencias.tolerancia.data

    if banda1 == 'Negro':
        valor1 = 0
    elif banda1 == 'Cafe':
        valor1 = 1
    elif banda1 == 'Rojo':
        valor1 = 2
    elif banda1 == 'Naranja':
        valor1 = 3
    elif banda1 == 'Amarillo':
        valor1 = 4
    elif banda1 == 'Verde':
        valor1 = 5
    elif banda1 == 'Azul':
        valor1 = 6
    elif banda1 == 'Violeta':
        valor1 = 7
    elif banda1 == 'Gris':
        valor1 = 8
    elif banda1 == 'Blanco':
        valor1 = 9

    
    if banda2 == 'Negro':
        valor2 = 0
    elif banda2 == 'Cafe':
        valor2 = 1
    elif banda2 == 'Rojo':
        valor2 = 2
    elif banda2 == 'Naranja':
        valor2 = 3
    elif banda2 == 'Amarillo':
        valor2 = 4
    elif banda2 == 'Verde':
        valor2 = 5
    elif banda2 == 'Azul':
        valor2 = 6
    elif banda2 == 'Violeta':
        valor2 = 7
    elif banda2 == 'Gris':
        valor2 = 8
    elif banda2 == 'Blanco':
        valor2 = 9

    resultado = str(valor1) + str(valor2)
    if banda3 == 'Negro':
        resultado = int(resultado) * 1
    elif banda3 == 'Cafe':
        resultado = int(resultado) * 10
    elif banda3 == 'Rojo':
        resultado = int(resultado) * 100
    elif banda3 == 'Naranja':
        resultado = int(resultado) * 1000
    elif banda3 == 'Amarillo':
       resultado = int(resultado) * 10000
    elif banda3 == 'Verde':
        resultado = int(resultado) * 100000
    elif banda3 == 'Azul':
        resultado = int(resultado) * 1000000
    elif banda3 == 'Violeta':
        resultado = int(resultado) * 1000000
    elif banda3 == 'Gris':
        resultado = int(resultado) * 1000000
    elif banda3 == 'Blanco':
        resultado = int(resultado) * 1000000

    if banda2 == 'Negro':
        valor2 = 0
    elif banda2 == 'Cafe':
        valor2 = 1
    elif banda2 == 'Rojo':
        valor2 = 2
    elif banda2 == 'Naranja':
        valor2 = 3
    elif banda2 == 'Amarillo':
        valor2 = 4
    elif banda2 == 'Verde':
        valor2 = 5
    elif banda2 == 'Azul':
        valor2 = 6
    elif banda2 == 'Violeta':
        valor2 = 7
    elif banda2 == 'Gris':
        valor2 = 8
    elif banda2 == 'Blanco':
        valor2 = 9

    tol = 0
    if tolerancia == 'Dorado':
        tol = 0.5
    else:
        tol = .1

    coloruno = color(banda1)
    colordos = color(banda2)
    colortres = color(banda3)
    colorcuatro = color(tolerancia)
    print(colorcuatro)

    maximo = float(resultado) + (float(resultado) * tol)
    minimo = float(resultado) - (float(resultado) * tol)

    return render_template("resistencias.html", form=resistencias, banda1 = banda1, banda2 = banda2, banda3 = banda3
                           ,coloruno = coloruno, colordos = colordos, colortres = colortres, colorcuatro = colorcuatro, resultado = resultado,
                           tolerancia = tol, maximo = maximo, minimo = minimo)


def color(valor):
    color_seleccionado = ''

    if valor == 'Cafe':
        color_seleccionado = "brown"
    elif valor == 'Negro':
         color_seleccionado = "black"
    elif valor == 'Rojo':
         color_seleccionado = "red"
    elif valor == 'Naranja':
         color_seleccionado = "orange"
    elif valor == 'Amarillo':
         color_seleccionado = "yellow"
    elif valor == 'Verde':
         color_seleccionado = "green"
    elif valor == 'Azul':
         color_seleccionado = "blue"
    elif valor == 'Morado':
         color_seleccionado = "purple"
    elif valor == 'Gris':
         color_seleccionado = "gray"
    elif valor == 'Blanco':
         color_seleccionado = "white"
    elif valor == 'Dorado':
         color_seleccionado = "goldenrod"
    elif valor == 'Plateado':
         color_seleccionado = "silver"
    return color_seleccionado


@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    b1 = 0
    b2 = 0
    b3 = 0
    tol = 0
    color1 = ''
    color2 = ''
    color3 = ''
    color4 = ''
    val = 0
    minimo = 0
    maximo = 0

    resistencias = formsexm.Resistencias(request.form)
    if request.method == 'POST':
        b1 = resistencias.b1.data
        b2 = resistencias.b2.data
        b3 = resistencias.b3.data
        tol = resistencias.tol.data

        if int(b1) == 0:
            color1 = 'Negro'
        elif int(b1) == 1:
            color1 = 'Cafe'
        elif int(b1) == 2:
            color1 = 'Rojo'
        elif int(b1) == 3:
            color1 = 'Naranja'
        elif int(b1) == 4:
            color1 = 'Amarillo'
        elif int(b1) == 5:
            color1 = 'Verde'
        elif int(b1) == 6:
            color1 = 'Azul'
        elif int(b1) == 7:
            color1 = 'Violeta'
        elif int(b1) == 8:
            color1 = 'Gris'
        elif int(b1) == 9:
            color1 = 'Blanco'

        if int(b2) == 0:
            color2 = 'Negro'
        elif int(b2) == 1:
            color2 = 'Cafe'
        elif int(b2) == 2:
            color2 = 'Rojo'
        elif int(b2) == 3:
            color2 = 'Naranja'
        elif int(b2) == 4:
            color2 = 'Amarillo'
        elif int(b2) == 5:
            color2 = 'Verde'
        elif int(b2) == 6:
            color2 = 'Azul'
        elif int(b2) == 7:
            color2 = 'Violeta'
        elif int(b2) == 8:
            color2 = 'Gris'
        elif int(b2) == 9:
            color2 = 'Blanco'

        c3 = ""
        if int(b3) == 1:
            color3 = 'Negro'
            c3 = "black"
        elif int(b3) == 10:
            color3 = 'Cafe'
            c3 = "brown"
        elif int(b3) == 100:
            color3 = 'Rojo'
            c3 = "red"
        elif int(b3) == 1000:
            color3 = 'Naranja'
            c3 = "orange"
        elif int(b3) == 10000:
            color3 = 'Amarillo'
            c3 = "yellow"
        elif int(b3) == 100000:
            color3 = 'Verde'
            c3 = "green"
        elif int(b3) == 1000000:
            color3 = 'Azul'
            c3 = "blue"
        elif int(b3) == 10000000:
            color3 = 'Violeta'
            c3 = "purple"
        elif int(b3) == 100000000:
            color3 = 'Gris'
            c3 = "gray"
        elif int(b3) == 1000000000:
            color3 = 'Blanco'
            c3 = "white"

        c4 = ""
        if float(tol) == 0.05:
            color4 = 'Dorado'
            c4 = "goldenrod"
        elif float(tol) == 0.1:
            color4 = 'Plateado'
            c4 = "silver"

        x = str(b1) + str(b2)
        val = int(x) * int(b3)
        minimo =  float(val) - float(val) * float(tol)
        maximo = float(val) + float(val) * float(tol) 

        c1 = obtnerColor(int(b1))
        c2 = obtnerColor(int(b2))
        print("El elemento seleccionado es:" + tol)

    return render_template("ej.html", form=resistencias, b1=b1, b2=b2, b3=b3,
                           color1=color1, color2=color2, color3=color3, color4=color4, val=val,
                           tol=tol, maximo=maximo, minimo=minimo, c1 = c1, c2 = c2, c3 = c3, c4 = c4)

def obtnerColor(number):
    if number == 0:
        return "black"
    elif number == 1:
        return "brown"
    elif number == 2:
        return "red"
    elif number == 3:
        return "orange"
    elif number == 4:
        return "yellow"
    elif number == 5:
        return "green"
    elif number == 6:
        return "blue"
    elif number == 7:
        return "purple"
    elif number == 8:
        return "gray"
    elif number == 9:
        return "white"
        

if __name__ == "__main__":
    app.run(debug=True)