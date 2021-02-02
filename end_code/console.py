import pdb
import datetime
#imports python debugger.

from models.activity import Activity
from models.booking import Booking
from models.instructor import Instructor
from models.location import Location
from models.member import Member

#import models.

import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository
import repositories.member_repository as member_repository
#import repos.

activity_repository.delete_all()
booking_repository.delete_all()
instructor_repository.delete_all()
location_repository.delete_all()
member_repository.delete_all()
#removes the repos from the db when script is run.

## MEMBERS ##

member1 = Member('true', 'gold', '3', 'hansto@tmail.com', '07567654345', datetime.date(1989,12,22), 'Stocker', 'Hannah')
member_repository.save(member1)

member2 = Member('true', 'gold', '2', 'maryberry46@hotamil.com', '07332345097', datetime.date(1946,4,21), 'Berry', 'Mary')
member_repository.save(member2)

member3 = Member('true', 'silver', '1', 'iamagoodboy@dogmail.co.uk', '07982233234', datetime.date(1976,5,2), 'Marples', 'Angus')
member_repository.save(member3)

member4 = Member('true', 'gold', '2', 'why_m@googlemail.co.uk', '07122112452', datetime.date(1962,2,4), 'Marples', 'Yvonne')
member_repository.save(member4)

member5 = Member('true', 'gold', '3', 'barry1976@tescomail.com', '07323543456', datetime.date(1976,9,19), 'McDonald', 'Barry')
member_repository.save(member5)

member6 = Member('true', 'gold', '3', 'ewan123@hmail.com', '07998778761', datetime.date(1968,7,14), 'McDonald', 'Ewan')
member_repository.save(member6)

member7 = Member('true', 'silver', '1', 'jimmyjimjim@jimmail.net', '07584267899', datetime.date(1948,8,2), 'McClure', 'Jim')
member_repository.save(member7)

member8 = Member('true', 'silver', '1', 'mags45664@jimmail.net', '07584267555', datetime.date(1949,3,9), 'McClure', 'Mags')
member_repository.save(member8)

member9 = Member('true', 'gold', '3', 'geoffbygrove@gmail.com', '07762345911', datetime.date(2002,12,6), 'Bygrove', 'Geoff')
member_repository.save(member9)

member10 = Member('true', 'gold', '2', 'lozza_shap@gmail.com', '07212345678', datetime.date(2008,1,12), 'Shaply', 'Laura')
member_repository.save(member10)

member11 = Member('true', 'silver', '3', 'fergie_mcdergie@gmail.com', '07112343212', datetime.date(2005,11,2), 'MacDonald', 'Fern')
member_repository.save(member11)

member12 = Member('true', 'silver', '1', 'rossscott@hotmail.com', '07987556643', datetime.date(1985,10,11), 'Scott', 'Ross')
member_repository.save(member12)

member13 = Member('true', 'silver', '1', 'murraymint@gmail.com', '07221962309', datetime.date(1980,12,23), 'Brown', 'Murray')
member_repository.save(member13)

member14 = Member('true', 'silver', '2', '565_tom@gmail.com', '07212445398', datetime.date(1998,6,30), 'Kerr', 'Tom')
member_repository.save(member14)

member15 = Member('true', 'gold', '2', 'martinyounger@gmail.com', '01505685286', datetime.date(1988,11,10), 'Younger', 'Martin')
member_repository.save(member15)

member16 = Member('true', 'silver', '3', 'hunter55@hotmail.com', '07097679399', datetime.date(1955,4,17), 'Hunter', 'Kelly')
member_repository.save(member16)

member17 = Member('true', 'silver', '2', 'gordygrant@askjeeves.net', '03456779867', datetime.date(1957,3,2), 'Grant', 'Gordy')
member_repository.save(member17)

member18 = Member('true', 'gold', '1', 'flammingflemming@house.gov', '07778443666', datetime.date(1999,1,27), 'Flemming', 'Dick')
member_repository.save(member18)

member19 = Member('true', 'silver', '2', 'lucyinthesky@msn.com', '07898434666', datetime.date(1962,9,16), 'Donaldson', 'Lucy')
member_repository.save(member19)

