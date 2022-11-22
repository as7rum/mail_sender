import smtplib
from conf_data import email, email_password, subject
from email.mime.text import MIMEText
from ggl_sheets_con import values


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
        msg['Subject'] = subject
        server.sendmail(sender, sending_email, msg.as_string())

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please'

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

def send_email_for_all():
    
    rows_number = get_number_of_elements(values['values'])
    
    for row in range(rows_number):
        status = values['values'][row][13]
        if status == 'Письмо':
            name = values['values'][row][2].split(' ')[1]
            link = values['values'][row][3]
            sending_email = values['values'][row][8]
            send_email(name, link, sending_email, status)
            


def main():
    send_email_for_all()
    # message = 'This message means nothing.'
    # print("Number of elements in the list: ", get_number_of_elements(values['values']))



if __name__ == '__main__':
    main()