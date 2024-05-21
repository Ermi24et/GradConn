from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
gradconn = db.gradconn

@app.route('/blogs', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        time = datetime.now().strftime('%Y-%m-%d %T %p')
        gradconn.insert_one({'title': title, 'content': content, 'time': time})
        return render_template('blogs.html', all_blogs=gradconn.find())
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
