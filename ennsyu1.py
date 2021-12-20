from flask import *
from werkzeug.utils import secure_filename
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

def detect_text_uri(save_path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    with open(save_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return texts

#-----ファイルのアップロード-----#
#GETの処理
@app.route('/up/', methods=['GET'])
def up_get():
    return render_template('up.html', message = '数式だけが載っている画像を送って下さい', flag = False)

def ansserch(textinfo):
    a = []
    texts = textinfo
    length = len(texts)
    for count in range(length):
        judge = texts[count].description.isdigit()
        #print(hanntei)    
        if judge == True:
            a.append( int(texts[count].description) )
    #print(a[0])    #print(a[1])
    for count in range(length):
        ennzann = texts[count].description
        if ( ennzann == "+") or (ennzann == "＋"):        
            r = int(a[0]) + int(a[1])
        elif (ennzann == "-") or (ennzann == "－"):
            r = int(a[0]) - int(a[1])
        elif (ennzann == "×") or (ennzann == "✕") or (ennzann == "*") or (ennzann == "x"):
            r = int(a[0]) * int(a[1]) 
        elif (ennzann == "÷") or (ennzann == "/") or (ennzann == "／"):
            r = int(a[0]) / int(a[1])
    return r        

#POSTの処理
@app.route('/up/', methods=['POST'])
def up_post():
# ファイルのリクエストパラメータを取得
    f = request.files.get('image')
# ファイル名を取得
    filename = secure_filename(f.filename)
# ファイルを保存するディレクトリを指定
    filepath = 'static/image/' + filename
# ファイルを保存する
    f.save(filepath)
    #return render_template('up.html', title = 'Form Sample(post)', message = 'アップロードされた画像({})'.format(filename), flag = True, image_name = filename)
    readinfo = detect_text_uri(filepath)
    ans = ansserch(readinfo)
    return "<h2>" + str(ans) + "</h2>"

# サーバーを起動
if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5555))
    #app.run(debug=True, port=os.environ['PORT'], host="0.0.0.0")
    app.run(port=5555, debug=True)
