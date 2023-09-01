-- users (employees) table
CREATE TABLE
  users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    role TEXT NOT NULL
  );

-- rooms table
CREATE TABLE
  rooms (
    id INTEGER PRIMARY KEY,
    room_number INTEGER NOT NULL,
    status TEXT NOT NULL,
    price NUMERIC NOT NULL
  );

-- action report table
CREATE TABLE
  action_report (
    id INTEGER PRIMARY KEY,
    action TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    number_of_reservations INTEGER,
    Actions_notes_of_employee TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
  );

-- patient table
CREATE TABLE
  patient (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT NOT NULL,
    roomid INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    phone1 VARCHAR(15) NOT NULL,
    phone2 VARCHAR(15),
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_relation TEXT,
    emergency_contact_phone VARCHAR(15) NOT NULL,
    emergency_contact_address TEXT,
    registration_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Email VARCHAR(255),
    b_day INT,
    b_year INT,
    b_month INT,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (roomid) REFERENCES rooms (id)
  );

-- reservations table
CREATE TABLE
  reservations (
    id INTEGER PRIMARY KEY,
    roomid INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    price NUMERIC,
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    reservation_status TEXT NOT NULL,
    payment TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (roomid) REFERENCES rooms (id)
  );

-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",1,0,"none");
-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",2,0,"none");
-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",3,0,"none");
-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",4,0,"none");
-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",5,0,"none");
-- INSERT INTO action_report(action ,user_id, number_of_reservations, Actions_notes_of_employee) VALUES ("none",6,0,"none");
-- INSERT INTO rooms(room_number,status,price) VALUES (101,"open",1000);
-- INSERT INTO rooms(room_number,status,price) VALUES (102,"open",1500);
-- INSERT INTO rooms(room_number,status,price) VALUES (103,"open",2000);
-- INSERT INTO rooms(room_number,status,price) VALUES (104,"open",2500);
-- INSERT INTO rooms(room_number,status,price) VALUES (201,"open",3000);
-- INSERT INTO rooms(room_number,status,price) VALUES (202,"open",3500);
-- INSERT INTO rooms(room_number,status,price) VALUES (203,"open",4000);
-- INSERT INTO rooms(room_number,status,price) VALUES (204,"open",4500);
-- INSERT INTO rooms(room_number,status,price) VALUES (301,"open",5000);
-- INSERT INTO rooms(room_number,status,price) VALUES (302,"open",5500);
-- SELECT users.first_name,users.middle_name,users.last_name,users.role,action_report.action ,action_report.user_id, action_report.number_of_reservations, action_report.Actions_notes_of_employee FROM action_report JOIN users ON users.id = action_report.user_id ;