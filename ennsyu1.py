from flask import *

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <h2> 計算ページ </h2>
    <form action="/add" method="post">
      <input type="text" name="a"> +
      <input type="tepyxt" name="b">
      <input type="submit" value="足し算の結果">
    </form>
    <form action="/sub" method="post">
      <input type="text" name="a"> -
      <input type="text" name="b">
      <input type="submit" value="引き算の結果">
    </form>
    <form action="/mult" method="post">
      <input type="text" name="a"> *
      <input type="text" name="b">
      <input type="submit" value="掛け算の結果">
    </form>

    <form action="/div" method="post">
      <input type="text" name="a"> /
      <input type="text" name="b">
      <input type="submit" value="割り算の結果">
    </form>

    <form action="/power" method="post">
      <input type="text" name="a"> ^
      <input type="text" name="b">
      <input type="submit" value="べき乗の結果">
    </form>

   

    """

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
    app.run(debug=True, port=5555)