import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

# @app.route("/<username>/<int:year_id>")
# def hello_world(username=None,year_id=None):
#     return render_template('index.html', name=username, year=year_id)
@app.route("/")
def home():
    """index page"""
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    """other pages"""
    return render_template(f'{page_name}.html')

def write_to_file(data):
    """write txt"""
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    """write csv"""
    with open('database.csv', 'a', newline='') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    """contact form submit"""
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return 'Something went wrong, try again'
    else:
        return 'Something went wrong, try again'

