#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
print("<html><head><head><body>")
print("<link rel='stylesheet' href='style.css'>")
import smtplib
from email.message import EmailMessage
def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    user="sssminiproject@gmail.com"
    msg['from']=user
    password="zxgtwbgycbrzejuj"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
import cgi
form=cgi.FieldStorage()
user=(str(form.getvalue("user"))).upper()
mail=form.getvalue("email")
from firebase import firebase
firebase=firebase.FirebaseApplication("https://plasma-donor-application-default-rtdb.firebaseio.com/",None)
result=firebase.get("https://plasma-donor-application-default-rtdb.firebaseio.com/donor","")
list=[]
blood1=[]
city1=[]
name=[]
phone1=[]
for i in result:
    list.append(result[i])
for i in list:
    blood1.append(i["Blood"])
    phone1.append(i["Phone Number:"])
    name.append(i["Name"])
    city1.append(i["City"])
print("<h2>Details are")
for i in name:
    if(user==i):
        k=name.index(i)
        print("<h2> Phone number:",phone1[k],"</h2><br>")
        print("<h2>City:",city1[k],"</h2><br>")
        if __name__ == '__main__':
            msg="This person requested {} Requested Plasma at {} Phone number was: {}".format(user,city1[k],phone1[k])
            email_alert("Notify",msg,mail)
        break
        

print("</body></html>")