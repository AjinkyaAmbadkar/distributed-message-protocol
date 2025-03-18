import requests

# Update the server's address (change to Pod-0 address)
SERVER_URL = "http://ajambadk-sset-0.dms-service.default.svc.cluster.local:6060"

def send_message():
    message = {"type": "greeting", "content": "Hello from Client!"}
    response = requests.post(f"{SERVER_URL}/message", json=message)
    print("Response:", response.json())

def check_health():
    response = requests.get(f"{SERVER_URL}/health")
    print("Health Check:", response.json())

if __name__ == '__main__':
    send_message()
    check_health()
