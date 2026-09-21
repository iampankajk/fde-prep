from flask import Flask, jsonify, request

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

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Home Page </h1>"

@app.route("/students", methods=["GET","POST"])
def students():
    if request.method == "GET":
        return jsonify(students)

    if request.method == "POST":

        data = request.json()

        id = len(students) + 1
        name = data["name"]
        age  = data["age"]
        course = data["course"]

        student = {
            "id":id,
            "name":name,
            "age":age,
            "course":course
        }

        students.append(student)
        return jsonify(student)


@app.route("/test")
def testing():
    return "Test"


@app.route("/student/<int:id>", methods = ["GET", "PUT"])
def get_student(id):
    if request.method == "GET":
        for student in students:
            if id == student['id']:
                return jsonify(student)

        return "NOT FOUND"

    if request.method == "PUT":
        data = request.json()
        
        name = data["name"]
        age  = data["age"]
        course = data["course"]

        for student in students:
            if id == student["id"]:
                student["name"] = name
                student["age"] = age
                student["course"] = course

                return jsonify(student)

        return "NOT Found"

if __name__ == "__main__":
    app.run()