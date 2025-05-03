# from transformers import pipeline

# # Initialize the NLP model
# nlp = pipeline("zero-shot-classification", model="distilbert-base-uncased")

# def parse_user_input(user_input):
#     """
#     Parse the user input and map it to a cloud operation intent.
#     """
#     # Example intents
#     intents = ["create", "resize", "delete", "query"]

#     # Perform zero-shot classification to match the input to one of the intents
#     result = nlp(user_input, candidate_labels=intents)
    
#     intent = result['labels'][0]
#     if intent in ["create", "resize", "delete"]:
#         return extract_entities(user_input, intent)
#     elif intent == "query":
#         return {"action": "query", "resource": "usage"}
#     else:
#         return None

# def extract_entities(user_input, action):
#     """
#     Extract resource name and other entities from the user input.
#     """
#     # Example entity extraction (to be improved with regex or an NLU library)
#     if action == "create":
#         resource = "vm"  # Default resource
#         name = user_input.split("named")[-1].strip()
#         return {"action": action, "resource": resource, "name": name}
#     elif action == "resize":
#         resource = "vm"
#         name = user_input.split("to")[0].strip()
#         flavor = user_input.split("to")[-1].strip()
#         return {"action": action, "resource": resource, "name": name, "flavor": flavor}
#     elif action == "delete":
#         resource = "vm"
#         name = user_input.split("named")[-1].strip()
#         return {"action": action, "resource": resource, "name": name}
#     return None



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
