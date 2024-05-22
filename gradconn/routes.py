from gradconn import app, gradconn
from flask import render_template, request, url_for, redirect
from bson.objectid import ObjectId
from datetime import datetime


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/catagories/internships')
def internships():
    return render_template('internships.html')

@app.route('/catagories/fellowships')
def fellowships():
    return render_template('fellowships.html')

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
    return redirect(url_for('blog_posts'))

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
def blog_posts():
    all_blogs = gradconn.find()
    return render_template('blogs.html', all_blogs=all_blogs)

@app.route('/contact')
def contact():
    return render_template('contact.html')