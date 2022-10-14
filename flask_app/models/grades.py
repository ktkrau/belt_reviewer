from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash #para mandar mensajes/errores
from datetime import datetime #manipular fechas / importacion directamente de python
class Grade:

    def __init__(self, data):
        self.id = data['id']
        self.alumno = data['alumno']
        self.stack = data['stack']
        self.fecha = data['fecha']
        self.calificacion = data['calificacion']
        self.cinturon = data['cinturon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    
    @staticmethod
    def valida_calificacion(formulario):
        es_valido = True

        if formulario['alumno'] == '':
            flash('Alumno no puede estar vacío', 'grades')
            es_valido = False
        if formulario['calificacion'] == '':
            flash('Ingresa una calificacion', 'grades')
            es_valido = False
        else:
            if int(formulario['calificacion']) <1 or int(formulario['calificacion']) > 10:
                flash('Calificación debe ser entre 1 y 10', 'grade')
                es_valido = False
        if formulario['fecha'] == '':
            flash('Ingresa una fecha', 'grades')
            es_valido = False
        else:
            #recibo la fecha como un texto, quiero pasar ese texto a datetime(tipo fecha)
            fecha_obj = datetime.strptime(formulario['fecha'], '%Y-%m-%d') #estamos transformando un texto a formato fecha
            #obtener la fecha de hoy:
            hoy = datetime.now()
            #comparacion de las dos fechas:
            if hoy < fecha_obj:
                flash('La fecha debe ser en pasado', 'grades')
                es_valido = False

        return es_valido


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO grades (alumno, stack, fecha, calificacion, cinturon, user_id) VALUES (%(alumno)s, %(stack)s, %(fecha)s, %(calificacion)s, %(cinturon)s, %(user_id)s)"
        result = connectToMySQL('belt_reviewer').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM grades"
        results = connectToMySQL('belt_reviewer').query_db(query)
        #recibo lista de diccionario y quiero una lista de instancias
        grades = []
        for grade in results:
            grades.append(cls(grade))

        return grades

    @classmethod
    def get_by_id(cls, formulario):#para editar
        query = "SELECT * FROM grades WHERE id = %(id)s"
        result = connectToMySQL('belt_reviewer').query_db(query, formulario)
        grade = cls(result[0])
        return grade
        
    @classmethod
    def update(cls, formulario):
        query = "UPDATE grades SET alumno=%(alumno)s, stack=%(stack)s, fecha=%(fecha)s, calificacion=%(calificacion)s, cinturon=%(cinturon)s, user_id=%(user_id)s WHERE id=%(id)s"
        result = connectToMySQL('belt_reviewer').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM grades WHERE id=%(id)s"
        result = connectToMySQL('belt_reviewer').query_db(query, formulario)
        return result
        


        






