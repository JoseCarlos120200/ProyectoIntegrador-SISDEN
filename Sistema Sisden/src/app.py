from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

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

@app.route('/inicio')
def inicio():
    logout_user()
    return redirect(url_for('index'))


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
                    
                elif roluser =="Medico":
                    print("Medico")
                    return redirect(url_for('home'))
                elif roluser =="Asistente":
                    print("Asistente")
                    return redirect(url_for('hometres'))
                    
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
@login_required
def home():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    print(data)
    cur.close()
    return render_template('index_medico.html', coches = data)

@app.route('/hometres')
@login_required
def hometres():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    print(data)
    cur.close()
   
    return render_template('index_asistente.html', coches = data)




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
     ##################################3
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM clinica')
     data1 = cur.fetchall()
     print(data)
     print('cambio')
     cur.close()
     ##################################Activos
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM user WHERE estado="Activo"')
     data2 = cur.fetchall()
     print(data2)
     print('cambio')
     cur.close()
     ##################################Inactivos
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM user WHERE estado="Inactivo"')
     data3 = cur.fetchall()
     print(data3)
     print('cambio')
     cur.close()
     return render_template('index_clinica.html', coches = data,clinica=data1,activos=data2,inactivos=data3)

@app.route('/add_users', methods=['POST'])
def add_users():
    if request.method == 'POST':
        correo = request.form['correo']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        rol =request.form['rol']
        clinica=request.form['comp_select2']
        estado=request.form['estado']
        print(correo,nombre,contrasena,rol,clinica,estado)
        contrasena=generate_password_hash(contrasena, method='sha256')
        cur = db.connection.cursor()
        cur.execute("INSERT INTO user (username, password, fullname,estado,rol,clinica) VALUES (%s,%s,%s,%s,%s,%s)", (correo, contrasena, nombre, estado,rol,clinica))
        db.connection.commit()
        ##############################################
        cur1 = db.connection.cursor()
        cur1.execute('SELECT * FROM user')
        data1 = cur1.fetchall()
        print(data1)
        print('cambio')
        cur1.close()
        return redirect(url_for('homedos'))

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
        estado = request.form['estado']
        clinica =request.form['clinica']
        print(nombre,correo,contrasena,rol)
        contrasena=generate_password_hash(contrasena, method='sha256')
        cur = db.connection.cursor()
        cur.execute("UPDATE user SET username=%s,password=%s,fullname=%s,estado=%s,rol=%s,clinica=%s WHERE `id`=%s", (correo, contrasena, nombre, estado,rol,clinica,id))
        db.connection.commit()
        
        ##############################################
        cur1 = db.connection.cursor()
        cur1.execute('SELECT * FROM user')
        data1 = cur1.fetchall()
        print(data1)
        print('cambio')
        cur1.close()
        return redirect(url_for('homedos'))

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
        cur.execute("SELECT * FROM events WHERE clinica = %s AND title='' ORDER BY id;",[select])
        calendar = cur.fetchall() 
        print(calendar)
        print('cambio')
        cur.close()
        return render_template('calendar.html', calendar = calendar,data=data)
###################################################################################        
@app.route('/calendar_admin',methods=["POST"])
def calendar_admin():
     if request.method == 'POST':
        select = request.form.get('comp_select')
        data=select
        print(select)
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM events WHERE clinica = %s ORDER BY id;",[select])
        calendar = cur.fetchall() 
        print(calendar)
        print('cambio')
        cur.close()
        return render_template('calendarioadmin.html', calendar = calendar,data=data)

