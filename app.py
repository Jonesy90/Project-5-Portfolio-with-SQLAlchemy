#Creating Virtual Enviroment: python3 -m venv env
#Activating Virtual Enviroment: source ./env/bin/activate
import itertools
from flask import (render_template, 
                    url_for, request, redirect)
from models import (db, Project, app, datetime)

#Homepage
@app.route('/') 
def index():
    projects = Project.query.all()
    skills = []
    for project in projects:
        skills.append(project.skills.split(", "))
    all_skills = list(itertools.chain.from_iterable(skills))
    all_skills = list(dict.fromkeys(all_skills))
    return render_template('index.html', projects=projects, skills=all_skills)

#A route to the 'create project' page.
#Takes the values supplied by user in the form and creates a Project object, which is then sent to the database.
@app.route('/new', methods=['GET', 'POST'])
def create():
    if request.form:
        new_project = Project(title=request.form['title'], date=datetime.datetime.strptime(request.form['date'], '%Y-%m'), description=request.form['desc'], skills=request.form['skills'], project_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


#A route to the 'detail' page.
#When the user selects a project, they are taken to a new page which details everything about that project for them to view.
#On this page, the user can decide to update or delete the project.
@app.route('/detail/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    projects = Project.query.all()
    skills = project.skills.split(", ")
    return render_template('detail.html', project=project, skills=skills, projects=projects)


#A route to allow the user to 'edit' the project they're current under.
#This has an identical form as the 'create' page but it will override any all the values.
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.date = datetime.datetime.strptime(request.form['date'], '%Y-%m')
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.project_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=project)


#A route to allow the user to delete an entire 'project' entry from the database.
@app.route('/delete/<id>')
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


#A route to take the user to the 'about.html' page.
@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


#A route to handle any error that may occur, if something can't be found a 404 error will execute.
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')