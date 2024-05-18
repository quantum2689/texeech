from flask import Flask,request,render_template,send_file
from gtts import gTTS
import os
import uuid

os.mkdir('Audio')
app = Flask(__name__,template_folder="template")
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'Audio')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Id= uuid.uuid4()
def audio(text,lang):
    speech = gTTS(text=text,lang=lang,slow=False,tld="com.au")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{Id}.mp3")
    speech.save(filepath)
    return filepath



@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        text = request.form["text"]
        filepath = audio(text,"en")
        return send_file(filepath,as_attachment=True)


    

app.run(host='0.0.0.0', port=5100,debug=True)
