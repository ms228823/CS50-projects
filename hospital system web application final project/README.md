<<<<<<< HEAD
# This is CS50's final project hospital reservaton system web application
#### Video Demo:  There is the [Youtube Vedio]()
#### Description:
=======
# This is CS50 Final Project (Hospital reservation system (web application))
<p> Programming languages Used:<strong> HTML & CSS, JavaScript, Python (Flask), SQL</strong>
Libraries and frameworks used :<strong> Flask, Flask-session, Jinja2, Werkzeug, pytz, requests, sqlite3</strong></p>

## There is the [Youtube Vedio]()

# Description:
<p>This web app is a hospital room reservation system in which it's main purpose is to simulate room reservations, adding users with different roles and different system functions and generating reports similar to real hospital systems.

 <strong>This project was made for HarvardX's university's course (cs50x).</strong> It has been developed using Python Flask framework. The main purpose of
 1. The user can sign in himself/herself by providing his details (username & password).
 2. After signing in the user will be redirected to the Main page where he/she has options that differ according to the user's Role
</p>
for example:

### <h1>1. Admins:</h1>
![Admins](/gifs/davidadmin.gif)

<h2>Admins can do:</h2>
    <ol style ="font-size: 14pt;">
        <li>Adding new users to all roles (except admin which are added by default in the database).</li>
        <li>Changing users' status from working to ("Fired", "Retired", "Moved", "Promoted", "Demoted", "Transferred") or
    vice versa (except admins which their statuses are determined by default in users' tables).</li>
        <li>Patient registration.</li>
        <li>Book a room for patient after patient registration.</li>
        <li>Check out a reservation</li>
        <li>Able to see users actions report and print it</li>
        <li>Able to check rooms (room no., price, status) and print it</li>
        <li>Able to see reservations history and print it</li>
    </ol>

### <h1>2. Reception Manager:</h1>
![Reception Manager](/gifs/receptionmanager.gif)

<h2>Reception Manager can do:</h2>
    <ol style ="font-size: 14pt;">
        <li>Adding new user (Receptionist)</li>
        <li>Changing Receptionist status from working to ("Fired", "Retired", "Moved", "Promoted", "Demoted", "Transferred") or
    vice versa .</li>
        <li>Patient registration.</li>
        <li>Book a room for patient after patient registration.</li>
        <li>Check out a reservation</li>
        <li>Able to see Receptionist actions report and print it</li>
        <li>Able to check rooms (room no., price, status) and print it</li>
        <li>Able to see reservations history and print it</li>
    </ol>

### <h1>3. Receptionist:</h1>
![Receptionist](/gifs/Receptionist.gif)

<h2> Receptionists can do:</h2>
    <ol style ="font-size: 14pt;">
        <li>Patient registration.</li>
        <li>Book a room for patient after patient registration.</li>
        <li>Check out a reservation</li>
        <li>Able to check rooms (room no., price, status) and print it</li>
        <li>Able to see reservations history and print it</li>
    </ol>

### <h1>4. Reporter:</h1>

![reporter](/gifs/reporter.gif)

<h2> Reporters can do: </h2>
    <ol style ="font-size: 14pt;">
        <li>Able to see users actions report and print it</li>
        <li>Able to check rooms (room no, price, status) and print it</li>
        <li>Able to see reservations history and print it</li>
    </ol>

<mark style = "background-color: Green; font-size: 24pt; color: white;">All Users usernames, passwords, roles, and status in users.txt</mark>

## Functions pages :

### 1. Patient Registration
![Patient Registration](/gifs/patientregestration.gif)

<p>Patient registration allows users to add patient personal information, Contact information, And Emergency Contact Information</p>

### 2. Check-In
![Check In](/gifs/checkin.gif)

<p> Check-in comes after patient registration On this page users select patient data and rooms that are available to him/her, each room selection has a price, check-in date, and check-out date having a minimum value of today, and payment method (Cash, Visa or Mastercard).
After Check-in the room status changed from open to reserved</p>

### 3. Check Out
![Check Out](/gifs/checkout.gif)

<p>Choosing a reservation to add an exit date to this reservation (N.B: exit date is the confirmed date with the patient left the hospital).
After check-out, the room status changes back to open and becomes available to be reserved again at check-in.</p>

![Check Out](/gifs/reservationshistoryafterchecking out.mp.gif)

### 4. Employees Report
![Employees Report](/gifs/usersreport.gif)

<p>This page shows the users' information like name, their roles in the system, their status, and no. of reservations made by users (For reporters no. of reservations is none) and any action notes.
The user can Print this report by clicking the button "print this page".</p>

### 5. Add New User
![Add New User](/gifs//staticAddinguser.gif)

<p>This function is available to only admins and reception manager which:
<strong>Admin can add only reception manager, receptionist, and reporter</strong>
<strong>Reception manager can only add receptionist </strong>
Once the user is added he/she can use the system in restricted borders</p>

### 6. Changing User Status
![Changing User Status](/gifs/changinguserstatus.gif)

<p>This function is available to only admins and reception manager which:
<strong>Admin can change status to only reception manager, receptionist, and reporter from working to ("Fired", "Retired", "Moved", "Promoted", "Demoted", "Transferred") or vice versa .</strong>
<strong>Reception manager can only change status to receptionist from working to ("Fired", "Retired", "Moved", "Promoted", "Demoted", "Transferred") or vice versa .</strong>
Once the user's status changes from working to anything else he can't use the system and vice versa. </p>

![Changing User Status](/gifs/usersreportafterchanginguser status.gif)

### 7. Check Rooms
![Check Rooms](/gifs/checkrooms.gif)

<p>This page shows room information: room no, price, and status which can be "open", "reserved"
The user can Print this report by clicking the button "print this page".</p>


### 8. Reservations History
![Reservations History](/gifs/reservationshistory.gif)

<p>This page shows Reservations information: Rooms No.	patient Name, Check-In Date, Check-Out Date, Exit Date, Total Price, which is no of reservation days * price,....etc.
The user can Print this report by clicking the button "print this page".</p>
>>>>>>> 351e0a0829047f8e80c5f2b25f4931aff66b0ab0
