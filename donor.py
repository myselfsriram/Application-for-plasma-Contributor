#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
name=form.getvalue("name").upper()
city=form.getvalue("city").upper()
phone=form.getvalue("phone").upper()
blood=form.getvalue("blood").upper()
mail=form.getvalue("mail")
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
from firebase import firebase
firebase=firebase.FirebaseApplication("https://plasma-donor-application-default-rtdb.firebaseio.com",None)
data={
    "Name":name,
    "City":city,
    "Phone Number:":phone,
    "Blood":blood,
    "Mail id":mail
}
result=firebase.post("https://plasma-donor-application-default-rtdb.firebaseio.com/donor",data)
print("<html><head></head><link rel='stylesheet' href='style.css'>")
print("<script>alert('Details are updated');</script>")
print("<h1>Details are updated</h1><br>")
print("<h1>We will update you if any receiver want your help means</h1>")
print("<br><h2>Thank you for using our applicationhave a nice day</h2>")
print("<br><h2>We will be notify through mail have a nice day</h2>")
if __name__ == '__main__':
            msg="Thank you Register yourself, in this application. Have a nice day . We will notify who need your help through mail."
            email_alert("Notify",msg,mail)
print("</body></html>")