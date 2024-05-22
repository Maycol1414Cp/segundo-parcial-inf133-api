from flask import Blueprint, request, jsonify
from models.task_model import Task as task
from views.task_view import render_task_list, render_task_detail
from utils.decorators import jwt_required, roles_required

task_bp = Blueprint("task", __name__)


@task_bp.route("/tasks", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "member"])
def get_tasks():
    tasks = task.get_all()
    return jsonify(render_task_list(tasks))

@task_bp.route("/tasks/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "member"])
def get_task(id):
    task = task.get_by_id(id)
    if task:
        return jsonify(render_task_detail(task))
    return jsonify({"error": "task no encontrado"}), 404

@task_bp.route("/tasks", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_task():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    task = task(name=name, species=species, age=age)
    task.save()

    return jsonify(render_task_detail(task)), 201

@task_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_task(id):
    task = task.get_by_id(id)

    if not task:
        return jsonify({"error": "task no encontrado"}), 404

    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")


    task.update(name=name, species=species, age=age)

    return jsonify(render_task_detail(task))



@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_task(id):
    task = task.get_by_id(id)

    if not task:
        return jsonify({"error": "task no encontrado"}), 404

    task.delete()

    return "", 204
