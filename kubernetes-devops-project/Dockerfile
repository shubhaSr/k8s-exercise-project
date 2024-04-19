FROM python:3.8.10
 
WORKDIR /app
COPY . /app
 
RUN python -m pip install pip==20.0.2
RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
