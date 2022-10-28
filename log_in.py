#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
user1=form.getvalue("username")
password1=form.getvalue("password")
from firebase import firebase
firebase=firebase.FirebaseApplication("https://plasma-donor-application-default-rtdb.firebaseio.com/",None)
result=firebase.get("https://plasma-donor-application-default-rtdb.firebaseio.com/users/","")
list=[]
users=[]
passwords=[]
for i in result:
  list.append(result[i])
for i in list:
  users.append(i["Mail id"])
  passwords.append(i["Password"])
flag=0
k=0
for j in users:
  if(user1 == j):
    k=users.index(j)
    if(password1 == passwords[k]):
      flag=1
if(flag==1):
   print("<html><head><body bgcolor='red'><a href='choose.html'><h1 align='center'>Click here to go forward</h1></a></body></head></html>")

if(flag==0):
  print("<html><head><body bgcolor='red'><a href='login.html'><h1 align='center'>Click here to go back</h1></a></body></head></html>")
  print("<script>alert('No matches in our database');</script>")
