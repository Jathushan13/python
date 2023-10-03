receiver_email = 'jathushan13@outlook.com'
f = open('D:\\python\passwords\gmail APass.txt','r')
password = f.readline()
bcc = ['niveathan1@outlook.com','haritpatel46050@gmail.com']
all_receiver = [receiver_email] + bcc

print("," .join(all_receiver))

print(password)
print(receiver_email)



