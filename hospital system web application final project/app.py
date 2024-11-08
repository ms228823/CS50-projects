import os
from datetime import date
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///hospital.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not (username := request.form.get("username")):
            warning = 1
            return render_template("login.html",warning = warning,)
        
        # Ensure password was submitted
        elif not (password := request.form.get("password")):
            warning = 2
            return render_template("login.html",warning = warning,)
        
        # Query database for username
<<<<<<< HEAD
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
=======
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?;", request.form.get("username")
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            warning = 3
            return render_template("login.html",warning = warning,)

        # Remember which user has logged in
        
        session["user_id"] =  rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        return render_template("login.html")

@app.route("/")
@login_required
def index():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # if status is not "Working"
<<<<<<< HEAD
    if(status[0]["status"] != "Working"):
        # return to tmplate role,status,name
        return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],status = status[0]["status"])

    return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],status = status[0]["status"])
=======
    if employee_info[0]["status"] != "Working":
        # return to template role,status,name
        return render_template(
            "index.html",
            employee_info=employee_info,
        )

    return render_template(
        "index.html",
        employee_info=employee_info,
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0


@app.route("/patientregisteration", methods=["GET", "POST"])
@login_required
def patient_registeration():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # Titles values allowed
    titles = ["Mr.","Miss.","Ms."]
    #  genders values allowed
    genders = ["Male","Female"]
    #  countries values allowed
    countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
    # get phone2 from form
    phone2 = request.form.get("phone2")
    # get patient middle name from form
    
    middle_name = request.form.get("middle_name")
    # get emergency contact address from form
    emergency_contact_address =request.form.get("emergency_contact_address")
    # get email from form
<<<<<<< HEAD
    email = request.form.get("email")    

    
    if(status[0]["status"] != "Working"):
        # return to tmplate role,status,name
        return render_template("patient_registeration.html",role = role[0]["role"],name = name[0]["first_name"], countries = countries, titles = titles ,genders = genders,status = status[0]["status"],)
=======
    email = request.form.get("email")
    # if user is working
    # if (employee_info[0]["status"] == "Working"):
    #     # return to template role,status,name
    #     return render_template(
    #         "patient_registeration.html",
    #         countries=countries,
    #         titles=titles,
    #         genders=genders,
    #         employee_info = employee_info,
    #     )
    # if user is not working
    if employee_info[0]["status"] != "Working":
        # return to template role,status,name
        return render_template(
            "patient_registeration.html",
            countries=countries,
            titles=titles,
            genders=genders,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure title was submitted
    if not (title := request.form.get("title")):
        warning = 1
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders, countries = countries, titles = titles,status = status[0]["status"],)
    
    # Ensure first_name was submitted
    elif not (first_name := request.form.get("first_name")):
        warning = 2
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )

    # Ensure first_name was submitted
    elif not (first_name := request.form.get("first_name")):
        warning = 2
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure last_name was submitted
    elif not (last_name := request.form.get("last_name")):
        warning = 3
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure genders was submitted
    elif not (gender_get := request.form.get("gender")):
        warning = 4
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
    
    # Ensure nationality was submitted
    elif not (nationality := request.form.get("nationality")):
        warning = 6
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )

    # Ensure nationality was submitted
    elif not (nationality := request.form.get("nationality")):
        warning = 6
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure id was submitted
    elif not (id := request.form.get("id")):
        warning = 7
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure street was submitted
    elif not (street := request.form.get("street")):
        warning = 8
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure phone1 was submitted
    elif not (phone1 := request.form.get("phone1")):
        warning = 9
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure your_email was submitted
    elif not (your_email := request.form.get("your_email")):
        warning = 10
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
    
    # Ensure emergency_contact_name was submitted
    elif not (emergency_contact_name := request.form.get("emergency_contact_name")):
        warning = 11
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )

    # Ensure emergency_contact_name was submitted
    elif not (emergency_contact_name := request.form.get("emergency_contact_name")):
        warning = 11
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure emergency_contact_relation was submitted
    elif not (emergency_contact_relation := request.form.get("emergency_contact_relation")):
        warning = 12
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Ensure emergency_contact_phone was submitted
    elif not (emergency_contact_phone := request.form.get("emergency_contact_phone")):
        warning = 13
