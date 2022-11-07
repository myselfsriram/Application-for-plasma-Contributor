#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
import cgi
from logging import exception
from operator import ne
form=cgi.FieldStorage()
blood=str(form.getvalue("blood")).upper()
city=str(form.getvalue("city")).upper()
name2=str(form.getvalue("name")).upper()
phone=form.getvalue("phone")
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
flag=0
for i in city1:
    if(city==i):
        for j in blood1:
            if (j==blood):
                k=blood1.index(j)
                print("<h2>Name:",name[k],"</h2>")
                print("<h2>City:",city1[k],"</h2>")
                flag=1
                blood1.pop(k)
                city1.pop(k)
                name.pop(k)
                
if(flag==0):
    print("No persons are in our database")
    print("</body></html>")
if(flag==1):
    try:
        print("<html><head></head><body><link rel='stylesheet' href='style.css'>")
        print("<p><h2>Who do you wish to contact</h2><p>")
        print("<form  action='display.py' method='POST'>")
        print("Name:<input type='text' placeholder='Choose donor:' name='user'><br>")
        print("Enter your mail Adddress:<input type='mail' name='email' placeholder='email@gmail.com'><br>")
        print("<input type='submit' value='submit'>")
        print("</form>")


        print("</body></html>")
    except Exception as e:
        print(e)
    try:
        from firebase import firebase
        firebase=firebase.FirebaseApplication("https://plasma-donor-application-default-rtdb.firebaseio.com",None)
        data={
            "Name":name2,
            "Request for:Blood type":blood,
            "City":city,
            }
        result1=firebase.post("https://plasma-donor-application-default-rtdb.firebaseio.com/receivers",data)
    except Exception as e:
        print(e)
