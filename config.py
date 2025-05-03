# config.py

# # OpenStack credentials
# OPENSTACK_AUTH_URL = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000/v3"
# OPENSTACK_USERNAME = "Hackathon_AIML_1"
# OPENSTACK_PASSWORD = "Hackathon_AIML_1@567"
# OPENSTACK_PROJECT_NAME = "a02b14bcfca64e44bd68f2d00d8555b5"
# OPENSTACK_DOMAIN_NAME = "default"

# Hugging Face API settings
# HUGGINGFACE_API_TOKEN = "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"  # Replace with your actual token
HUGGINGFACE_API_KEY = "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"
# OPENSTACK_CONFIG = {
#     "username": "Hackathon_AIML_1",
#     "password": "Hackathon_AIML_1@567",
#     "project_name": "a02b14bcfca64e44bd68f2d00d8555b5",
#     "auth_url": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000/v3"
# }
# OPENSTACK_ENDPOINTS = {
#     "compute": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1",
#     "network": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9696",
#     "volume": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3",
# }

# OpenStack authentication and endpoint details
OPENSTACK_CREDENTIALS = {
    "username": "Hackathon_AIML_1",
    "password": "Hackathon_AIML_1@567",
    "project_name": "a02b14bcfca64e44bd68f2d00d8555b5",
    "domain": "default"  # You can change this if you're using a different domain
}

OPENSTACK_ENDPOINTS = {
    "auth": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000/v3",  # Keystone auth URL
    "compute": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1",  # Compute API endpoint
    "network": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9696",  # Networking API endpoint
    "volume": "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3/a02b14bcfca64e44bd68f2d00d8555b5"  # Volume API endpoint
}

