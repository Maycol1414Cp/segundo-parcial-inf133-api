from database import db
#  Se debe almacenar en **Base de Datos** los siguientes datos de las **Tareas**:
# - **id**: Identificador único de la tarea. De tipo **entero y autoincremental**.
# - **title**: Título de la tarea. De tipo **cadena de texto**.
# - **description**: Descripción de la tarea. De tipo **cadena de texto**.
# - **status**: Estado de la tarea (pendiente, en curso, completada). De tipo **cadena de texto**.
# - **created_at**: Fecha de creación de la tarea. De tipo **cadena de texto**.
# - **assigned_to**: Nombre del usuario asignado a la tarea. De tipo **cadena de texto**.

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.String(20), nullable=False)
    assigned_to = db.Column(db.String(50), nullable=False)

    def __init__(self, title, description, status, created_at, assigned_to):
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.assigned_to = assigned_to

    def save(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return '<Task %r>' % (self.title)
    
    @staticmethod
    def get_all():
        return Task.query.all()
    
    def __init__(self, title=None, description=None, status=None, created_at=None, assigned_to=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None: 
            self.assigned_to = assigned_to
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
