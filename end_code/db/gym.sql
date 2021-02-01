DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS locations;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    date_of_birth DATE,
    contact_number VARCHAR(255),
    email_address VARCHAR(255),
    experience VARCHAR(255),
    membership_level VARCHAR (255),
    active_status BOOLEAN
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    duration TIME,
    experience_level VARCHAR (255)
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    contact_number VARCHAR(255)
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    capacity INT,
    accessible BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    activity_id INT REFERENCES activities(id),
    instructor_id INT REFERENCES instructors(id),
    location_id INT REFERENCES locations(id)  
);