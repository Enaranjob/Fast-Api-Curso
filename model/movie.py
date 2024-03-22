#La "magia" detrás de la creación automática de la tabla "movies" en SQLAlchemy se debe a la clase Base de config.database.py, que es una instancia de declarative_base(). Al heredar de esta clase al definir la clase Movie, se establece una conexión con la base de datos. Al ejecutar Base.metadata.create_all(bind=Engine) en main.py, SQLAlchemy utiliza esa conexión para crear la tabla automáticamente. Este proceso simplifica la creación de tablas y se basa en la funcionalidad ORM de SQLAlchemy.

from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
