from flask import Flask, request, jsonify

app = Flask(__name__)

# Game State
rooms = {
    "start": {"description": "You are in a dark room. Doors lead north and east.", "exits": ["north", "east"]},
    "north": {"description": "You found a forest glade.", "exits": ["south"]},
    "east": {"description": "You entered a cave full of bats!", "exits": ["west"]},
}

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    current_room = data.get("current_room")
    direction = data.get("direction")

    if current_room not in rooms:
        return jsonify({"error": "Invalid room"}), 400

    if direction not in rooms[current_room]["exits"]:
        return jsonify({"error": "Invalid direction"}), 400

    new_room = "north" if direction == "north" else "east" if direction == "east" else "start"
    return jsonify({"new_room": new_room, "description": rooms[new_room]["description"]})

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the MUD Game! Start in the 'start' room."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
