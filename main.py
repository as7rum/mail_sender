import smtplib
from conf_data import email, email_password, subject
from email.mime.text import MIMEText




def send_email(name, link, sending_email, status):
    sender = email
    password = email_password

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    # name = 'Евгений Онегин'
    # link = 'This is link, you know?'

#     text = f"""
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1>...</h1>
#     <span>Здравствуйте, {name}!</span>
# </body>
# </html>
#     """

    try:
        with open('RRC.html') as file:
            template = file.read()
            template = template.replace('PASTE_THE_NAME', name)
            template = template.replace('PASTE_THE_LINK', link)

    except IOError:
        return "The template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, 'html')
        msg['From'] = sender
        msg['To'] = sending_email
        msg['Subject'] = subject
        server.sendmail(sender, sending_email, msg.as_string())

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please'

def main():
    name = 'Тест'
    link = 'https://redcrossdonation.su/action.php?id=3727364&reactAgent=570160024'
    sending_email = 'test-8k7xconnk@srv1.mail-tester.com'
    status = 'Письмо'
    
    print(send_email(name, link, sending_email, status))




if __name__ == '__main__':
    main()