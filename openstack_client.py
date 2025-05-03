import requests
from config import OPENSTACK_ENDPOINTS, OPENSTACK_CREDENTIALS  # Assuming you store config here

class OpenStackClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.authenticate()

    def authenticate(self):
        """Authenticate with Keystone v3 and obtain a token."""
        auth_url = OPENSTACK_ENDPOINTS['auth'] + "/auth/tokens"
        credentials = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name": OPENSTACK_CREDENTIALS['username'],
                            "domain": {"name": OPENSTACK_CREDENTIALS['domain']},
                            "password": OPENSTACK_CREDENTIALS['password']
                        }
                    }
                },
                "scope": {
                    "project": {
                        "id" : OPENSTACK_CREDENTIALS['project_name']
                    }
                }
            }
        }

        # Authenticate with Keystone and get the token from headers
        response = self.session.post(auth_url, json=credentials)
        
        if response.status_code == 201:
            self.token = response.headers.get('X-Subject-Token')
            self.session.headers.update({'X-Auth-Token': self.token})
            print("✅ Authentication successful. Token obtained.")
        else:
            raise Exception(f"❌ Authentication failed: {response.status_code}\n{response.text}")

    def execute_intent(self, intent_data):
        """Execute the user's intent based on the action."""
        action = intent_data['action']
        resource = intent_data['resource']
        name = intent_data.get('name')

        if action == "create" and resource == "vm":
            return self.create_vm(name)
        elif action == "resize" and resource == "vm":
            return self.resize_vm(name, intent_data['flavor'])
        elif action == "delete" and resource == "vm":
            return self.delete_vm(name)
        else:
            return "❗ Unsupported action or resource."

    def create_vm(self, name):
        """Create a new virtual machine."""
        url = f"{OPENSTACK_ENDPOINTS['compute']}/servers"
        data = {
            "server": {
                "name": name,
                # "imageRef": "image-id",   # You should set this properly
                # "flavorRef": "flavor-id"  # Same here
            }
        }
        response = self.session.post(url, json=data)
        if response.status_code == 202:
            return response.json()
        else:
            return f"❌ Failed to create VM: {response.text}"

    def resize_vm(self, name, flavor):
        """Resize an existing virtual machine."""
        url = f"{OPENSTACK_ENDPOINTS['compute']}/servers/{name}/action"
        data = {
            "resize": {
                "flavorRef": flavor
            }
        }
        response = self.session.post(url, json=data)
        if response.status_code == 202:
            return {"message": "✅ Resize operation initiated."}
        else:
            return f"❌ Failed to resize VM: {response.text}"

    def delete_vm(self, name):
        """Delete a virtual machine."""
        url = f"{OPENSTACK_ENDPOINTS['compute']}/servers/{name}"
        response = self.session.delete(url)
        if response.status_code == 204:
            return {"message": "🗑️ VM deleted successfully."}
        else:
            return f"❌ Failed to delete VM: {response.text}"
