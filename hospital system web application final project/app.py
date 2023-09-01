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

# Custom filter
app.jinja_env.filters["usd"] = usd

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
            return render_template("login.html", warning=warning)

        # Ensure password was submitted
        elif not (password := request.form.get("password")):
            warning = 2
            return render_template("login.html", warning=warning)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            warning = 3
            return render_template("login.html", warning=warning)

        # Remember which user has logged in

        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    # print("HELLO World")
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])

    # if(action_button := (request.form['action_button']) == "patient_registeration"):
    #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    #     return render_template("patient_registeration.html",role = role,)

    # elif(action_button := (request.form['action_button']) == "checkrooms"):
    #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    #     rooms = db.execute("SELECT * FROM rooms;")
    #     return render_template("checkrooms.html",role = role,rooms = rooms)

    # # elif(action_button := (request.form['action_button']) == "checkin"):
    # #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])

    # # elif(action_button := (request.form['action_button']) == "checkout"):
    # #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])

    # elif(action_button := (request.form['action_button']) == "printreport"):
    #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    #     name = db.execute("""SELECT users.first_name,users.middle_name,users.last_name FROM users JOIN action_report ON
    #                     users.id = action_report.user_id """)
    #     actions = db.execute("""SELECT action_report.* FROM action_report JOIN users ON
    #                     users.id = action_report.user_id """)
    #     return render_template("printreport.html",role = role ,actions = actions,name = name)

    # elif(action_button := (request.form['action_button']) == "addnewuser"):
    #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    #     name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
    #     roles = ["admin","reception","reporting","reception manager"]
    #     m_name = request.form.get("middle_name")
    #     return render_template("addnewuser.html", roles = roles, role = role[0]["role"])

    # elif(action_button := (request.form['action_button']) == "removeuser"):
    #     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])

    # elif(action_button := (request.form['action_button']) == "logout"):
    #     redirect("/logout")

    return render_template(
        "index.html", role=role[0]["role"], name=name[0]["first_name"]
    )


