from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medios, AlbumSchema
from flask_restful import Api, Resource
from .vistas import VistaCanciones, VistaCancion, VistaAlbumes, VistaAlbum, VistaUsuarios, VistaUsuario


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')
api.add_resource(VistaAlbumes, '/albumes')
api.add_resource(VistaAlbum, '/albumes/<int:id_album>')
api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaUsuario, '/usuarios/<int:id_usuario>')

with app.app_context():
    u = Usuario(nombre_usuario='Julian T', contrasena='A.54@z')
    al = Album(titulo='Artaud', anio=1973, descripcion='clasico', medio=Medios.DISCO)
    c = Cancion(titulo='Bajan', minutos=5, segundos=45, interprete='Spinetta')
    u.albumes.append(al)
    al.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Usuario.query.all())
    print([AlbumSchema().dumps(Album) for Album in Album.query.all()])
    print(Album.query.all())
    print(Usuario.query.all()[0].albumes)
    print(Cancion.query.all())
    db.session.delete(al)
