from app import app
from schemas.movies_api import *
from schemas.directors_api import *
from schemas.genres_api import *

if __name__ == '__main__':
    app.run(debug=True)