<<<<<<< HEAD
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
    # # Ensure birth_date was submitted
    elif not (birth_date := request.form.get("birth_date")):
        warning = 14
        return render_template("patient_registeration.html",warning = warning,role = role[0]["role"], genders = genders ,countries = countries, titles = titles,status = status[0]["status"],)
=======
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
    # # Ensure birth_date was submitted
    elif not (birth_date := request.form.get("birth_date")):
        warning = 14
        return render_template(
            "patient_registeration.html",
            warning=warning,
            genders=genders,
            countries=countries,
            titles=titles,
            employee_info=employee_info,
        )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # birthdate group
    # get birthdate from website
    birth_date = datetime.datetime.strptime(request.form.get("birth_date"),"%Y-%m-%d")
    # birthdate day
    birth_date_day = birth_date.day
    # birthdate month
    birth_date_month = birth_date.month
    # birthdate year
    birth_date_year = birth_date.year
    # calculate age ***   
    # def age(birthdate):
    today = date.today()
    # calculating age
    age = today.year - birth_date_year - ((today.month, today.day) < (birth_date_month, birth_date_day))
    

    # inserting data into patient table
    db.execute("""INSERT INTO patient(first_name, middle_name, last_name,
                                  birth_date, age, gender, user_id,
                                  phone1, phone2,
                                  emergency_contact_name, emergency_contact_relation,
                                  emergency_contact_phone,
                                  emergency_contact_address, Email,Patient_reservation_status)
<<<<<<< HEAD
                                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                  first_name, middle_name, last_name,
                                  birth_date, age, gender_get,
                                  session["user_id"], phone1, phone2,
                                  emergency_contact_name, emergency_contact_relation, emergency_contact_phone,
                                  emergency_contact_address, email,"wait for a room")

    sucessed = 1
    # return to main tempalte after sucsessful patient regestration
    return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],sucessed = sucessed,status = status[0]["status"],)
    

=======
                                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
        first_name,
        middle_name,
        last_name,
        birth_date,
        age,
        gender_get,
        session["user_id"],
        phone1,
        phone2,
        emergency_contact_name,
        emergency_contact_relation,
        emergency_contact_phone,
        emergency_contact_address,
        email,
        "wait for a room",
    )

    sucessed = 1
    # return to main template after successful patient registration
    return render_template(
        "index.html",
        sucessed=sucessed,
        employee_info=employee_info,
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0


@app.route("/printreport", methods=["GET", "POST"])
@login_required
def printreport():
<<<<<<< HEAD
    # get employee's role from database
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    # get employee's status from database 
    name = db.execute("""SELECT users.first_name,users.middle_name,users.last_name FROM users JOIN action_report ON
                                users.id = action_report.user_id ;""")
    # get status from database
    status = db.execute("SELECT status FROM users WHERE id = ?", session["user_id"])

    # if status is not "Working"
    if(status[0]["status"] != "Working"):
        # return to tmplate role,status,name
        return render_template("emplyoeereport.html",role = role[0]["role"],name = name[0]["first_name"],status = status[0]["status"],)

    actions_of_employees = db.execute("""SELECT users.first_name AS first_name,users.middle_name As middle_name,users.last_name AS last_name,
                                   users.role AS role,action_report.action AS action,action_report.user_id AS user_id, 
                                   action_report.number_of_reservations AS number_of_reservations, action_report.Actions_notes_of_employee AS actions_notes_of_employee
                                   FROM action_report JOIN users ON users.id = action_report.user_id ;""")
    return render_template("emplyoeereport.html",role = role[0]["role"],actions_of_employees = actions_of_employees,name = name[0]["first_name"],status = status[0]["status"],)
=======
    # # get employee's status from database
    # name = db.execute(
    #     """SELECT users.first_name,users.middle_name,users.last_name FROM users JOIN action_report ON
    #                             users.id = action_report.user_id ;"""
    # )
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # if status is not "Working"
    if employee_info[0]["status"] != "Working":
        # return to template role,status,name
        return render_template(
            "emplyoeereport.html",
            employee_info=employee_info,
        )

    actions_of_employees = db.execute(
        """SELECT users.first_name AS first_name,
                  users.middle_name As middle_name,
                  users.last_name AS last_name,
                  users.status As status,
                  users.role AS role,
                  action_report.action AS action,
                  action_report.user_id AS user_id,
                  action_report.number_of_reservations AS number_of_reservations,
                  action_report.Actions_notes_of_employee AS actions_notes_of_employee
                  FROM action_report JOIN users ON users.id = action_report.user_id ;"""
    )
    return render_template(
        "emplyoeereport.html",
        actions_of_employees=actions_of_employees,
        employee_info=employee_info,
    )

>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

@app.route("/checkrooms", methods=["GET", "POST"])
@login_required
def checkrooms():
<<<<<<< HEAD
    # get role and status
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    # get employees name
    name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
    # get status from database
    status = db.execute("SELECT status FROM users WHERE id = ?", session["user_id"]) 
    # if status is not "Working"
    if(status[0]["status"] != "Working"):
        # return to tmplate role,status,name
        return render_template("checkrooms.html",role = role[0]["role"],name = name[0]["first_name"],status = status[0]["status"])
    # select rooms data from database
    rooms_data = db.execute("SELECT room_number,status,price FROM rooms;")
    # return data got from database to check rooms template
    return render_template("checkrooms.html",role = role[0]["role"],rooms_data = rooms_data,name = name[0]["first_name"],status = status[0]["status"])
=======
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # if status is not "Working"
    if employee_info[0]["status"] != "Working":
        # return to template role,status,name
        return render_template(
            "checkrooms.html",
            employee_info=employee_info,
        )
    # select rooms data from database
    rooms_data = db.execute("SELECT room_number,status,price FROM rooms;")
    # return data got from database to check rooms template
    return render_template(
        "checkrooms.html",
        rooms_data=rooms_data,
        employee_info=employee_info,
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/checkin", methods=["GET", "POST"])
@login_required
def checkin():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # rooms_data data from database
<<<<<<< HEAD
    rooms_data = db.execute("SELECT * FROM rooms WHERE status = ?;","open")
    # get status from database
    status = db.execute("SELECT status FROM users WHERE id = ?", session["user_id"])
=======
    rooms_data = db.execute("SELECT * FROM rooms WHERE status = ?;", "open")
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
    # rooms options
    rooms = {
        101: [101, 1000],
        102: [102, 1500],
        103: [103, 2000],
        104: [104, 2500],
        201: [201.3000],
        202: [202, 3500],
        203: [203, 4000],
        204: [204, 4500],
        301: [301, 5000],
        302: [302, 5500],
    }
    # patients data from database
    patients_data = db.execute("SELECT id,first_name,middle_name,last_name FROM patient WHERE Patient_reservation_status = ?;",
                               "wait for a room")

    today_date = date.today()
    # payment values allowed
<<<<<<< HEAD
    payment_values = ["Cash","Visa ,Mastercard"]

    # if status is not "Working"
    if(status[0]["status"] != "Working"):
        # return to tmplate role,status,name
        return render_template("checkin.html",role = role[0]["role"],name = name[0]["first_name"],payment_values = payment_values,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"])

    # if room no is null 
    if not (room_no := request.form.get("patient")):
        warning = 1
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"], payment_values = payment_values, warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    
    # if patient is null
    elif not (patient := request.form.get("patient")):
        warning = 2
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"],payment_values = payment_values,warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    # if patient is null
    if not (room := request.form.get("room")):
        warning = 3
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"],payment_values = payment_values,warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    # if checkin_date is null
    elif not (checkin_date := request.form.get("checkin_date")):
        warning = 4
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"],payment_values = payment_values,warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    # if checkout_date is null
    elif not (checkout_date := request.form.get("checkout_date")):
        warning = 5
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"],payment_values = payment_values,warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    # if payment is null
    elif not (payment := request.form.get("payment")):
        warning = 6
        return render_template("checkin.html",role = role[0]["role"] ,name = name[0]["first_name"],payment_values = payment_values,warning = warning,today_date = today_date,patients_data = patients_data,rooms_data = rooms_data,status = status[0]["status"],)
    
    # dates of check in and check out 
=======
    payment_values = ["Cash", "Visa ,Mastercard"]
    # if status is  "Working"
    # if (employee_info[0]["status"] == "Working"):
    #     # return to tmplate role,status,name
    #     return render_template(
    #         "checkin.html",
    #         payment_values=payment_values,
    #         today_date=today_date,
    #         patients_data=patients_data,
    #         rooms_data=rooms_data,
    #         employee_info = employee_info,
    #     )
    # if status is not "Working"
    if employee_info[0]["status"] != "Working":
        # return to tmplate role,status,name
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )

    # if room no is null
    if not (room_no := request.form.get("room")):
        warning = 1
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )

    # if patient is null
    elif not (patient := request.form.get("patient")):
        warning = 2
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )
    # if room is null
    if not (room := request.form.get("room")):
        warning = 3
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )
    # if checkin_date is null
    elif not (checkin_date := request.form.get("checkin_date")):
        warning = 4
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )
    # if checkout_date is null
    elif not (checkout_date := request.form.get("checkout_date")):
        warning = 5
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )
    # if payment is null
    elif not (payment := request.form.get("payment")):
        warning = 6
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )
    # if room is not in rooms
    elif not (room not in rooms):
        warning = 7
        return render_template(
            "checkin.html",
            payment_values=payment_values,
            warning=warning,
            today_date=today_date,
            patients_data=patients_data,
            rooms_data=rooms_data,
            employee_info=employee_info,
        )

    # dates of check in and check out
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
    # check in group
    # get check in from website
    checkin_date = datetime.datetime.strptime(request.form.get("checkin_date"),"%Y-%m-%d")
    # checkin_date = datetime.datetime.strptime(request.form.get("checkin_date"),"%Y-%m-%d")

    # check in day
    checkin_day = checkin_date.day
    # check in month
    checkin_month = checkin_date.month
    # check in year
    checkin_year = checkin_date.year
    # check out group
    # get check out from website
    
    checkout_date = datetime.datetime.strptime(request.form.get("checkout_date"),"%Y-%m-%d")
    # check out day
    checkout_day = checkout_date.day
    # check out month
    checkout_month = checkout_date.month
    # check out year
    checkout_year = checkout_date.year
    # calculate days of reservation
    # subtract checkin and check out dates
    delta = checkout_date - checkin_date
    # # days of reservation
    days_of_reservations = delta.days    
    
    #
