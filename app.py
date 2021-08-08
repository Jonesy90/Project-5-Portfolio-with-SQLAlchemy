#Creating Virtual Enviroment: python3 -m venv env
#Activating Virtual Enviroment: source ./env/bin/activate

from flask import (render_template, 
                    url_for, request, redirect)
from models import (db, Project, app, datetime)


#Homepage
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/new', methods=['GET', 'POST'])
def create():
    if request.form:
        # date = datetime.date(request.form['date'])
        # new_date = date.strftime('%d-%m=%Y')
        new_project = Project(title=request.form['title'], date=datetime.datetime.strptime(request.form['date'], '%d/%m/%Y').date(), description=request.form['desc'], skills=request.form['skills'], project_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/detail/<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.project_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=project)


@app.route('/delete/<id>')
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')