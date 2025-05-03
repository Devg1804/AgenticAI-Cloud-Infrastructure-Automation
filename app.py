from flask import Flask, request, jsonify, render_template
from dialog_manager import parse_user_input
from openstack_client import OpenStackClient
from db_logger import log_request

app = Flask(__name__)
client = OpenStackClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    confirmation = data.get("confirm")

    # Parse user input to extract intent and entities
    intent_data = parse_user_input(user_input)

    if not intent_data:
        return jsonify({"response": "Sorry, I didn't understand that."}), 400

    # Ask for confirmation if needed
    if intent_data["action"] in ["create", "resize", "delete"] and not confirmation:
        return jsonify({
            "response": f"Do you want to proceed with: {intent_data['action']} {intent_data['resource']} named {intent_data.get('name')}?",
            "intent": intent_data,
            "confirm_required": True
        })

    # Execute action after confirmation
    result = client.execute_intent(intent_data)
    log_request(user_input, intent_data, result)

    return jsonify({"response": result})

if __name__ == '__main__':
    app.run(debug=True)
