from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)
app.secret_key = "mysecretkey"

db = MySQL(app)
login_manager_app = LoginManager(app)    
idusuario=""

@login_manager_app.user_loader
def load_user(id):

    print("id es",id)
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        
        if logged_user != None:
            if logged_user.password:

                print(logged_user.password)
                print(logged_user.rol)
                roluser=logged_user.rol
                login_user(logged_user)
                if roluser =="Admin":
                    print("entre como admin")
                    return redirect(url_for('homedos'))
                    
                elif roluser =="Operador":
                    print("Operador")
                    return redirect(url_for('home'))
                    
                else:
                    return redirect(url_for('home'))


            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    print(data)
    cur.close()
   
    return render_template('index_clinica.html', coches = data)




@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404





#########################CRUD#####################################




###################################################################
@app.route('/homedos')
def homedos():
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM user')
     data = cur.fetchall()
     print(data)
     print('cambio')
     cur.close()
     return render_template('index_clinica.html', coches = data)

@app.route('/add_users', methods=['POST'])
def add_users():
    if request.method == 'POST':
        correo = request.form['correo']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        rol =request.form['rol']
        print(correo,nombre,contrasena,rol)
        contrasena=generate_password_hash(contrasena, method='sha256')
        cur = db.connection.cursor()
        cur.execute("INSERT INTO user (username, password, fullname,rol) VALUES (%s,%s,%s,%s)", (correo, contrasena, nombre, rol))
        db.connection.commit()
        flash('Se agrego al registro')
        ##############################################
        cur1 = db.connection.cursor()
        cur1.execute('SELECT * FROM user')
        data1 = cur1.fetchall()
        print(data1)
        print('cambio')
        cur1.close()
        return render_template('index_clinica.html', coches = data1)

@app.route('/salida/<id>', methods = ['POST', 'GET'])
def salida(id):
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM user WHERE id = %s;', [id])
     data = cur.fetchall()
     cur.close()
     print(data[0])
     return render_template('salida.html', coches = data[0])

@app.route('/pago/<id>', methods = ['POST', 'GET'])
def pago(id):
     if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        rol =request.form['rol']
        print(nombre,correo,contrasena,rol)
        contrasena=generate_password_hash(contrasena, method='sha256')
        cur = db.connection.cursor()
        cur.execute("INSERT INTO user (username, password, fullname,rol) VALUES (%s,%s,%s,%s)", (correo, contrasena, nombre, rol))
        db.connection.commit()
        flash('Se agrego al registro')
        ##############################################
        cur1 = db.connection.cursor()
        cur1.execute('SELECT * FROM user')
        data1 = cur1.fetchall()
        print(data1)
        print('cambio')
        cur1.close()
        return render_template('index_clinica.html', coches = data1)

# @contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
# def delete_contact(id):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
#     mysql.connection.commit()
#     flash('Contact Removed Successfully')
#     return redirect(url_for('contacts.Index'))

##################################################################################

###################################################################################3

@app.route('/event',methods=["POST","GET"])
def event():
    if request.method == 'POST':
        select = request.form.get('cinica')
        print(select)
    return redirect(url_for('calendar'))

@app.route('/calendar',methods=["POST","GET"])
def calendar():
     if request.method == 'POST':
        select = request.form.get('clinica')
        data=select
        print(select)
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM events WHERE clinica = %s ORDER BY id;",[select])
        calendar = cur.fetchall() 
        print(calendar)
        print('cambio')
        cur.close()
        return render_template('calendar.html', calendar = calendar,data=data)

@app.route("/insert",methods=["POST","GET"])
def insert():
    cur = db.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        lugar=request.form['lugar']
        global fecha
        fecha=(start,end,lugar)
        print('esat es la fecha')
        print(fecha)     
        print(start)  
        # cur.execute("INSERT INTO events (title,start_event,end_event) VALUES (%s,%s,%s)",[title,start,end])
        # mysql.connection.commit()       
        # cur.close()
        msg = 'success'  
    return render_template('forms_cita_clinica.html',data=fecha)

@app.route('/add_event', methods=['POST'])
def add_event():
    print('evento')
    nombre = request.form['nombrepaciente']
    apellido = request.form['apellidopaciente']
    telefono = request.form['telefonopaciente']
    clinica = request.form['clinicapaciente']
    print(nombre,apellido,telefono,clinica)
    startevent =request.form['placa']
    endevent=request.form['marca']
    print(startevent)
    
    lugar=request.form['color']
    print(lugar)
    cur = db.connection.cursor()
    cur.execute("SELECT `consultorio` FROM `events` WHERE `start_event`=%s AND `clinica`=%s", (startevent,lugar))
    disponibilidad = cur.fetchall() 
    print(disponibilidad)
    cur.close()
    disponibilidad2=len(disponibilidad)
    print(disponibilidad2)
    if disponibilidad2>=2:
        flash('Lo siento ese horario ya se encuentra disponible, revisa nuevamente el calendario.')
    elif disponibilidad2==1 :
        print(disponibilidad[0][0])
        if disponibilidad[0][0]=='1':
            consultorio="2"
            cur = db.connection.cursor()
            cur.execute("INSERT INTO events (start_event, end_event,nombre, apellido, servicio,telefono,clinica,consultorio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (startevent,endevent,nombre, apellido, clinica, telefono,lugar,consultorio))
            db.connection.commit()
            flash('Se agrego al registro')
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM `events` WHERE `start_event`=%s AND `consultorio`=%s AND `clinica`=%s", (startevent,consultorio,lugar))
            reserva = cur.fetchall() 
            print(reserva)
            return render_template('reservapdf.html',reserva=reserva)
        elif disponibilidad[0][0]=='2':
            consultorio="1"
            cur = db.connection.cursor()
            cur.execute("INSERT INTO events (start_event, end_event,nombre, apellido, servicio,telefono,clinica,consultorio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (startevent,endevent,nombre, apellido, clinica, telefono,lugar,consultorio))
            db.connection.commit()
            flash('Se agrego al registro')
            print('el consultorio ocupado es:')
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM `events` WHERE `start_event`=%s AND `consultorio`=%s AND `clinica`=%s", (startevent,consultorio,lugar))
            reserva = cur.fetchall() 
            print(reserva)
            return render_template('reservapdf.html',reserva=reserva)
    elif disponibilidad2==0:
        consultorio="1"
        cur = db.connection.cursor()
        cur.execute("INSERT INTO events (start_event, end_event,nombre, apellido, servicio,telefono,clinica,consultorio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (startevent,endevent,nombre, apellido, clinica, telefono,lugar,consultorio))
        db.connection.commit()
        flash('Se agrego al registro')
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM `events` WHERE `start_event`=%s AND `consultorio`=%s AND `clinica`=%s", (startevent,consultorio,lugar))
        reserva = cur.fetchall() 
        print(reserva)
        return render_template('reservapdf.html',reserva=reserva)


    else:    
        print('fallo')
    # cur = db.connection.cursor()
    # cur.execute("INSERT INTO events (start_event, end_event,nombre, apellido, servicio,telefono,clinica) VALUES (%s,%s,%s,%s,%s,%s,%s)", (startevent,endevent,nombre, apellido, clinica, telefono,lugar))
    # db.connection.commit()
    # flash('Se agrego al registro')

    print(nombre,apellido,telefono,clinica)
    return render_template('index_clinica.html')







   

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()

