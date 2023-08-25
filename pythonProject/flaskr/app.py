from flaskr import create_app
from .modelos import Cancion, db, Usuario
from .modelos import Album, db
from .modelos import Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


with app.app_context():
    AlbumSchema = AlbumSchema()
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio = Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([AlbumSchema.dumps(Album) for Album in Album.query.all()])
