from flask import Flask, render_template, request 
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from VideoToAudio import main
from pathlib import Path
from Transcript import Transcript

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files/mp4'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])

@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        fileName = secure_filename(file.filename)
        fileValue = Path(fileName).stem
        btnConvert = "<button>convert to mp3</button>"
        src = os.path.abspath("static/files/mp4/" + fileName)
        #src = "/home/gaston/Desktop/Whisper_App/UPLOAD_FILE/Flask-File-Uploads/static/files/mp4/"+fileName
        return render_template('index.html', form=form, fileName= fileName, btnConvert=btnConvert, src= src, fileValue= fileValue)
    return render_template('index.html', form=form)

class WhisForm(FlaskForm):
    fileWhis = FileField("File")
    submitWhis = SubmitField("WHIS")


@app.route('/convert', methods = ['POST', 'GET'])
def convert():
    form= WhisForm()
    
    output = request.form.to_dict()
    source = output['srcConvert']
    nameMp3 = output['srcFileName']+ '.mp3'
    
    mp3 = os.path.abspath(nameMp3)
    main(source, nameMp3)
    return render_template('index2.html', form=form, mp3=mp3)


@app.route('/whisper', methods = ['POST','GET'])
def whisperAudio():
    output = request.form.to_dict()
    audio = output['mp3']

    text= Transcript.get_transcript(audio = audio)
    result= "The result is: " + text
    return result
    #return render_template('index2.html', text=text)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

#/home/gaston/Desktop/Whisper_App/UPLOAD_FILE/Flask-File-Uploads/static/files/Clase_N1.mp4