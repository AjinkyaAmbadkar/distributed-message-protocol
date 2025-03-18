import requests

SERVER_URL = "http://localhost:5050"

def send_message():
    # JSON message to send
    message = {"type": "greeting", "content": "Hello, Server!"}
    try:
        print("Start of send_message()")
        print(f"Sending message: {message} to {SERVER_URL}")
        
        # Send the POST request
        response = requests.post(f"{SERVER_URL}/message", json=message)
        print("POST request sent successfully")
        
        print(f"Received response: {response.status_code}")
        print(f"Response content: {response.json()}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("End of send_message()")

def check_health():
    try:
        print("Checking health of the server")
        response = requests.get(f"{SERVER_URL}/health")
        print(response.json())
        print("GET request sent for health check")

    except Exception as e:
        print(f"Error occured! {str(e)}")


if __name__ == '__main__':
    print("Client script started")
    send_message()
    check_health()
    print("Client script finished")