FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

# アプリのコードを clone してくる
RUN git clone https://github.com/Lfu001/PBL-Test.git myapp

WORKDIR /myapp

RUN pip3 install flask pandas

# # アプリを起動する
ENV FLASK_APP server.py
#CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "9761" ]
CMD [ "python", "ennsyu1.py" ]