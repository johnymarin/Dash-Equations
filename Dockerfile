FROM python:3.9.12

RUN apt-get update
RUN apt-get install nano

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the default port for the Dash application (8050)
EXPOSE 8050

# Set the default command to start the Dash application
#CMD ["python", "main.py"]
CMD gunicorn -b 0.0.0.0:8050 main:server