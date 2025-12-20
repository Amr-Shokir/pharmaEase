# 1. Use a lightweight version of Python
FROM python:3.13-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy requirements first (to cache dependencies efficiently)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Tell Docker we are using port 5000
EXPOSE 5000

# 7. The command to run your app
CMD ["python", "run.py"]