<<<<<<< HEAD
    #  Select price of room choosen
    price_of_room = db.execute("SELECT price FROM rooms WHERE room_number = ? and status = ?;",room,"open")
=======
    #  Select price of room chosen
    price_of_room = db.execute(
        "SELECT price FROM rooms WHERE room_number = ? and status = ?;", room, "open"
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
    # multiply price with days
    total_price = price_of_room[0]["price"] * days_of_reservations
    # select patient id selected
    # patient_id = db.execute("SELECT id FROM patient WHERE id = ?;",
    #                         patient[0]["id"])

    # select id of room selected
    room_id = db.execute("SELECT id FROM rooms WHERE room_number = ? ;",room)
    # insert reservation information --error
    db.execute("""INSERT INTO reservations(roomid, user_id,patient_id, price,
                                           checkin, checkout, days,
                                           reservation_status, payment)
                                           VALUES (?,?,?,?,?,?,?,?,?);""",
                                           room_id[0]["id"],session["user_id"],patient,total_price,
                                           checkin_date,checkout_date,days_of_reservations,
                                           "Done",payment)
    # db.execute("""INSERT INTO reservations(roomid,user_id,price,
    #                                        checkin,checkout,days,reservation_status,payment)
    #                               VALUES (?,?,?,?,?,?,?,?)""",
    #                               room_id,session["user_id"],total_price,checkin_date,checkout_date,days_of_reservations,"Done",payment)
    # update status of room to be "reserved"
    db.execute("""UPDATE rooms SET
                  status = ? WHERE id = ?;
    ""","reserved",patient)
    # update status of room to be "reserved"
    db.execute("""UPDATE patient SET
                  Patient_reservation_status = ? WHERE id = ?;
    ""","checked in",patient)
    
    # get number of reservations of user
<<<<<<< HEAD
    number_of_reservation_get = db.execute("SELECT number_of_reservations FROM action_report WHERE user_id = ?",session["user_id"])
=======
    number_of_reservation_get = db.execute(
        "SELECT number_of_reservations FROM action_report WHERE user_id = ?;",
        session["user_id"],
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
    # add one to number of reservations of user
    number_of_reservations_sent = number_of_reservation_get[0]["number_of_reservations"] + 1
    # update the number of reservations to the new one
    db.execute("""UPDATE action_report SET
                  number_of_reservations = ? WHERE user_id = ?;
    """,number_of_reservations_sent,session["user_id"])

    # make condition to return if check in sucessed
    sucessed = 1
<<<<<<< HEAD
    # return to main after sucessful check in
    return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],sucessed = sucessed,status = status[0]["status"],)
