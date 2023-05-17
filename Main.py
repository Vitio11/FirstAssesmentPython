from flask import Flask, request, render_template
from abc import ABC, abstractmethod
from Clases.EquipamientoDeportivo import EquipamientoFutbol, EquipamientoBasketball, EquipamientoRugby

app = Flask(__name__,template_folder='html')

@app.route("/", methods =['GET'])
def Equipamiento():
    return render_template("start_Equipamiento.html")

@app.route("/mostrar_Equipamiento", methods=['POST'])
def mostrar_Equipamiento():
    # Obtener el equipamiento seleccionado por el usuario
    Equipamiento_ingresado= request.form["equipamiento"]
    Precio_ingresado = int(request.form["precio"])

    # Insertar el código aquí
    if Equipamiento_ingresado == "Futbol":
        talla_ingresada= request.form["talla"]
        equipamiento = EquipamientoFutbol(Equipamiento_ingresado,Precio_ingresado,talla_ingresada)
    elif Equipamiento_ingresado == "Baketball":
         talla_ingresada= request.form["talla"]
         material_ingresado= request.form["material"]
         equipamiento= EquipamientoBasketball(Equipamiento_ingresado,Precio_ingresado,talla_ingresada,material_ingresado)

    elif Equipamiento_ingresado == "Rugby":
        Precio_ingresado = int(request.form["precio"])
        peso_ingresado = request.form["precio"]
        equipamiento = EquipamientoRugby(Equipamiento_ingresado,Precio_ingresado,peso_ingresado)
                
        # Renderizar la página de Equipamiento con la equipamiento seleccionado
    return render_template("Equipamiento.html", Equipamiento=equipamiento)

@app.route("/volver", methods=["Post"])
def volver():
    return render_template("start_Equipamiento.html")
    

if __name__ == '__main__':
   app.run(debug=True)