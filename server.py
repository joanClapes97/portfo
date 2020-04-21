from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# pythonanywhere user: joancl

@app.route('/') # my home directory
def my_home():
  return render_template('index.html')

@app.route('/<string:page_name>')   #everything works dynamically
def html_page(page_name):
  return render_template(page_name)

def write_to_file(data):
    """ database.txt contains info about who has contacted me
    and it persists in my laptop memory """
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
    """ database.csv contains info about who has contacted me
    and it persists in my laptop memory """
    with open('database2.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database!'
    else:
        return 'something went wrong, try again!!'
