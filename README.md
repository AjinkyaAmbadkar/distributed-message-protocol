Simple Protocol Exchange

**Project Overview**
As Part of Assignment 1 to build simple messeging protocol I have used python as programming language and HTTP for interaction between client and server. I had previously worked on HTTP protocols like GET, POST while I was working as software engineer. So,  went for HTTP and Json() for same reason.

**Project Structure**
The Project structure is as below:
SIMPLE-PROTOCOL-EXCHANGE
|
|___docker
|    |
|    |____Dockerfile
|
|___k8s
|   |_____server-deployment.yaml
|   |_____server-service.yaml
|
|___src
|   |
|   |____client.py
|   |____server.py
|
|___virtual --(This is for the virtual environment which I have created to install the libraries for client and server interaction)

**Code details**
1. In src I have created clinet and server two python files. As name suggests client is used to send the HTTP request to the server. I have used HTTP POST to publish message on server and GET to check the health of the server. 

client.py
    def send_message(): this method is for sending the POST request to the server and we are also sending the payload with the request. Written code in try and except block so that if any error occurs our program would not terminate instead we will be seeing errors in catch block and some debug meassages.

    def check_health(): As i have seen in real world projects there are health check endpoint which are exposed and we can check them to test if service is up and running by hitting the endpoint via swagger, So, I have kept this endpoint. Which will be helpful in upcomming assignments as we are using this as a base.

    from main method I have just called both methods.

server.py
    def handle_message(): This is the method to handel the HTTP request which will come from "http://localhost:5050/message" endpoint and it should be POST request. Then this method serve that perticular request with response code of 200.

    def check_health(): This method is to handel the HTTP request which will come from "http://localhost:5050/health" endpoint and it should be GET request. This will return status as Status : Running. with HTTP response 200.

As Initially I have testes this code as I have created virtual environment as you can see in folder structure. Then installed the flask requirements.

Commands as follows:

**Code Testing on virtual Env**

to create and activate virtual env:
    python3 -m venv virtual
    source virtual/bin/activate

to install flask requirements:
    pip install flask requests

then I run the server.py file in terminal and keep that terminal open.
    python src/server.py

after it is running I run the client.py file in another and I am getting the response from server.py 
    python src/client.py

Now I started setting up docker. I went through the minikube as Professor is using it and if I run through any blocker it might be easily debugged if I need any help in future.

-----------------------------------------------------------------------------------------------------------------------------------
**Docker Steps**
docker --> Dockerfile

Mentioned all the instruction for building the docker images. All instructions are same across the environment so that the image we will build be same across all the platform


# Install curl as it is not installed previously so i have to debug the issue so mentioning the step.
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* 

# Copy the server code to the container
COPY src/server.py .

# Install Flask
RUN pip install flask

# Expose the server port
EXPOSE 5050

# Run the server
CMD ["python", "server.py"]


command for building the image:

eval $(minikube docker-env)
docker build -t simple-protocol-exchange:latest -f docker/Dockerfile .
-----------------------------------------------------------------------------------------------------------------------------------
**YAML File details**
k8s --> server.deployment.yaml

This file contains information that how our appliaction should be deployed on kubernetes. Like in specification we can see the name of the server, image and which port is used.

server-service.yaml

This file contains infromation about the how our application is exposed to the outside world and within the kubernetes.

steps :
to deploy this yaml files on kubernetes

kubectl apply -f k8s/server-deployment.yaml
kubectl apply -f k8s/server-service.yaml

to get url :

minikube service server-service --url

I have faced issue while working on docker as Image which I was trying to upload was giving me image_pull error as it was not able to deploy correctly so i have tried to redeploy it and checked the name in yaml files just to confirm and checked port number as well. 

-----------------------------------------------------------------------------------------------------------------------------------
**CURLS for Testing**
CURL to test:
curl -X POST http://<MINIKUBE_IP>:<NODE_PORT>/message -H "Content-Type: application/json" -d '{"type": "greeting", "content": "Hello, Server!"}'

curl http://<MINIKUBE_IP>:<NODE_PORT>/health

-----------------------------------------------------------------------------------------------------------------------------------
                                                    Assignment 2
-----------------------------------------------------------------------------------------------------------------------------------

The goal of the Assignment is as follows:

1. Opening a shell into a running Kubernetes pod.
2. Copying a simple server (server.py) into the container.
3. Running the server inside the container.
4. Exposing the server to the outside world using port forwarding.
5. Testing the server using curl.
This builds upon Assignment 1, where we created a simple message exchange protocol using Python's Flask framework and deployed it using Docker and Minikube.

In Assignment 1 I have done till step 4 as I have already copied the server.file inside the container. I was able to run it properly too. The one issue I was facing is that the port 5050 which i have used was already occupied as I have deployed the image on minikube and that was running. 

I checked that by using *docker ps* command and stop the execution of particular image on docker.

Then As mentioned in the last step I exposed my server to the outside world using the port forwarding.

kubectl port-forward pod/server-deployment-db495c9-xqxhl 8000:5050

Terminal Output:
(base) ajinkyaambadkar@Ajinkyas-MacBook-Pro-6 ~ % kubectl port-forward pod/server-deployment-db495c9-xqxhl 8000:5050
Forwarding from 127.0.0.1:8000 -> 5050
Forwarding from [::1]:8000 -> 5050
Handling connection for 8000

I opened new terminal tab and then hit the curl for checking the health and other endpoint which I had exposed in server.py file
I am getting below output with forwareded port as well:

(base) ajinkyaambadkar@Ajinkyas-MacBook-Pro-6 ~ % curl http://127.0.0.1:8000/health

{"status":"Running"}
(base) ajinkyaambadkar@Ajinkyas-MacBook-Pro-6 ~ % curl -X POST http://127.0.0.1:8000/message -H "Content-Type: application/json" -d '{"type": "greeting", "content": "Hello, Server!"}'

{"message":"Message received!","status":"success"}
(base) ajinkyaambadkar@Ajinkyas-MacBook-Pro-6 ~ % 


Both the result are as expected.

-----------------------------------------------------------------------------------------------------------------------------------