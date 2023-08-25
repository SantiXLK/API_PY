from flask_restful import Resource
from ..modelos import db, Cancion, CancionesSchema
from flask import request

cancion_schema = CancionesSchema()

class VistasCanciones(Resource):
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'], \
                                minutos=request.json['minutos'], \
                                segundos=request.json['segundos'], \
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

class VistasCancion(Resource):
    def get(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operación exitosa', 204
