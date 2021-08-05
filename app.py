#Creating Virtual Enviroment: python3 -m venv env
#Activating Virtual Enviroment: source ./env/bin/activate

from flask import (render_template, 
                    url_for, request, redirect)
from models import (db, Project, app)


#Homepage
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('projectform.html')


@app.route('/<id>')
def detail(id):
    return render_template('detail.html')


@app.route('/<id>/edit')
def edit(id):
    return render_template('edit.html')


@app.route('/<id>/delete')
def delete(id):
    return render_template('delete.html')


@app.route('/about')
def about():
    return render_template('about.html')















if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')