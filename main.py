import smtplib
from conf_data import email, email_password


def send_email(message):
    sender = email
    password = email_password

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please'

def main():
    message = 'This message means nothing.'
    print(send_email(message))



if __name__ == '__main__':
    main()