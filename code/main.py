from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
import json
from object_size import ip

#print ip('pictures/j2.jpg',2.2)

UPLOAD_FOLDER =  '/home/rratcliffe/github/Standardize-The-Size/code/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

gfilename = ''

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global gfilename
    if request.method == 'POST':
        # check if the post request has the file part
        for items in request.files:
            print items
            print "z"
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return "Filename empty"
            #flash('No selected file')
            return redirect(request.url)
        #if file and allowed_file(file.filename):
        if file:
            filename = secure_filename(file.filename)
            gfilename = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print filename
            x=[ip("uploads/"+filename,2.2,'height'),ip("uploads/"+filename,2.2,'width')]
            print x
            return str(x)


            #return redirect(url_for('uploaded_file',
                                    #filename=filename))
           # return render_template("index.html")

    return render_template("index.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                               filename)

@app.route('/scan',methods=['GET'])
def scan():
    global gfilename
    test=ProcessImage()
    result=test.process_image('../uploads/' + gfilename)
    result = json.loads(result)
    #print result
    result=result['images'][0]['text']
   
    #print result
    date=test.get_dates(result)
    print ("fix_erro3")
    event_json=test.make_json(date,result)
    google=Google()
    print ("fix_erro2")
    triggered= google.add(event_json)
    print "wtf"

    return triggered
    
    

@app.route('/enter', methods=['POST'])
def sample():
    #return "Enter function"
    print str(request.data)
    return request.data


if __name__ == "__main__":
    app.run(debug=True)
