from gradconn import app, gradconn, user_db
from flask import render_template, request, url_for, redirect, flash
from bson.objectid import ObjectId
from datetime import datetime
from gradconn.forms import SignUpForm, SignInForm
from flask_login import login_user, logout_user, login_required, current_user
from gradconn.utils import hash_password, check_password

@app.route('/user/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user_email = {
            "email": form.email.data
        }
        existing_user = user_db.find_one(user_email)
        if existing_user:
            flash('This user already exists please sign in!')
            return redirect(url_for('login'))
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        hashed_password = hash_password(password)
        user_dict = {"first_name": first_name,
                     "last_name": last_name,
                     "email": email,
                     "password": hashed_password
                     }

        user_db.insert_one(user_dict)
        user_data = user_db.find()
        return render_template('user_profile.html', user_data=user_data)

    return render_template('register.html', form=form)

@app.route('/user/signin/', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_data = user_db.find_one({"email": email})

        if user_data and check_password(password, user_data['password']):
            return render_template('user_profile.html', user_data=user_data)
        else:
            error_msg = "Invalid email or password."
            return render_template('signin.html', form=form, error_msg=error_msg)
    return render_template('signin.html', form=form)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/category/internships/')
def internships():
    return render_template('internships.html')

@app.route('/category/fellowships/')
def fellowships():
    return render_template('fellowships.html')

@app.route('/category/volunteer/')
def volunteer():
    return render_template('volunteer.html')

@app.route('/blog_form/', methods=('GET', 'POST'))
def blogs_form():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        time = datetime.now().strftime('%Y-%m-%d %T %p')
        return redirect(url_for('blogs', title=title, content=content, time=time))
    
    return render_template('blog_form.html')


@app.post('/<id>/delete/')
def delete(id):
    gradconn.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('blog_posts'))

@app.post('/<id>/update/')
def update(id):
    return redirect(url_for('update_blog', id=id))

@app.route('/blogs/updated/<id>/', methods=('GET', 'POST'))
def update_blog(id):
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        time = datetime.now().strftime('%Y-%m-%d %T %p')
        return redirect(url_for('blogs', title=title, content=content, time=time))
    
    all_blogs = gradconn.find_one({"_id": ObjectId(id)})
    gradconn.delete_one({"_id": ObjectId(id)})

    return render_template('update_blog.html', all_blogs=all_blogs)

@app.route('/blogs/<title>/<content>/<time>/')
def blogs(title, content, time):
    gradconn.insert_one({'title': title, 'content': content, 'time': time})
    all_blogs = gradconn.find()
    return render_template('blogs.html', all_blogs=all_blogs)

@app.route('/blog_posts/')
def blog_posts():
    all_blogs = gradconn.find()
    return render_template('blogs.html', all_blogs=all_blogs)

@app.route('/contact/')
def contact():
    return render_template('contact.html')