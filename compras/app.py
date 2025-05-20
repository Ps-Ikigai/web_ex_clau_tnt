from flask import Flask, render_template
app = Flask(__name__)
@app.route( '/' )
def inicio():
    return "¡Hola desde Flask!, mi internet es pésimo no logré visualizar el resultado. Profesor este mensaje es para usted"
if __name__ == '__main__':
    app.run(debug=True)

# Se registran los datos de los usuarios registrados para el Ejercicio 2
usuarios = {
    "juan": "admin",
    "pepe": "user"
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    edad = None
    cantidad_tarros = None
    total_sin_descuento = None
    total_con_descuento = None
    descuento_aplicado = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
            descuento_aplicado = 15
        elif edad > 30:
            descuento = 0.25
            descuento_aplicado = 25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template('ejercicio1.html', nombre=nombre, edad=edad,
                           cantidad_tarros=cantidad_tarros,
                           total_sin_descuento=total_sin_descuento,
                           total_con_descuento=total_con_descuento,
                           descuento_aplicado=descuento_aplicado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        if nombre in usuarios and usuarios[nombre] == contrasena:
            if nombre == 'juan':
                mensaje = "Bienvenido administrador Juan"
            elif nombre == 'pepe':
                mensaje = "Bienvenido usuario Pepe"
        else:
            mensaje = "Credenciales incorrectas"
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

