from flaskr import create_app
from .modelos import db, Album, Usuario, Medio, AlbumSchema
from flask_restful import Api
from .vistas import VistasCanciones, VistasCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(VistasCanciones, '/canciones')
api.add_resource(VistasCancion, '/canciones/<int:id_cancion>')

with app.app_context():
    album_schema = AlbumSchema()
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([album_schema.dump(album) for album in Album.query.all()])
