from flask import Flask, render_template, request

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




if __name__ == "__main__":
    app.run(debug=True)