@app.route('/calendar_medico',methods=["POST"])
def calendar_medico():
     if request.method == 'POST':
        select = request.form.get('comp_select')
        data=select
        print(select)
        cur = db.connection.cursor()
        cur.execute("SELECT `consultorio`,`clinica`,`turno` FROM `user` WHERE `id`=%s;",[select])
        consultorio = cur.fetchall()
        print('consultorio')
        print(consultorio[0][0])
        if consultorio[0][0]=='1' and consultorio[0][2]=='Matutino':
            cur = db.connection.cursor()
            cur.execute("SELECT * from events where `consultorio`=%s AND `clinica`=%s AND `start_event` between curdate() + interval 9 hour and curdate() + interval 14 hour;",[consultorio[0][0],consultorio[0][1]])
            citas = cur.fetchall()
            print(citas)
            return render_template('calendariomedico.html', calendar = citas)
        elif consultorio[0][0]=='1' and consultorio[0][2]=='Vespertino':
            cur = db.connection.cursor()
            cur.execute("SELECT * from events where `consultorio`=%s AND `clinica`=%s AND `start_event` between curdate() + interval 15 hour and curdate() + interval 20 hour;",[consultorio[0][0],consultorio[0][1]])
            citas = cur.fetchall()
            print(citas)
            return render_template('calendariomedico.html', calendar = citas)
        elif consultorio[0][0]=='2' and consultorio[0][2]=='Matutino':
            cur = db.connection.cursor()
            cur.execute("SELECT * from events where `consultorio`=%s AND `clinica`=%s AND `start_event` between curdate() + interval 9 hour and curdate() + interval 14 hour;",[consultorio[0][0],consultorio[0][1]])
            citas = cur.fetchall()
            print(citas)
            return render_template('calendariomedico.html', calendar = citas)
        elif consultorio[0][0]=='2' and consultorio[0][2]=='Vespertino':
            cur = db.connection.cursor()
            cur.execute("SELECT * from events where `consultorio`=%s AND `clinica`=%s AND `start_event` between curdate() + interval 15 hour and curdate() + interval 20 hour;",[consultorio[0][0],consultorio[0][1]])
            citas = cur.fetchall()
            print(citas)
            return render_template('calendariomedico.html', calendar = citas)
        else:
            print("algo salio mal")
            return render_template('index_medico.html')


        cur.close()
        ####################################################### 
        
        
        return render_template('index_medico.html')
        #return render_template('calendar.html', calendar = calendar,data=data)
######################################################################################
@app.route("/insert",methods=["POST","GET"])
def insert():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM servicio')
    data1 = cur.fetchall()
    print(data1)
    print('cambio')
    cur.close()

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
        msg = 'success'


    return render_template('forms_cita_clinica.html',data=fecha,data1=data1)

    


