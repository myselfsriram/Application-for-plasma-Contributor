#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
user1=form.getvalue("username")
password1=form.getvalue("password")
fname=str(form.getvalue("fname")).upper()
lname=str(form.getvalue("lname")).upper()
mail=str(form.getvalue("email"))
phone=form.getvalue("phone")
mail=mail
password=password1
try:
  data={
    "User name":user1,
    " First Name":fname,
    "Last name ":lname,
      "Mail id"  :mail,
      "Password":password,
      "Phone ":phone
    }
  from firebase import firebase
  firebase=firebase.FirebaseApplication("https://plasma-donor-application-default-rtdb.firebaseio.com",None)
  result1=firebase.post("https://plasma-donor-application-default-rtdb.firebaseio.com/users",data)

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
  if __name__ == '__main__':
    email_alert("Thanking","Login link=http://localhost/PythonProject/login.html",mail)
    print("Check your mail box for conformation")
    
except Exception as e:
  print(e)

print("welcome ",user1)

