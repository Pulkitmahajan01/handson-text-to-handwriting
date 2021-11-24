# imports
# to activate virtual environment in windows & f:/allora/venv/Scripts/Activate.ps1
import os
import img2pdf
from os import name
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import magic
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            activator(os.path.join(
                app.config['UPLOAD_FOLDER'], filename), filename.rsplit('.', 1)[1].lower())
            createPDF()
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template("index.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory("", "output.pdf", as_attachment=True)


def activator(filePath, extension):
    magic.magicWand(filePath, extension)


def createPDF():
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert(
            [i for i in os.listdir('.') if i.endswith(".png")]))
    # deleting png files created
    filelist = [f for f in os.listdir('.') if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join('.', f))


if __name__ == "__main__":
    app.run(debug=True)
    #val = input("Enter file with extension:  ")
    #activator(val, val.rsplit('.', 1)[1].lower())
