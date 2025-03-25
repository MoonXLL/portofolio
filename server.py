from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_website():
    return render_template('index.html')  

@app.route('/<string:pagename>')
def home(pagename):
    return render_template(pagename) 

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n EMAIL : {email}, SUBJECT : {subject}, MESSAGE : {message}')

def write_to_csv(data):
    with open('database2.csv', mode = 'a', newline = '') as database2:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",",  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writeheader()
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return ' something went wrong'






    