member20 = Member('true', 'gold', '3', 'gibbo247@gfr.de.scot', '01505762543', datetime.date(1957,9,6), 'Gibson', 'Duncan')
member_repository.save(member20)


## ACTIVITIES ##

# Yoga #

activity1 = Activity('3', datetime.time(0,30), 'Yoga consists of deliberate, concentrated movements and postures designed to promote flexibility, tone and strengthen muscles and align the body.', 'Advanced Yoga')
activity_repository.save(activity1)

activity2 = Activity('2', datetime.time(0,30), 'Yoga consists of deliberate, concentrated movements and postures designed to promote flexibility, tone and strengthen muscles and align the body.', 'Intermediate Yoga')
activity_repository.save(activity2)

activity3 = Activity('1', datetime.time(0,30), 'Yoga consists of deliberate, concentrated movements and postures designed to promote flexibility, tone and strengthen muscles and align the body.', 'Beginners Yoga')
activity_repository.save(activity3)

# Circuit Training #

activity4 = Activity('3', datetime.time(1,0), 'Interval style, fast paced training around a circuit.', 'Advanced Circuit Training')
activity_repository.save(activity4)

activity5 = Activity('2', datetime.time(0,45), 'Interval style, fast paced training around a circuit.', 'Intermediate Circuit Training')
activity_repository.save(activity5)

activity6 = Activity('1', datetime.time(0,30), 'Interval style, fast paced training around a circuit.', 'Beginners Circuit Training')
activity_repository.save(activity6)

# Kickboxing #

activity7 = Activity('3', datetime.time(1,0), 'Kickboxing is a martial-arts style of fitness that provides a great cardiovascular workout and helps build endurance, coordination, tones muscles and core, all while working the heart and burning a lot of calories.', 'Advanced Kickboxing')
activity_repository.save(activity7)

activity8 = Activity('2', datetime.time(0,45), 'Kickboxing is a martial-arts style of fitness that provides a great cardiovascular workout and helps build endurance, coordination, tones muscles and core, all while working the heart and burning a lot of calories.', 'Intermediate Kickboxing')
activity_repository.save(activity8)

activity9 = Activity('1', datetime.time(0,30), 'Kickboxing is a martial-arts style of fitness that provides a great cardiovascular workout and helps build endurance, coordination, tones muscles and core, all while working the heart and burning a lot of calories.', 'Beginners Kickboxing')
activity_repository.save(activity9)

# Zumba #

activity10 = Activity('3', datetime.time(1,0), 'Zumba takes working out and converts it to something fun and upbeat that doesn’t feel like working out!', 'Advanced Zumba')
activity_repository.save(activity10)

activity11 = Activity('2', datetime.time(1,0), 'Zumba takes working out and converts it to something fun and upbeat that doesn’t feel like working out!', 'Intermediate Zumba')
activity_repository.save(activity11)

activity12 = Activity('1', datetime.time(1,0), 'Zumba takes working out and converts it to something fun and upbeat that doesn’t feel like working out!', 'Beginners Zumba')
activity_repository.save(activity12)

# Cycling #

activity13 = Activity('3', datetime.time(2,0), 'A cycling class is great cardio workout that relies on a fitness center cycling machine', 'Advanced Cycling')
activity_repository.save(activity13)

activity14 = Activity('2', datetime.time(1,5), 'A cycling class is great cardio workout that relies on a fitness center cycling machine', 'Intermediate Cycling')
activity_repository.save(activity14)

activity15 = Activity('1', datetime.time(1,0), 'A cycling class is great cardio workout that relies on a fitness center cycling machine', 'Beginners Cycling')
activity_repository.save(activity15)

# Bootcamp #

activity16 = Activity('3', datetime.time(2,0), 'Bootcamp classes are normally harder classes designed to push you outside of your regular limits through a combination of high intensity, cardio and strength-training movements.', 'Advanced Bootcamp')
activity_repository.save(activity16)

activity17 = Activity('2', datetime.time(2,0), 'Bootcamp classes are normally harder classes designed to push you outside of your regular limits through a combination of high intensity, cardio and strength-training movements.', 'Intermediate Bootcamp')
activity_repository.save(activity17)

# HIIT #

