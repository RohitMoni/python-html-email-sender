import argparse
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help="Configuration section to use from the config.ini file")
args = parser.parse_args()

configParser = configparser.ConfigParser()
configParser.read('config.ini')

if args.config:
    config = configParser[args.config]
else:
    config = configParser['DEFAULT']

recievers = ['rohitmdxb@gmail.com']

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test Email with Subject"

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <h1>Test Email Header</h1>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

try:
    server = smtplib.SMTP_SSL(
        host=config['smtp.host'], port=int(config['smtp.port']))
    server.login(config['smtp.user'], config['smtp.pass'])
    failed = server.sendmail(config['smtp.user'], recievers, msg.as_string())

    for email, error in failed.items():
        print("Error occurred sending to {email}: {error}".format(email=email, error=error))

except smtplib.SMTPException as e:
    print("Error occurred: {error}".format(error=e))
