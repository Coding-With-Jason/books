from books_app import app

from books_app.controllers import books
from books_app.controllers import authors

if __name__=='__main__':
    app.run(debug=True)