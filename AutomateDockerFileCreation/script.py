import docker

# Connect to Docker daemon
client = docker.from_env()

# Define the base image
base_image = 'python:3.8-slim'

# Define the Dockerfile commands
dockerfile = """
FROM {base_image}
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
"""

# Build the image using the Dockerfile
image, logs = client.images.build(
    fileobj=io.BytesIO(dockerfile.encode('utf-8')),
    tag='my-image',
    rm=True
)

# Push the image to a Docker registry
client.images.push('my-image')
