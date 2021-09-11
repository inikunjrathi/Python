from flask import Flask, app, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
    },
]


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/get-data")
def get_data():
    return jsonify(tasks)


@app.route("/put-data", methods=["POST"])
def put_data():
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json["description"],
        "done": False,
    }
    tasks.append(task)
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