=======
    # return to main after successful check in
    return render_template(
        "index.html",
        sucessed=sucessed,
        employee_info=employee_info,
    )

>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # get reservation's data
    reservation_data = db.execute(
        """SELECT
                                  reservations.id AS id,
                                  reservations.checkin AS checkin,
                                  reservations.checkout AS checkout,
                                  patient.first_name AS pateint_first_name ,
                                  patient.middle_name AS pateint_middle_name ,
                                  patient.last_name AS pateint_last_name
                                  FROM reservations
                                  JOIN patient ON patient.id = reservations.patient_id
                                  WHERE exit_date IS NULL
                                ;"""
    )

    # if status is not "Working"
    # if(employee_info[0]["status"] == "Working"):
    #     warning = 1
    #     # return to tmplate role,status,name,reservation data
    #     return render_template("checkout.html",employee_info = employee_info,reservation_data = reservation_data,warning = warning,)

    # if status is not "Working"
    if employee_info[0]["status"] != "Working":
        warning = 1
        # return to tmplate role,status,name,reservation data
        return render_template(
            "checkout.html",
            employee_info=employee_info,
            warning=warning,
        )
    reservation = request.form.get("reservation")
    # if there is no reservation selected
    if not (reservation := request.form.get("reservation")):
        warning = 2
        # return to tmplate role,status,name,reservation data
        return render_template(
            "checkout.html",
            employee_info=employee_info,
            reservation_data=reservation_data,
            warning=warning,
        )
    # get today's date
    today = date.today()

    # # update exit date if exists
    # if(reservation_data[11]["exit_date"] is not ""):
    #     db.execute("UPDATE reservations SET exit_date = ? WHERE id = ?;",today,reservation[0]["id"])
    # inserting exit date to be today's date
    db.execute(
        "UPDATE reservations SET exit_date = ? WHERE id = ?;", today, reservation
    )
    # select room id from reservations table by reservation id
    roomid = db.execute("SELECT roomid FROM reservations WHERE id = ?;", reservation)
    # updating room status to be opened
    db.execute(
        """UPDATE rooms SET
                  status = ? WHERE id = ?;
    """,
        "open",
        roomid,
    )
    sucessed = 1
    # return to main after checking out
    return render_template(
        "index.html",
        sucessed=sucessed,
        employee_info=employee_info,
    )


