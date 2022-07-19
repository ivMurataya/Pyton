import smtplib
my_email = "vriim360@gmail.com"
password = "enevbkiuobaptybj"
with smtplib.SMTP("smtp.gmail.com") as connection:
   connection.starttls() # Secure connection, encrypts mail
   connection.login(user=my_email, password=password)
   connection.sendmail(from_addr=my_email,to_addrs="mura.ivan@hotmail.com",
                       msg="Subject:Hello\n\nThis is the body of my email")
   connection.close()

