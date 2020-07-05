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
import ctypes


def call():
    gmail_user = "your_mail"
    gmail_pwd = "your_password"
    FROM = 'your_mail'
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
        server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn'
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        ctypes.windll.user32.MessageBoxW(0, "Mail Sent Successfully",
                                         "                            Pain Detected                            ", 0)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Failed to send mail",
                                         "                            Pain Detected                            ", 0)