<<<<<<< HEAD
# @app.route("/addnewuser", methods=["GET", "POST"])
# @login_required
# def addnewuser():
#     # 
#     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
#     # 
#     name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
#     # 
#     roles = ["Admin","Receptionist","Reporter","Reception manager"]
#     # 
#     m_name = request.form.get("middle_name")
#     # 
#     status = db.execute("SELECT status FROM users WHERE id = ?", session["user_id"])
=======
@app.route("/addnewuser", methods=["GET", "POST"])
@login_required
def addnewuser():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # roles options
    roles_for_admin = ["Receptionist", "Reporter", "Reception manager"]
    # roles options
    roles_for_reception_manager = ["Receptionist"]
    # get middle name of adding user from template
    m_name = request.form.get("middle_name")
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # # if status is "Working"
    # if (employee_info[0]["status"] == "Working"):
    #     # return to tmplate role,status,name
    #     return render_template("addnewuser.html",roles_for_admin = roles_for_admin,roles_for_reception_manager = roles_for_reception_manager,employee_info = employee_info,)
    # # if status is not "Working"
    if employee_info[0]["status"] != "Working":
        # return to tmplate role,status,name
        return render_template(
            "addnewuser.html",
            employee_info=employee_info,
        )
    #
    if not (f_name := request.form.get("first_name")):
        warning = 1
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif not (l_name := request.form.get("last_name")):
        warning = 2
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif not (username := request.form.get("username")):
        warning = 3
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif not (password := request.form.get("password")):
        warning = 4
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif not (role_in := request.form.get("role")):
        Warning = 5
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif not (confirmation := request.form.get("confirmation")):
        warning = 6
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )
    #
    elif confirmation != password:
        warning = 7
        return render_template(
            "addnewuser.html",
            warning=warning,
            roles_for_admin=roles_for_admin,
            roles_for_reception_manager=roles_for_reception_manager,
            employee_info=employee_info,
        )

