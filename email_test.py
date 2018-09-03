import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ethanczc.rpi@gmail.com','zaq1@wsx')

msg='test from raspberry pi'

server.sendmail('ethanczc.rpi@gmail.com','ethanczc@gmail.com',msg)
print('email sent')
server.quit()