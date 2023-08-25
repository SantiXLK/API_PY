from flaskr import create_app
from .modelos import Cancion, db, Usuario
from .modelos import Album, db
from .modelos import Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = Usuario(nombre = 'juan', contrasenia='12345')
    c = Cancion(titulo="prueba", minutos=2, segundos=25, interprete="Santiago")
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio = Medio.CD)
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())