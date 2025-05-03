

from transformers import pipeline

# Initialize the zero-shot classification pipeline
nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def parse_user_input(user_input):
    """
    Parse the user input and determine the user's intent.
    """
    intents = ["create", "resize", "delete"]
    result = nlp(user_input, candidate_labels=intents)
    intent = result['labels'][0]

    return extract_entities(user_input, intent)

def extract_entities(user_input, action):
    """
    Extract relevant entities based on the detected action.
    """
    resource = "vm"  # Assume 'vm' for simplicity

    if action == "create":
        # Example: "Create a vm named test-vm"
        if "named" in user_input:
            name = user_input.split("named")[-1].strip()
        else:
            name = "unknown"
        return {"action": action, "resource": resource, "name": name}

    elif action == "resize":
        # Example: "Resize vm test-vm to large"
        parts = user_input.split("to")
        if len(parts) == 2:
            name = parts[0].replace("resize", "").replace("vm", "").strip()
            flavor = parts[1].strip()
        else:
            name = "unknown"
            flavor = "unknown"
        return {"action": action, "resource": resource, "name": name, "flavor": flavor}

    elif action == "delete":
        # Example: "Delete vm named test-vm"
        if "named" in user_input:
            name = user_input.split("named")[-1].strip()
        else:
            name = user_input.replace("delete", "").replace("vm", "").strip()
        return {"action": action, "resource": resource, "name": name}

    return None
