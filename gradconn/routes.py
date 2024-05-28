from gradconn import app, gradconn, user_db, admin_db
from flask import render_template, request, url_for, redirect, flash
from bson.objectid import ObjectId
from datetime import datetime
from gradconn.forms import SignUpForm, SignInForm, AdminSignInForm, AdminSignUpForm
from flask_login import login_user, logout_user, login_required, current_user
from gradconn.utils import hash_password, check_password, check_name

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

@app.route('/admin/signup/', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignUpForm()
    if form.validate_on_submit():
        admin_email = {
            "email": form.email.data
        }
        existing_admin = admin_db.find_one(admin_email)
        if existing_admin:
            flash('This admin already exists please sign in!')
            return redirect(url_for('login'))
        
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = hash_password(password)
        admin_dict = {"name": name,
                     "email": email,
                     "password": hashed_password
                     }

        admin_db.insert_one(admin_dict)
        admin_data = admin_db.find()
        return render_template('admin_profile.html', admin_data=admin_data)
    return render_template('admin_register.html', form=form)

@app.route('/user/signin/', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_data = user_db.find_one({"email": email})

        if user_data and check_password(password, user_data['password']):
            print(password, user_data['password'])
            return render_template('user_profile.html', user_data=user_data)
        else:
            error_msg = "Invalid email or password."
            return render_template('signin.html', form=form, error_msg=error_msg)
    return render_template('signin.html', form=form)

@app.route('/admin/signin/', methods=['GET', 'POST'])
def admin_signin():
    form = AdminSignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        admin_data = admin_db.find_one({"email": email})

        if admin_data and check_password(password, admin_data['password']):
            return render_template('admin_profile.html', admin_data=admin_data)
        else:
            error_msg = "Admin user not found."
        return render_template('admin_signin.html', form=form, error_msg=error_msg)
    return render_template('admin_signin.html', form=form)


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

@app.route('/employer/dashboard/')
@login_required
def employer_dashboard():
    return render_template('employer_dashboard.html')

@app.route('/employer/post_job/', methods=['GET', 'POST'])
@login_required
def post_job():
    form = JobForm()
    if form.validate_on_submit():
        job_posting = {
            'position_title': form.position_title.data,
            'contract_type': form.contract_type.data,
            'working_codition': form.working_condition.data,
            'types_of_vacancy': form.types_of_vacancy.data,
            'organization_name': form.organization_name.data,
            'organization_description': form.organization_description.data,
            'job_description': form.job_description.data,
            'required_education_experience': form.required_education_experience.data,
            'skills': form.skills.data,
            'how_to_apply': form.how_to_apply.data,
            'disclaimer': form.disclaimer.data,
            'posted_data': datetime.utcnow(),
            'updated_date': datetime.utcnow(),
            'deadline_date': form.deadline_date.data,
            'applicants': []
        }
        job_db.insert_one(job_posting)
        flash('Job posting created successfully', 'success')
        return redirect(url_for('employer_dashboard'))
    return render_template('post_job.html', form=form)

@app.route('/employer/list_jobs/')
@login_required
def list_jobs():
    jobs = job_db.find({"organization_name": current_user.organization_name})
    return render_template('list_jobs.html', jobs=jobs)

@app.route('/employer/job/<job_id>/update/', methods=['GET', 'POST'])
@login_required
def update_job(job_id):
    job = job_db.find_one({'_id': ObjectId(job_id)})
    form = JobForm(obj=job)
    if form.validate_on_submit():
        update_job = {
            'position_title': form.position_title.data,
            'contract_type': form.contract_type.data,
            'working_condition': form.working_condition.data,
            'type_of-vacancy': form.type_of_vacancy.data,
            'organization_description': form.organization_description.data,
            'job_description': form.job_description.data,
            'required_education_experience': form.required_education_experience.data,
            'skills': form.skills.data,
            'how_to_apply': form.how_to_apply.data,
            'disclaimer': form.disclaimer.data,
            'updated-date': datetime.utcnow(),
            'deadline_date': form.deadline_date.data,
        }
        job_db.update_one({"_id": ObjectId(job_id)}, {'$set': updated_job})
        flash('Job updated successfully', 'success')
        return redirect(url_for('list_jobs'))
    return render_template('update_job.html', form=form, job_id=job_id)

@app.route('/employer/job/<job_id>/delete/', methods=['POST'])
@login_required
def delete_job(job_id):
    job_db.delete_one("_id": ObjectId(job_id)})
    flash('Job deleted successfully', 'success')
    return redirect(url_for('list_jobs'))

@app.route('/employer/job/<job_id>/applicants/')
@login_required
def view_applicants(job_id):
    job = job_db.find_one({"_id": ObjectId(job_id)})
    applicants = job.get('applicants', [])
    return return-template('view_applicants.html', job=job, applicants=applicants)

@app.route('/employer/job/<job_id>/applicant/<applicant_id>/')
@login_required
def view_applicant(job_id, applicant_id):
    job = job_db.find_one({"_id": ObjectId(job_id)})
    applicant = next((a for a in job['applicant'] if str(a['_id']) == applicant_id), None)
    if applicant:
        return render_template('view_applicant.html', job=job, applicant=applicant)
    flash('Applicant not found', 'error')
    return redirect(url_for('view_applicants', job_id=job_id))

@app.route('/employer/job/<job_id>/applicant/<applicant_id>/download/')
@login_required
def download_applicant(job_id, applicant_id):
    job = job_db.find_one({"_id": ObjectId(job_id)})
    applicant = next(( a for a in job['applicants'] if str(a['_id']) == applicant_id), None)
    if applicant:
        return jsonify(applicant)
    flash('Applicant not found', 'error')
    return redirect(url_for('view_applicants', job_id=job_id))

@app.route('/employer/job/<job_id>/applicant/<applicant_id>/status/', methods=['POST'])
@login_required
def update_applicant_status(job_id, applicant_id):
    job = job_db.find_one({"_id": ObjectId(job_id)})
    applicant = next(( a for a in job['applicants'] if str(a['_id']) == applicant_id), None)
    if applicant:
        status = request.form.get('status')
        for app in job['applicants']:
            if str(app('_id']) == applicant_id:
                app['status'] = status
        job_db.update_one({"_id": ObjectId(job_id)}, {'$set': {'applicants': job['applicants']}})
        flash('Applicant status updated successfully', 'success')
        return redirect(url_for('view_applicant', job_id=job_id, applicant_id=applicant_id))
    flash('Applicant not found', 'error')
    return redirect(url_for('view-applicants', job_id=job_id))

@app.route('/employer/search_employees/', methods=['GET', 'POST'])
@login_required
def search_employees():
    from = EmployeesSeacrhForm()
    employees = []
    if form.validate_on_submit():
        education = form.education.data
        skills = form.skills.data
        query = {}
        if education:
            query['education'] = {'$regex': education, '$options': 'i'}
        if skills:
            query['skills'] = {'$regex': skills, '$options': 'i'}
        employees = employee-db.find(query)
    return render_template('search_employees.html', form=form, employees=employees)

@app.route('employer/profile/')
@login_required
def employer_profile():
    profile_data = current_user
    return render_template('employer_profile.html', profile=profile_data)

@app.route('/employer/settings/', methods=['GET', 'POST'])
@login_required
def employer_settings():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm-password = request.form.get('confirm_password')
        if new_password and new_apassword == confirm_password:
            hashed_password = hash_password(new_password)
            user_db.update_one({'_id': current_user._id}, {'$set': {'password': hashed_password}})
            flasj('Password updated successfully', 'success')
        else:
            flash('Passwords do not match', 'danger')
    return render_template('employer_settings.html')


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