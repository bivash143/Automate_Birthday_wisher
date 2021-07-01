#! /usr/bin/python3
import smtplib
import pandas
import datetime as dt
import random


now = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")

present_month_info = df[df["month"] == now.month]
present_date_info = present_month_info[present_month_info["day"] == now.day].to_dict("record")

for x in present_date_info:

    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter_to_send = file.read().replace("[NAME]", x["name"])

    with smtplib.SMTP("smtp.____your_smtp_url___.com", port=587) as connection:
        connection.starttls()
        connection.login(user="___your_email____@___.com", password="*****Your Password*****")
        connection.sendmail(from_addr="_____your_email__@___.com", to_addrs=x["email"], msg=f"Subject:Happy Birthday Wish\n\n{letter_to_send}")