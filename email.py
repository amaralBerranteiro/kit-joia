def send_email(subject, body, recipient):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('johannesmaravieskiamaral@gmail.com', '24102007')

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = 'johannesmaravieskiamaral@gmail.com'
        message['To'] = recipient

        server.sendmail('johannesmaravieskiamaral@gmail.com', recipient, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False