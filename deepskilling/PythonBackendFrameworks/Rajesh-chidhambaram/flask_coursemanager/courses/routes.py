from flask import Blueprint, jsonify, request

from extensions import db
from .models import Course

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return jsonify([
        course.to_dict()
        for course in courses
    ])

@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get(id)

    if course is None:
        return jsonify({
            "error": "Course not found"
        }), 404

    return jsonify(course.to_dict())


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    required = [
        "name",
        "code",
        "credits"
    ]

    for field in required:

        if field not in data:

            return jsonify({
                "error": f"{field} is required"
            }), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"]
    )

    db.session.add(course)

    db.session.commit()

    return jsonify(
        course.to_dict()
    ), 201

@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get(id)

    if course is None:
        return jsonify({
            "error": "Course not found"
        }), 404

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]

    db.session.commit()

    return jsonify(
        course.to_dict()
    )

@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get(id)

    if course is None:
        return jsonify({
            "error": "Course not found"
        }), 404

    db.session.delete(course)

    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })