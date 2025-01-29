from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer(), autoincrement= True, primary_key = True)
    username = db.Column(db.String(35), nullable = False )
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(35), nullable = False)
    role = db.Column(db.String(30), nullable = False)
    # created_at = db.Column( db.DateTime, default = datetime.utcnow )

    projects = db.relationship('Project', backref="user_owner")
    # requests = db.relationship("AccessRequest", backref= "requesters")

    def __repr__(self):
        return f" User {self.firstname}, {self.email}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # def update(self, firstname, lastname, email, password, role):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.email = email
    #     self.password = password
    #     self.role = role


# class Department(db.Model):

#     __tablename__ = 'departments'

#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(), unique = True, nullable = False)    
#     users = db.relationship('User', backref='department', lazy=True)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    supervisor_id = db.Column(db.Integer(), nullable = True)
    department = db.Column(db.String(50), nullable = False)
    # uploaded_at = db.Column(db.DateTime, nullable = True, default = datetime.utcnow())
    file_url = db.Column(db.String(100), nullable = True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable = True)

    # owner = db.relationship('User', backref = "Project")
    requests = db.relationship("AccessRequest", backref = "project")



    def __repr__(self):
        return f" User {self.title}, {self.description}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, description, department, supervisor_id, file_url ):
        self.title = title
        self.description = description
        self.department = department
        self.supervisor_id = supervisor_id
        self.file_url = file_url

        db.session.commit()
    

class AccessRequest(db.Model):
    __tablename__ = 'requesters'

    id = db.Column(db.Integer(), primary_key=True)
    requester_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    status = db.Column(db.String(25), default = 'Pending')
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'))
    # requested_at = db.Column(db.DateTime, default = datetime.utcnow)


    # requester = db.relationship('User', backref = "requests")
    projectss = db.relationship('Project', backref = "linked_requests")
    def __repr__(self):
        return(f"< Requester {self.requester_id} for project {self.project_id}>")