@app.route('/add_event', methods=['POST'])
def add_event():
    print('evento')
    nombre = request.form.get('nombrepaciente')
    apellido = request.form['apellidopaciente']
    telefono = request.form['telefonopaciente']
    clinica = request.form['clinicapaciente']
    print(nombre,apellido,telefono,clinica)
    startevent =request.form['placa']
    endevent =request.form['color']
    lugar=request.form['marca']
    print(startevent)
    cur = db.connection.cursor()
    cur.execute("SELECT `consultorio` FROM `events` WHERE `start_event`=%s AND `clinica`=%s", (startevent,lugar))
    disponibilidad = cur.fetchall() 
    print(disponibilidad)
    cur.close()
    disponibilidad2=len(disponibilidad)
    print(disponibilidad2)
    if disponibilidad2>=2:
        return render_template('index.html')
    elif disponibilidad2==1 :
        print(disponibilidad[0][0])
        if disponibilidad[0][0]=='1':
            consultorio="2"
            cur = db.connection.cursor()
            cur.execute("INSERT INTO events (start_event, end_event,nombre, apellido, servicio,telefono,clinica,consultorio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (startevent,endevent,nombre, apellido, clinica, telefono,lugar,consultorio))
            db.connection.commit()
            
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
    return render_template('index.html')
################################################################################
###Servicios
####################################################################
@app.route('/servicios')
def servicios():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM servicio')
    data = cur.fetchall()
    print(data)
    cur.close()
    return render_template('servicios.html',servicios=data)

@app.route('/insertservicios',methods=['POST'])
def insertservicios():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        descripcion= request.form.get('descripcion')
        print(nombre,precio,descripcion)
        cur = db.connection.cursor()
        cur.execute("INSERT INTO servicio (servicio, precio,descripcion) VALUES (%s,%s,%s)", (nombre,precio,descripcion))
        db.connection.commit()
        print('Exito')
        return redirect(url_for('homedos'))

########################################################################
#citas
#####################################################################
@app.route('/consultarcitas')
def consultarcitas():
    cur = db.connection.cursor()
    cur.execute('SELECT * from events')
    data = cur.fetchall()
    print(data)
    cur.close()
    return render_template('citas_medico.html',citas=data)
#############################################
#cancelar citas
########################################
@app.route('/cancelar',methods=["POST","GET"])
def cancelar():
     if request.method == 'POST':
        ide = request.form.get('cancelarid')
        tel = request.form.get('cancelartel')
        cur = db.connection.cursor()
        cur.execute("UPDATE events SET title='Cancelado' WHERE id=%s AND telefono =%s", (ide,tel))
        db.connection.commit()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM events WHERE id=%s",[ide])
        reserva = cur.fetchall() 
        print(reserva)
        return render_template('comprobantecancelar.html',reserva=reserva)

##################################################################
#############detalles citas######################################
@app.route('/detallescita/<id>', methods = ['POST', 'GET'])
def detallescita(id):
     cur = db.connection.cursor()
     cur.execute('SELECT * FROM events WHERE id = %s;', [id])
     data = cur.fetchall()
     cur.close()
     print(data[0])
     return render_template('detalles.html', coches = data[0])

@app.route('/detallescitamedico/<id>', methods = ['POST', 'GET'])
def detallescitamedico(id):
     cur = db.connection.cursor()
     cur.execute('SELECT servicio.precio, events.id, events.title, events.start_event, events.end_event, events.nombre, events.nombre, events.apellido,events.servicio,events.telefono,events.clinica,events.consultorio FROM events INNER JOIN  servicio ON  events.servicio= servicio.servicio WHERE events.id=%s;', [id])
     data = cur.fetchall()
     cur.close()
     print(data[0])
     return render_template('detallesmedico.html', coches = data[0])

#################################################################################
##########pagado
#################################################################################
@app.route('/pagado',methods=["POST","GET"])
def pagado():
     if request.method == 'POST':
        total = request.form.get('total')
        ide = request.form.get('id')
        estado = request.form.get('estado')
        medico = request.form.get('medico')
        print(total)
        cur = db.connection.cursor()
        cur.execute("UPDATE `events` SET `title`=%s,`precio`=%s,`Medico`=%s WHERE `id`=%s", (estado,total,medico,ide))
        db.connection.commit()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM events WHERE id=%s",[ide])
        reserva = cur.fetchall() 
        print(reserva)
        return render_template('comprobantepago.html',reserva=reserva)

####################################################################333
@app.route('/calendar_asistente',methods=["POST"])
def calendar_asistente():
     if request.method == 'POST':
        select = request.form.get('comp_select')
        data=select
        print(select)
        cur = db.connection.cursor()
        cur.execute("SELECT `clinica` FROM `user` WHERE `id`=%s;",[select])
        consultorio = cur.fetchall()
        print('consultorio')
        print(consultorio[0][0])
        cur = db.connection.cursor()
        cur.execute("SELECT * from events where  `clinica`=%s AND `start_event` between curdate() + interval 8 hour and curdate() + interval 20 hour;",[consultorio[0][0]])
        citas = cur.fetchall()
        print(citas)
        cur.close()
        return render_template('calendarioasistente.html', calendar = citas)

@app.route('/pagado2',methods=["POST","GET"])
def pagado2():
     if request.method == 'POST':
        total = request.form.get('total')
        ide = request.form.get('id')
        estado = request.form.get('estado')
        medico = request.form.get('id')
        print(total)
        cur = db.connection.cursor()
        cur.execute("UPDATE `events` SET `title`=%s,`precio`=%s,`Medico`=%s WHERE `id`=%s", (estado,total,medico,ide))
        db.connection.commit()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM events WHERE id=%s",[ide])
        reserva = cur.fetchall() 
        print(reserva)
        return render_template('comprobantepago2.html',reserva=reserva)





   

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()

