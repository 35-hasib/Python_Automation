import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('35.mlwbd@gmail.com','tdftewfswonnnhoe')
server.sendmail('35.mlwbd@gmail.com','hrrahman35@gmail.com','Codeforces mission Completed')

print('mail sent')

