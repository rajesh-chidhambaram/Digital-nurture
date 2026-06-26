from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = [
    {
        "id": 1,
        "name": "Python Programming",
        "code": "CS101",
        "credits": 4
    },
    {
        "id": 2,
        "name": "Database Systems",
        "code": "CS102",
        "credits": 3
    }
]

@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)

@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    for course in courses:
        if course["id"] == id:
            return jsonify(course)

    return jsonify({
        "error": "Course not found"
    }), 404

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
            }),400

    new_course = {
        "id": len(courses)+1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(new_course)

    return jsonify(new_course),201

@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    data = request.get_json()

    for course in courses:

        if course["id"] == id:

            course["name"] = data["name"]
            course["code"] = data["code"]
            course["credits"] = data["credits"]

            return jsonify(course)

    return jsonify({
        "error":"Course not found"
    }),404

@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    for course in courses:

        if course["id"] == id:

            courses.remove(course)

            return jsonify({
                "message":"Course deleted"
            })

    return jsonify({
        "error":"Course not found"
    }),404