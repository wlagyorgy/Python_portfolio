import smtplib, ssl

host = "smtp.gmail.com"
port = 456

username = "don.georgleone@gmail.com"
password = "njjbvyuwbzdbruko"

context = ssl.create_default_context()
receiver = "wlagyorgy@gmail.com"
message = """
Subject: greetings
Hello from Python Udemy Course!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

