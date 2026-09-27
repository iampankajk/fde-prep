from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 22,
        "course": "Data Science"
    }
]


@app.route('/students', methods = ["GET"])
def get_students():
    if request.method == "GET":

        course = request.args.get("course")
        age = request.args.get("age")

        if course and age:
            for student in students:
                if (student["course"].lower() == course.lower()) and (student["age"] == int(age)):
                    return jsonify(student), 200
            return jsonify({"message":"student doesn't exist of this course and age"}), 404
        elif course:
            for student in students:
                 if student["course"].lower() == course.lower():
                     return jsonify(student), 200
            return jsonify({"message":"student doesn't exist of this course"}), 404
        elif age:
            for student in students:
                if student["age"] == int(age):
                    return jsonify(student), 200
            return jsonify({"message":"student doesn't exist of this age"}), 404
        
        return jsonify(students), 200

@app.route('/student', methods = ["POST"])
def add_student():
    data = request.get_json()
    id = len(students) + 1
    name = data["name"]
    age = data["age"]
    course = data["course"]

    student = {"id":id , "name":name, "age":age, "course":course}
    students.append(student)

    return jsonify({"message":"student added successfully", "data":student}), 201

@app.route('/student/<int:id>', methods = ["GET"])
def get_student_by_id(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"message":"student doesn't exist"}), 404

@app.route('/student/<int:id>', methods = ["DELETE"])
def delete_student_by_id(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message":"student deleted successfully"}
    return jsonify({"message":"student doesn't exist"}), 404

@app.route('/student/<int:id>', methods = ["PATCH"])
def update_student_by_id(id):
    data = request.get_json()
    for student in students:
        if student["id"] == id:
            if "name" in data:
                student["name"] = data["name"]
            if "age" in data:
                student["age"] = data["age"]
            if "course" in data:
                student["course"] = data["course"]
            return jsonify({"message":"data has been updated"}), 200
        return jsonify({"message":"student doesn't exist"}), 404
    
if __name__ == "__main__":
    app.run()