@app.route("/patientregisteration", methods=["GET", "POST"])
@login_required
def patient_registeration():
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])

    titles = ["Mr.", "Miss.", "Ms."]
    genders = ["Male", "Female"]
    countries = [
        "Afghanistan",
        "Aland Islands",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antarctica",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia, Plurinational State of",
        "Bonaire, Sint Eustatius and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island",
        "Brazil",
        "British Indian Ocean Territory",
        "Brunei Darussalam",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cape Verde",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Christmas Island",
        "Cocos (Keeling) Islands",
        "Colombia",
        "Comoros",
        "Congo",
        "Congo, The Democratic Republic of the",
        "Cook Islands",
        "Costa Rica",
        "Côte d'Ivoire",
        "Croatia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Ethiopia",
        "Falkland Islands (Malvinas)",
        "Faroe Islands",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "French Southern Territories",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Heard Island and McDonald Islands",
        "Holy See (Vatican City State)",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran, Islamic Republic of",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Korea, Democratic People's Republic of",
        "Korea, Republic of",
        "Kuwait",
        "Kyrgyzstan",
        "Lao People's Democratic Republic",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Macedonia, Republic of",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Mayotte",
        "Mexico",
        "Micronesia, Federated States of",
        "Moldova, Republic of",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Niue",
        "Norfolk Island",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestine",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Réunion",
        "Romania",
        "Russian Federation",
        "Rwanda",
        "Saint Barthélemy",
        "Saint Helena, Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin (French part)",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "South Sudan",
        "Svalbard and Jan Mayen",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syrian Arab Republic",
        "Taiwan, Province of China",
        "Tajikistan",
        "Tanzania, United Republic of",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "United States Minor Outlying Islands",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela, Bolivarian Republic of",
        "Viet Nam",
        "Virgin Islands, British",
        "Virgin Islands, U.S.",
        "Wallis and Futuna",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    ]
    days = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
    ]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years = [
        1900,
        1901,
        1902,
        1903,
        1904,
        1905,
        1906,
        1907,
        1908,
        1909,
        1910,
        1911,
        1912,
        1913,
        1914,
        1915,
        1916,
        1917,
        1918,
        1919,
        1920,
        1921,
        1922,
        1923,
        1924,
        1925,
        1926,
        1927,
        1928,
        1929,
        1930,
        1931,
        1932,
        1933,
        1934,
        1935,
        1936,
        1937,
        1938,
        1939,
        1940,
        1941,
        1942,
        1943,
        1944,
        1945,
        1946,
        1947,
        1948,
        1949,
        1950,
        1951,
        1952,
        1953,
        1954,
        1955,
        1956,
        1957,
        1958,
        1959,
        1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
    ]
    middle_name = request.form.get("middle_name")
    roomid = db.execute(
        "SELECT id  FROM  rooms where room_number = ?;", request.form.get("Room_no")
    )
    phone2 = request.form.get("phone2")
    emergency_contact_address = request.form.get("emergency_contact_address")
    email = request.form.get("email")
    # calculate age ***

    def age(birthdate):
        today = date.today()
        age = (
            today.year
            - request.form.get("year")
            - (
                (today.month, today.day)
                < (request.form.get("month"), request.form.get("day"))
            )
        )
        return age

    # Ensure title was submitted
    if not (title := request.form.get("title")):
        warning = 1
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure first_name was submitted
    elif not (first_name := request.form.get("first_name")):
        warning = 2
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure last_name was submitted
    elif not (last_name := request.form.get("last_name")):
        warning = 3
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure genders was submitted
    elif not (gender_get := request.form.get("gender")):
        warning = 4
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure nationality was submitted
    elif not (nationality := request.form.get("nationality")):
        warning = 6
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure id was submitted
    elif not (id := request.form.get("id")):
        warning = 7
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure street was submitted
    elif not (street := request.form.get("street")):
        warning = 8
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure phone1 was submitted
    elif not (phone1 := request.form.get("phone1")):
        warning = 9
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure your_email was submitted
    elif not (your_email := request.form.get("your_email")):
        warning = 10
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure emergency_contact_name was submitted
    elif not (emergency_contact_name := request.form.get("emergency_contact_name")):
        warning = 11
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure emergency_contact_relation was submitted
    elif not (
        emergency_contact_relation := request.form.get("emergency_contact_relation")
    ):
        warning = 12
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # Ensure emergency_contact_phone was submitted
    elif not (emergency_contact_phone := request.form.get("emergency_contact_phone")):
        warning = 13
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(day) was submitted
    elif not (birth_date_day := request.form.get("day")):
        warning = 14
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(month) was submitted
    elif not (birth_date_month := request.form.get("month")):
        warning = 15
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(year) was submitted
    elif not (birth_date_year := request.form.get("year")):
        warning = 16
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(day) in days
    elif birth_date_day not in days:
        warning = 17
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(month) in months
    elif birth_date_month not in months:
        warning = 18
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )
    # Ensure birth_date(year) in years
    elif birth_date_year not in years:
        warning = 19
        return render_template(
            "patient_registeration.html",
            warning=warning,
            role=role[0]["role"],
            genders=genders,
            countries=countries,
            titles=titles,
            days=days,
            months=months,
            years=years,
        )

    # inserting data into patient table
    db.execute(
        """INSERT INTO patient(first_name, middle_name, last_name,
                                  b_day,b_year,b_month, age, gender, roomid, user_id,
                                  phone1, phone2,
                                  emergency_contact_name, emergency_contact_relation,
                                  emergency_contact_phone,
                                  emergency_contact_address, Email)
                                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        first_name,
        middle_name,
        last_name,
        birth_date_day,
        birth_date_year,
        birth_date_month,
        age,
        gender_get,
        roomid,
        session["user_id"],
        phone1,
        phone2,
        emergency_contact_name,
        emergency_contact_relation,
        emergency_contact_phone,
        emergency_contact_address,
        email,
    )
    # get number of reservations of user
    number_of_reservation_get = db.execute(
        "SELECT number_of_reservations FROM action_report WHERE user_id = ?",
        session["user_id"],
    )
    # add one to number of reservations of user
    number_of_reservations_sent = number_of_reservation_get + 1
    # update the number of reservations to the new one
    db.execute(
        """UPDATE action_report
                  number_of_reservations = ? WHERE user_id = ?;
    """,
        number_of_reservations_sent,
        session["user_id"],
    )
    sucessed = 1
    return render_template("index.html", sucessed=sucessed)


@app.route("/printreport", methods=["GET", "POST"])
@login_required
def printreport():
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    # name = db.execute("""SELECT users.first_name,users.middle_name,users.last_name FROM users JOIN action_report ON
    #                             users.id = action_report.user_id ;""")

    actions_of_employees = db.execute(
        """SELECT users.first_name AS first_name,users.middle_name As middle_name,users.last_name AS last_name,
                                   users.role AS role,action_report.action AS action,action_report.user_id AS user_id, 
                                   action_report.number_of_reservations AS number_of_reservations, action_report.Actions_notes_of_employee AS actions_notes_of_employee
                                   FROM action_report JOIN users ON users.id = action_report.user_id ;"""
    )
    return render_template(
        "printreport.html",
        role=role[0]["role"],
        actions_of_employees=actions_of_employees,
    )


@app.route("/checkrooms", methods=["GET", "POST"])
@login_required
def checkrooms():
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    rooms_data = db.execute("SELECT room_number,status,price FROM rooms;")
    return render_template(
        "checkrooms.html", role=role[0]["role"], rooms_data=rooms_data
    )


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# @app.route("/checkin", methods=["GET", "POST"])
# @login_required
# def checkin():
# role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
# name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])

# sucessed = 1
# return render_template("index.html",sucessed = sucessed)
#     return render_template("checkin.html",role = role[0]["role"] ,name =name)

# @app.route("/checkout", methods=["GET", "POST"])
# @login_required
# def checkout():
# role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
#     return render_template("checkout.html",role = role[0]["role"])


@app.route("/addnewuser", methods=["GET", "POST"])
@login_required
def addnewuser():
    role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])
    name = db.execute("SELECT first_name FROM users WHERE id = ?", session["user_id"])
    roles = ["admin", "reception", "reporting", "reception manager"]
    m_name = request.form.get("middle_name")
    if not (f_name := request.form.get("first_name")):
        warning = 1
        return render_template(
            "addnewuser.html", warning=warning, roles=role[0]["role"]
        )

    # elif not (m_name := request.form.get("middle_name")):
    #     warning = 2
    #     return render_template("addnewuser.html",warning = warning, roles = roles)

    elif not (l_name := request.form.get("last_name")):
        warning = 2
        return render_template(
            "addnewuser.html", warning=warning, roles=roles, role=role[0]["role"]
        )

    elif not (username := request.form.get("username")):
        warning = 3
        return render_template(
            "addnewuser.html", warning=warning, roles=roles, role=role[0]["role"]
        )

    elif not (password := request.form.get("password")):
        warning = 4
        return render_template(
            "addnewuser.html", warning=warning, roles=roles, role=role[0]["role"]
        )

    elif not (role_in := request.form.get("role")):
        Warning = 5
        return render_template(
            "addnewuser.html", warning=warning, roles=roles, role=role[0]["role"]
        )

    elif role_in not in roles:
        Warning = 6
        return render_template(
            "addnewuser.html", warning=warning, roles=roles, role=role[0]["role"]
        )

    added_user = db.execute(
        """ INSERT INTO users (first_name, middle_name, last_name, username, hash, role)   );
                                VALUES (?,?,?,?,?,?);""",
        f_name,
        m_name,
        l_name,
        username,
        generate_password_hash(password),
        role_in,
    )
    sucessed = 1
    return render_template("index.html", sucessed=sucessed)
    # return render_template("addnewuser.html",user_role = user_role[0]["role"],roles =roles)


