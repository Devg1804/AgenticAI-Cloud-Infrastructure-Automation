# ChatCloud: Agentic AI for OpenStack Cloud Operations

## Overview

ChatCloud is a conversational AI agent designed to streamline your OpenStack cloud infrastructure management through natural language interaction. Forget complex CLI commands and API calls – simply tell ChatCloud what you need, and it will handle the rest. This agent empowers cloud operators by providing an intuitive and efficient way to manage Virtual Machines (VMs), Networks, and Volumes. ChatCloud intelligently interprets your requests, maps them to the necessary OpenStack API operations, and executes them after your explicit confirmation.

### Key Features:

* **Natural Language Understanding:** Leverages a pre-trained natural language model for zero-shot intent recognition, allowing you to interact using plain English.
* **Core Cloud Operations:** Supports essential OpenStack actions, including creating, resizing, and deleting Virtual Machines.
* **Resource Inquiry:** Enables you to easily query project usage and get insights into your resource consumption.
* **Action Confirmation:** Implements a crucial confirmation step before executing any operation that modifies your cloud resources, preventing accidental changes.
* **Request Logging:** Maintains a comprehensive database log of all user interactions for auditing and tracking purposes.
* **Secure Communication:** Utilizes HTTPS for secure API communication.

---

## Architecture

The ChatCloud architecture is composed of the following key components:

* **API Layer:** Provides the interface for receiving user input via HTTP POST requests and returning the agent's responses.
* **Natural Language Processing (NLP):** Employs a pre-trained transformer model to understand the user's intent and extract relevant entities from their natural language input.
* **OpenStack Client:** Acts as the intermediary, communicating with the OpenStack APIs using the `openstacksdk` to perform the requested cloud management tasks.
* **Database:** Stores a record of all user requests, the interpreted intent, and the outcome of the executed operations.

---

## Requirements

* **Python:** Version 3.7 or higher is required.
* **Python Libraries:** Ensure the following libraries are installed:
    ```bash
    pip install transformers torch flask requests openstacksdk
    ```

## Setup Instructions

Follow these steps to get ChatCloud up and running:

1.  **Clone the Repository:**
    ```bash
    git clone [(https://github.com/Devg1804/AgenticAI-Cloud-Infrastructure-Automation.git)]((https://github.com/Devg1804/AgenticAI-Cloud-Infrastructure-Automation.git))
    cd AgenticAI-Cloud-Infrastructure-Automation
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure OpenStack Credentials:**
    * Locate the `openstack_client.py` file within the repository.
    * Open this file and update the OpenStack connection parameters (e.g., `auth_url`, `project_name`, `username`, `password`) with your specific cloud credentials. This is crucial for the agent to authenticate and interact with your OpenStack environment.

## How to Run

To start the ChatCloud application, execute the following command in your terminal:

```bash
python app.py
