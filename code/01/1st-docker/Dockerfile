# 1. Base Image: Use the official Python 3.11 Slim version
FROM python:3.11-slim

# 2. Set Working Directory: Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy Dependency File: Copy requirements.txt to the working directory
COPY requirements.txt .

# 4. Install Dependencies: Install all packages listed in requirements.txt using pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code: Copy the local app.py file to the container's /app directory
COPY app.py .

# 6. Expose Port: Inform Docker that the application inside the container will use port 5000
EXPOSE 5000

# 7. Start Command: Define the command to execute when the container starts
# The ['python', 'app.py'] command will start the Flask application
CMD ["python", "app.py"]