<<<<<<< HEAD
#     #     employee_data = db.execute("SELECT role,status FROM users WHERE id = ?", session["user_id"])
#     #     name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
#     #     roles = ["Admin","Receptionist","Reporter","Reception manager"]
#     #     m_name = request.form.get("middle_name")
#     #     return render_template("addnewuser.html", roles = roles, role = role[0]["role"])
    
#     # elif not (m_name := request.form.get("middle_name")):
#     #     warning = 2
#     #     return render_template("addnewuser.html",warning = warning, roles = roles)

#     if not (f_name := request.form.get("first_name")):
#         warning = 1
#         return render_template("addnewuser.html",warning = warning, roles = roles,role = role[0]["role"],status = status[0]["status"],)
    
#     elif not (l_name := request.form.get("last_name")):
#         warning = 2
#         return render_template("addnewuser.html",warning = warning, roles = roles, role = role[0]["role"],status = status[0]["status"],)

#     elif not (username:= request.form.get("username")):
#         warning = 3
#         return render_template("addnewuser.html",warning = warning, roles = roles,role = role[0]["role"],status = status[0]["status"],)

#     elif not(password := request.form.get("password")):
#         warning = 4
#         return render_template("addnewuser.html",warning = warning, roles = roles, role = role[0]["role"],status = status[0]["status"],)

#     elif not (role_in := request.form.get("role")):
#         Warning = 5
#         return render_template("addnewuser.html",warning = warning, roles = roles, role = role[0]["role"],status = status[0]["status"],)
    
#     elif(role_in not in roles):
#         Warning = 6
#         return render_template("addnewuser.html",warning = warning, roles = roles, role = role[0]["role"],status = status[0]["status"],)
    
#     added_user = db.execute(""" INSERT INTO users (first_name, middle_name, last_name, username, hash, role,status)   );
#                                 VALUES (?,?,?,?,?,?,?);""",
#                                 f_name,m_name,l_name,
#                                 username,generate_password_hash(password),
#                                 role_in,"Working")
#     # sucessed = 1
#     # return render_template("index.html",sucessed = sucessed,status = status[0]["status"],)
#     sucessed = 1
#     return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],sucessed = sucessed,status = status[0]["status"],)
#     # return render_template("addnewuser.html",user_role = user_role[0]["role"],roles =roles)



# @app.route("/changinguserstatus", methods=["GET", "POST"])
# @login_required
# def removeuser():
#     name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
#     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
#     users_data = db.execute("SELECT * FROM users WHERE role != ?;","Admin")    
#     status = db.execute("SELECT status FROM users WHERE id = ?", session["user_id"])
=======
    # # admin have access to remove any role except admins
    # if (employee_info[0]["role"] == "Admin"):
    #     if(role_in not in roles_for_admin):
    #         warning = 8
    #         return render_template("addnewuser.html",warning = warning,employee_info = employee_info,)
    # # Reception manager have access to remove only Receptionists
    # elif(employee_info[0]["role"] == "Reception manager"):
    #     if(role_in not in roles_for_reception_manager):
    #         warning = 8
    #         return render_template("addnewuser.html",warning = warning,employee_info = employee_info,)

    # Inserting new added user's data into users table in database
    db.execute(
        """ INSERT INTO users(first_name, middle_name, last_name, username, hash, role,status)
                                VALUES (?,?,?,?,?,?,?);""",
        f_name,
        m_name,
        l_name,
        username,
        generate_password_hash(password),
        role_in,
        "Working",
    )
    # Adding user to users report
    # Selecting id of new user
    newuserid = db.execute(
        """ SELECT id FROM users WHERE first_name = ? AND last_name = ?
                                            AND username = ?
                                            AND role = ? AND status = ?;""",
        f_name,
        l_name,
        username,
        role_in,
        "Working",
    )
    userid = newuserid[0]["id"]
    # Inserting new added user's data into action report table in database
    db.execute(
        """ INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee)
                               VALUES (?,?,?,?);""",
        "none",
        userid,
        0,
        "none",
    )
    sucessed = 1
    # return to main page after a successful adding user
    return render_template(
        "index.html",
        sucessed=sucessed,
        employee_info=employee_info,
    )