activity18 = Activity('3', datetime.time(0,45), 'HIIT stands for High-Intensity Interval Training, and is an exercise strategy that alternates short periods of intense exercise movements, followed by less intense, but still active “recovery” periods.', 'Advanced HIIT')
activity_repository.save(activity18)

activity19 = Activity('2', datetime.time(0,30), 'HIIT stands for High-Intensity Interval Training, and is an exercise strategy that alternates short periods of intense exercise movements, followed by less intense, but still active “recovery” periods.', 'Intermediate HIIT')
activity_repository.save(activity19)

activity20 = Activity('1', datetime.time(0,30), 'HIIT stands for High-Intensity Interval Training, and is an exercise strategy that alternates short periods of intense exercise movements, followed by less intense, but still active “recovery” periods.', 'Beginners HIIT')
activity_repository.save(activity20)

# Pilates #

activity21 = Activity('3', datetime.time(0,30), 'This physical fitness system is a form of low-impact exercise that aims to strengthen muscles while improving postural alignment and flexibility.', 'Advanced Pilates')
activity_repository.save(activity21)

activity22 = Activity('2', datetime.time(0,30), 'This physical fitness system is a form of low-impact exercise that aims to strengthen muscles while improving postural alignment and flexibility.', 'Intermediate Pilates')
activity_repository.save(activity22)

activity23 = Activity('1', datetime.time(0,30), 'This physical fitness system is a form of low-impact exercise that aims to strengthen muscles while improving postural alignment and flexibility.', 'Beginners Pilates')
activity_repository.save(activity23)

# Kettlebells #

activity24 = Activity('3', datetime.time(0,30), 'Kettlebells offer a different kind of class training using dynamic moves targeting almost every aspect of fitness, endurance, strength, balance, agility and cardio endurance.', 'Advanced Kettlebells')
activity_repository.save(activity24)

activity25 = Activity('2', datetime.time(0,30), 'Kettlebells offer a different kind of class training using dynamic moves targeting almost every aspect of fitness, endurance, strength, balance, agility and cardio endurance.', 'Intermediate Kettlebells')
activity_repository.save(activity25)

activity26 = Activity('1', datetime.time(0,30), 'Kettlebells offer a different kind of class training using dynamic moves targeting almost every aspect of fitness, endurance, strength, balance, agility and cardio endurance.', 'Beginners Kettlebells')
activity_repository.save(activity26)


## INSTRUCTORS ##

instructor1 = Instructor('Wayne', 'Buttler', 'x4567')
instructor_repository.save(instructor1)

instructor2 = Instructor('Katy', 'Robertson', 'x4544')
instructor_repository.save(instructor2)

instructor3 = Instructor('Derek', 'Oliver', 'x4599')
instructor_repository.save(instructor3)

instructor4 = Instructor('Sophia', 'Price', 'x4521')
instructor_repository.save(instructor4)

instructor5 = Instructor('Liam', 'Harris', 'x4502')
instructor_repository.save(instructor5)


## LOCATIONS ##

location1 = Location(True, 100, 'For general use including Pilates, Zumba and Yoga', 'Main Hall')
location_repository.save(location1)

location2 = Location(False, 20, 'Light equipment use including Circuit Trainig, HIIT and Kettlebells', 'LG1')
location_repository.save(location2)

location3 = Location(False, 10, 'Boxing Ring for Kickboxing etc.', 'Ring')
location_repository.save(location3)

location4 = Location(True, 25, 'Spinning Equipment', 'G3')
location_repository.save(location4)

location5 = Location(True, 15, 'Spinning Equipment', 'G5')
location_repository.save(location5)

location6 = Location(True, 150, 'The main gym including all gym equipment', 'Main Gym')
location_repository.save(location6)

location7 = Location(False, 50, 'General use including Bootcamp, Yoga, Pilates and Zumba.', 'Anex')
location_repository.save(location7)


## BOOKINGS ##

booking1 = Booking(member2, activity21, instructor5, location7)
booking_repository.save(booking1)

booking2 = Booking(member20, activity21, instructor2, location1)
booking_repository.save(booking2)

booking3 = Booking(member14, activity13, instructor1, location5)
booking_repository.save(booking3)