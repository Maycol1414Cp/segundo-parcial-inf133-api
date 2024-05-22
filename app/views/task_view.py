
# Se debe almacenar en **Base de Datos** los siguientes datos de las **Tareas**:
# - **id**: Identificador único de la tarea. De tipo **entero y autoincremental**.
# - **title**: Título de la tarea. De tipo **cadena de texto**.
# - **description**: Descripción de la tarea. De tipo **cadena de texto**.
# - **status**: Estado de la tarea (pendiente, en curso, completada). De tipo **cadena de texto**.
# - **created_at**: Fecha de creación de la tarea. De tipo **cadena de texto**.
# - **assigned_to**: Nombre del usuario asignado a la tarea. De tipo **cadena de texto**.
def render_task_list(tasks):
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "assigned_to": task.assigned_to,
        }
        for task in tasks
    ]

def render_task_detail(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "created_at": task.created_at,
        "assigned_to": task.assigned_to,
    }
