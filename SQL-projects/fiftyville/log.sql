-- Keep a log of any SQL queries you execute as you solve the mystery.
--get description of crime happend in 28th of july 2021
SELECT description FROM crime_scene_reports
WHERE day = "28" AND month = "7" AND year = "2021"
and street="Humphrey Street";
-- Check the transcript of the theft date(28/7/2021) interviews mentioned by the bakery;
SELECT transcript FROM interviews
WHERE day = "28" AND month = "7" AND year = "2021" AND transcript like "%bakery%";
-- check for cars owners's that exit bakery with in 10 min.
select name from people
where license_plate IN
(select license_plate from bakery_security_logs
where day = "28" AND month = "7" AND year = "2021" AND hour = 10 AND minute > 14 AND minute < 25 AND activity = "exit");
-- check for accounts owners's,their id, account number and ammount of money withdrawed in (28/7/2021) at Leggett Street
select people.name,bank_accounts.person_id,bank_accounts.account_number,atm_transactions.amount from bank_accounts
inner join atm_transactions
inner join people
on bank_accounts.account_number = atm_transactions.account_number and people.id = bank_accounts.person_id
where bank_accounts.account_number in (select account_number from atm_transactions
where day = "28" AND month = "7" AND year = "2021" AND transaction_type = "withdraw" AND atm_location ="Leggett Street")
and people.id ;

-- check for phone calls that happened in (28/7/2021) and duration less than 60 seconds
select caller,receiver from phone_calls
where day = "28" AND month = "7" AND year = "2021" AND duration < 60;
--check for names of recievers
select name as receiver_name,phone_number as receiver_number from people
where receiver_number IN (select receiver from phone_calls
where day = "28" AND month = "7" AND year = "2021" AND duration < 60);
--check for names of callers
select name as caller_name,phone_number as caller_number from people
where caller_number IN (select caller from phone_calls
where day = "28" AND month = "7" AND year = "2021" AND duration < 60);

-- get all data of fiftyvile airport
select * from airports
where city = "Fiftyville";
--get all flights on (29/7/2021) from fiftyville
select id,origin_airport_id,destination_airport_id,hour,minute from flights
where origin_airport_id = 8 AND day = "29" AND month = "7" AND year = "2021";
--check for flight no. and passport number of Bruce and Diana
select flight_id,passport_number from passengers
where passport_number = 3592750733 or passport_number = 5773159633;
--check destination of airport's id 6 and 4
select * from airports
where id = 6 or id = 4;
