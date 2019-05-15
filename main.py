import argparse
import configparser
import smtplib

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

subject = "Subject Test"
message = "test message"

try:
    server = smtplib.SMTP_SSL(
        host=config['smtp.host'], port=int(config['smtp.port']))
    server.login(config['smtp.user'], config['smtp.pass'])
    server.sendmail(config['smtp.user'], recievers, message)
except smtplib.SMTPException as e:
    print("Error occurred: {error}".format(error=e))