@app.route("/changinguserstatus", methods=["GET", "POST"])
@login_required
def changinguserstatus():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )
    # get employee's data from database for Admin
    users_data_for_admin = db.execute("SELECT * FROM users WHERE role != ?;", "Admin")
    # get employee's data from database for Reception manager
    users_data_for_reception_manager = db.execute(
        "SELECT * FROM users WHERE role = ?;", "Receptionist"
    )
    # get employee's data from database for Admin
    users_data_for_admin_count = db.execute(
        "SELECT COUNT(id) FROM users WHERE role != ?;", "Admin"
    )
    # get employee's data from database for Reception manager
    users_data_for_reception_manager_count = db.execute(
        "SELECT COUNT(id) FROM users WHERE role = ?;", "Receptionist"
    )
    # status options
    status_options = [
        "Working",
        "Fired",
        "Retired",
        "Moved",
        "Promoted",
        "Demoted",
        "Transferred",
    ]
    # # roles options
    roles = ["Admin", "Receptionist", "Reporter", "Reception manager"]
    # roles options
    roles_for_admin = ["Receptionist", "Reporter", "Reception manager"]
    # roles options
    roles_for_reception_manager = ["Receptionist"]
    i = 0
    # # if status is not working quit
    # if (employee_info[0]["status"] == "Working"):
    #     # return to tmplate role,status,name
    #     return render_template("changinguserstatus.html",users_data_for_admin = users_data_for_admin,users_data_for_reception_manager =users_data_for_reception_manager,roles = roles,status_options = status_options,employee_info = employee_info,)
    # if status is not working quit
    if employee_info[0]["status"] != "Working":
        # return to tmplate role,status,name
        return render_template(
            "changinguserstatus.html",
            employee_info=employee_info,
        )
    # if there is no selected user
    if not (user := request.form.get("user")):
        warning = 1
        return render_template(
            "changinguserstatus.html",
            warning=warning,
            users_data_for_admin=users_data_for_admin,
            users_data_for_reception_manager=users_data_for_reception_manager,
            roles=roles,
            status_options=status_options,
            employee_info=employee_info,
        )
    # if there is no selected status
    elif not (status_get := request.form.get("status")):
        warning = 2
        return render_template(
            "changinguserstatus.html",
            warning=warning,
            users_data_for_admin=users_data_for_admin,
            users_data_for_reception_manager=users_data_for_reception_manager,
            roles=roles,
            status_options=status_options,
            employee_info=employee_info,
        )
    # if selected status not in status options
    elif status_get not in status_options:
        warning = 3
        return render_template(
            "changinguserstatus.html",
            warning=warning,
            users_data_for_admin=users_data_for_admin,
            users_data_for_reception_manager=users_data_for_reception_manager,
            roles=roles,
            status_options=status_options,
            employee_info=employee_info,
        )
    # admin have access to remove any role except admins
    # elif (employee_info[0]["role"] == "Admin"):
    #     while(i != users_data_for_admin_count):
    #         if(user not in users_data_for_admin):
    #             warning = 4
    #             # return render_template("changinguserstatus.html",warning = warning,employee_info = employee_info,)
    #         i = i + i
    #     if(i != users_data_for_admin_count):
    #         warning = 4
    #         return render_template("changinguserstatus.html",warning = warning,employee_info = employee_info,)
    # # Reception manager have access to remove only Receptionists
    # elif (employee_info[0]["role"] == "Reception manager"):
    #     while(i != users_data_for_reception_manager_count):
    #         if(user not in users_data_for_reception_manager):
    #             warning = 4
    #             return render_template("changinguserstatus.html",warning = warning,employee_info = employee_info,)
    #         i = i + i
    # if selected status not not equal to user's status
    # elif (user[i]["status"] != status_get):
    #     warning = 5
    #     return render_template("changinguserstatus.html",warning = warning,users_data_for_admin = users_data_for_admin,users_data_for_reception_manager =users_data_for_reception_manager,roles = roles,status_options = status_options,employee_info = employee_info,)
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0

    # Update status according to the status selected
    db.execute(""" UPDATE users SET status = ? WHERE id= ?;""", status_get, user)
    sucessed = 1
    # Return to main page after a successfully changing users status
    return render_template(
        "index.html",
        sucessed=sucessed,
        employee_info=employee_info,
    )
    # return render_template("index.html",sucessed = sucessed,employee_info = employee_info,)


