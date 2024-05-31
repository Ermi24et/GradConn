# GradCon: Graduates Connect

`Python` `Flask` `Bootstrap` `Html` `CSS` `MongoDB`

- GradCon is a platform that bridges the gap between fresh graduates and organizations. It offers graduates opportunities to find internships, volunteer activities, and job opportunities. Simultaneously, it provides organizations with talented individuals who are good fit for the company.

![GradConn](https://github.com/Ermi24et/GradConn/blob/master/gradconn.png)

## Introduction

- GradConn is a web application designed to connect the gap between fresh graduates and potential employers.

## Key Features

- User and Admin(Employer) Sign-up/Sign-in
- Job Posting and Mangement that includes CRUD
- Job Search for Users
- Employee Search for Employers

## Installation

- To be able to test our GradConn web application you  need to install some packages and modules.

```
# clone our repository
$ git clone https://github.com/Ermi24et/GradConn.git
# get into the repository
$ cd GRADCONN
# create a virtual environment
$ python3 -m venv .venv
# activate your virtual environment
$ source .venv/bin/activate
# install necessary packages
$ pip install flask pymongo flask-wtf wtforms email_validator bcrypt
# start your mongodb
$ sudo service mongodb start
# start your flask server
$ flask run --debug
```

- Once you installed the required packages you start your flask server you can go to the link http://127.0.0.1:5000/

## Usage

- You can navigate to the different routes that are already defined on the home page

## Contributing

- If you want to contribute to our platform you are very welcomed. by contributing to our project we can accelerate the job search of fresh graduates and talent search of organizations.

## How To Contribute

### reporting bugs
If you encounter any bugs or issues while using our GradConn platform please [open an issue](https://github.com/Ermi24et/GradConn/issues) on GitHub. be sure to provide detailed information about the problem, including steps to reproduce it and any error messages you encountered.

### Contributing Code

- We welcome contributions in the form of code changes, bug fixes, or new features. To contribute code to the project, follow these steps:

1, Fork the repository on GitHub.
2, Clone your forked repository to your local machine.

```
git clone https://github.com/Ermi24et/GradConn.git
# create a new branch for your changes
git checkout -b feature-name
# make your changes and commit them to your branch
git add .
git commit -m "Add new feature or fix bug"
# push your changes to your fork on github
git push origin feature-name
# Open a pull request (PR) against the main branch of the original repository. Provide a clear title and description for your PR, explaining the changes you made.
```

### code style guidelines

When contributing code to the project, please follow these guidelines:

- Use consistent coding style and formatting.
- Write clear and descriptive commit messages.
- Write comments and documentation to explain complex code or algorithms.
- Test your changes thoroughly before submitting a pull request.

We appreciate your contributions and look forward to working together to improve our Online Learning Management System!

## Contributors:
**Ermiyas Teklehaymanot**: [Twitter](https://x.com/Ermi24et), [Linkedin](https://www.linkedin.com/in/ermi24et/)

**Selomon Teshome**: [Twitter](), [Linkedin]()