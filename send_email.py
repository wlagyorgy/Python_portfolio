import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 456

    username = "don.georgleone@gmail.com"
    password = "njjbvyuwbzdbruko"

    context = ssl.create_default_context()
    receiver = "wlagyorgy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