@app.route("/reservationshistory", methods=["GET", "POST"])
@login_required
def reservationshistory():
    # get employee's data from database
    employee_info = db.execute(
        "SELECT first_name,role,status FROM users WHERE id = ?;", session["user_id"]
    )

<<<<<<< HEAD
#     if not(user:= request.form.get("user")):
#         warning = 2
#         return render_template("changinguserstatus.html",warning = warning,users_data =users_data,role = role[0]["role"] ,status_get = status[0]["status"],roles = roles,status_options = status_options,)
#     elif (role_get not in roles):
#         warning = 3
#         return render_template("changinguserstatus.html",warning = warning,users_data =users_data,role = role[0]["role"] ,status_get = status[0]["status"],roles = roles,status_options = status_options,)
#     elif (role_get != "Admin"):
#         warning = 4
#         return render_template("changinguserstatus.html",warning = warning,users_data =users_data,role = role[0]["role"] ,status_get = status[0]["status"],roles = roles,status_options = status_options,)
#     elif not(status_get:= request.form.get("status")):
#         warning = 5
#         return render_template("changinguserstatus.html",warning = warning,users_data =users_data,role = role[0]["role"],name = name[0]["first_name"],status_get = status[0]["status"],roles = roles,status_options = status_options,)
#     elif (status_get not in status_options):
#         warning = 6
#         return render_template("changinguserstatus.html",warning = warning,users_data =users_data,role = role[0]["role"],name = name[0]["first_name"],status_get = status[0]["status"],roles = roles,status_options = status_options,)
   
#     # id = db.execute("SELECT * FROM users WHERE username = ?;",user[4]["username"])
#     # db.execute(""" DELETE FROM users WHERE id= ?;""",id)
#     db.execute(""" UPDATE users SET status = "?" WHERE id= ?;""",status_get,user[0]["id"])
#     sucessed = 1
#     return render_template("index.html",role = role[0]["role"],sucessed = sucessed,status_get = status[0]["status"],)
#     # sucessed = 1
#     # return render_template("index.html",role = role[0]["role"],name = name[0]["first_name"],sucessed = sucessed,status = status[0]["status"],)
=======
    reservation_data = db.execute(
        """SELECT reservations.exit_date AS exit_date,
                                  reservations.registration_time AS registration_time,
                                  reservations.payment AS payment,
                                  reservations.reservation_status AS reservation_status,
                                  reservations.checkin AS checkin,
                                  reservations.checkout AS checkout,
                                  reservations.price AS price,
                                  rooms.room_number AS room_number,
                                  patient.first_name AS pateint_first_name ,
                                  patient.middle_name AS pateint_middle_name ,
                                  patient.last_name AS pateint_last_name ,
                                  users.first_name AS user_first_name ,
                                  users.role AS user_role
                                  FROM reservations
                                  JOIN patient ON patient.id = reservations.patient_id
                                  JOIN rooms ON rooms.id = reservations.roomid
                                  JOIN users ON users.id = reservations.user_id
                                ;"""
    )

    return render_template(
        "reservationshistory.html",
        reservation_data=reservation_data,
        employee_info=employee_info,
    )
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
