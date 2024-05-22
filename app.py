from flask import Flask, render_template, request, url_for, redirect, flash
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super secret key"

client = MongoClient('localhost', 27017)

db = client.flask_db
gradconn = db.gradconn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog_form', methods=('GET', 'POST'))
def blogs_form():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        time = datetime.now().strftime('%Y-%m-%d %T %p')
        return redirect(url_for('blogs', title=title, content=content, time=time))
    
    return render_template('index.html')


@app.post('/<id>/delete/')
def delete(id):
    gradconn.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('all_blogs'))

@app.post('/<id>/update/')
def update(id):
    return redirect(url_for('update_blog', id=id))

@app.route('/blogs/updated/<id>', methods=('GET', 'POST'))
def update_blog(id):
    title = ""
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        time = datetime.now().strftime('%Y-%m-%d %T %p')
        return redirect(url_for('blogs', title=title, content=content, time=time))
    
    all_blogs = gradconn.find_one({"_id": ObjectId(id)})
    gradconn.delete_one({"_id": ObjectId(id)})

    return render_template('update_blog.html', all_blogs=all_blogs)

@app.route('/blogs/<title>/<content>/<time>')
def blogs(title, content, time):
    gradconn.insert_one({'title': title, 'content': content, 'time': time})
    all_blogs = gradconn.find()
    return render_template('blogs.html', all_blogs=all_blogs)

@app.route('/blog_posts')
def all_blogs():
    all_blogs = gradconn.find()
    return render_template('blogs.html', all_blogs=all_blogs)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
