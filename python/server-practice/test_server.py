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

@app.route("/students")
def students():
    return jsonify(students)

@app.route("/test")
def testing():
    return "Test"


@app.route("/student/<int:id>")
def test(id):
    student  = list(filter(lambda x : x["id"] == id, students))
    return jsonify(student[0])

if __name__ == "__main__":
    app.run()