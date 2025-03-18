
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y procps lsof


COPY src/server.py .

RUN pip install flask

# Expose the server port
EXPOSE 5050

# Run the server
CMD ["python", "server.py"]

