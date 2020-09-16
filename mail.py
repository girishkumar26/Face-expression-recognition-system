# import RPi.GPIO as GPIO
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import sys


def call():
    gmail_user = "sender_mail"
    gmail_pwd = "sender_pwd"
    FROM = 'sender_mail'
    TO = ['receiver_mail']  # must be a list

    # IMAGE

    ##subprocess.Popen("sudo fswebcam input.jpg",shell=True).communicate()
    ##time.sleep(1)

    msg = MIMEMultipart()
    time.sleep(1)
    msg['Subject'] = "pain"

    # BODY with 2 argument

    body = "helloo"
    msg.attach(MIMEText(body, 'plain'))
    time.sleep(1)

    # IMAGE
    ##fp = open("input.jpg", 'rb')
    ##time.sleep(1)
    ##img = MIMEImage(fp.read())
    ##time.sleep(1)
    ##fp.close()
    ##time.sleep(1)
    ##msg.attach(img)
    ##time.sleep(1)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn't seem to work!
        print("smtp.gmail")
        server.ehlo()
        print("ehlo")
        server.starttls()
        print("start tls")
        server.login(gmail_user, gmail_pwd)
        print("reading mail id & password")
        server.sendmail(FROM, TO, msg.as_string())
        print("sending mail ")
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
