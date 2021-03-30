import random
import smtplib
import datetime

my_email = input("Enter your Yahoo email address. \n")
password = input("Enter your Yahoo email password. \n")
reciever = input("Enter the recieving email address. \n")

with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

now = datetime.datetime.now()
day = now.strftime("%d")

with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(
        from_addr= my_email,
        to_addrs= reciever,
        msg= f"Subject:{day} Motivation\n\n{random.choice(quotes)}"
    )

# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user= my_email, password= password)
#     connection.sendmail(
#         from_addr= my_email, 
#         to_addrs="firstlast@gmail.com", 
#         msg= "Subject:Hello\n\nThis is the body of my email."
#         )

# now = datetime.datetime.now()

# year = now.year
# month = now.month
# day_of_the_week = now.weekday()

# print(day_of_the_week)

# date_of_birth = datetime.datetime(year=1991, month=9, day=3, hour=3, minute=43, second=29)
# print(date_of_birth)