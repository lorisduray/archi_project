FROM python:3.10.6
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Expose the port that your FastAPI application will run on
EXPOSE 8080
# Command to run the FastAPI application using Uvicorn
CMD uvicorn backend.archi_style.API.fast:app --host 0.0.0.0 --port 8080 --reload
