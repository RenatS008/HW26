FROM python:3.10-slim

#ENV Home /app
WORKDIR /code

COPY requirements.txt .
#RUN python3 -m pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#ENTRYPOINT ["sh", "entrypoint.sh"]
CMD flask run -h 0.0.0.0 -p 80