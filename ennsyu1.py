from flask import *
import os

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return render_template("calculator.html")

# フォームの値を受け取って結果を表示 --- (*3)
@app.route("/power", methods=["post"])
def power():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a ** b
    return "<h1>" +str(a) +"の"+str(b)+"乗は " + str(r) + "</h1>"    

@app.route("/add", methods=["post"])
def add():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a + b
    return "<h1>" +str(a) +"＋"+str(b)+" ＝ " + str(r) + "</h1>"    

@app.route("/sub", methods=["post"])
def sub():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a - b
    return "<h1>" +str(a) +"－"+str(b)+" ＝ " + str(r) + "</h1>" 

@app.route("/mult", methods=["post"])
def mult():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a * b
    return "<h1>" +str(a) +"×"+str(b)+" ＝ " + str(r) + "</h1>" 

@app.route("/div", methods=["post"])
def div():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    if (b==0):
        return "<h1>0では割れません</h1>" 
    

    r = a / b
    return "<h1>" +str(a) +"÷"+str(b)+" ＝ " + str(r) + "</h1>" 


# サーバーを起動
if __name__ == "__main__":
    
    #port = int(os.environ.get("PORT", 9761))
    app.run(debug=True, port=os.environ['PORT'], host="0.0.0.0")