# @app.route("/removeuser", methods=["GET", "POST"])
# @login_required
# def removeuser():

#     role = db.execute("SELECT role FROM users WHERE id = ?", session["user_id"])

#     users = db.execute("SELECT * FROM users ;")

#     password = request.form.get("password")

#     # roles = ["admin","reception","reporting","reception manager"]
#     # if not (f_name := request.form.get("first_name")):
#     #     warning = 1
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif not(m_name := request.form.get("middle_name")):
#     #     warning = 2
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif not(l_name := request.form.get("last_name")):
#     #     warning = 3
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif not(username:= request.form.get("username")):
#     #     warning = 4
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif(role_in := request.form.get("role")):
#     #     Warning = 5
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif(f_name not in users):
#     #     Warning = 6
#     #     return render_template("addnewuser.html",warning = warning)
#     # elif(m_name not in users):
#     #     Warning = 6
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif(l_name not in users):
#     #     Warning = 7
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif(username not in users):
#     #     Warning = 8
#     #     return render_template("addnewuser.html",warning = warning)

#     # elif(role_in not in users):
#     #     Warning = 9
#     #     return render_template("addnewuser.html",warning = warning)

#     id = db.execute("SELECT * FROM users WHERE username = ?;",username)
#     added_user = db.execute(""" DELETE FROM users WHERE id= ?;""",id)

#     return render_template("removeuser.html",role = role)
