##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib

from datetime import datetime

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
now = datetime.now()
today = (now.month, now.day)

if today in birthdays:
    birthday = birthdays[today]
    birthday_email = birthday["email"]
    birthday_name = birthday["name"]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday["name"])

    email = input("Enter your Yahoo email address. \n")
    password = input("Enter your Yahoo email password. \n")
    recipient = birthday_email

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user= email, password= password)
        connection.sendmail(
            from_addr= email,
            to_addrs= recipient,
            msg = f"Subject: Happy Birthday {birthday_name}!\n\n{letter}"
        )
