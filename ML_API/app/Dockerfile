FROM python:3.12-slim

WORKDIR /app

# upgrade pip and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# copy all necessary files
COPY model.json .
COPY main.py .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]