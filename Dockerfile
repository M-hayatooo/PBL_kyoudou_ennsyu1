FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

# アプリのコードを clone してくる
RUN git clone https://github.com/M-hayatooo/web_app.git myapp

WORKDIR /myapp

RUN pip install --upgrade pip 
RUN pip install flask

# # アプリを起動する
ENV FLASK_APP ennsyu1.py
#CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "9761" ]
CMD [ "python", "ennsyu1.py" ]