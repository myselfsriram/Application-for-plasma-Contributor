#!C:/Users/ACER/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type:text/html")
print()
import cgi
from logging import exception
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
new_name=[]
new_phone=[]
new_city=[]
for i in blood1:
    for j in city1:
        if(blood==i and city==j):
            k=blood1.index(i)
            new_name.append(name[k])
            new_city.append(city1[k])
            new_phone.append(phone1[k])
            name.pop(k)
            city1.pop(k)
            phone1.pop(k)
            flag=1
            break
if(flag==0):
    print("No persons are in our database")
if(flag==1):
    try:
        print("<html><head></head><body><link rel='stylesheet' href='style.css'>")
        print("<p><h2>Who do you wish to contact</h2><p>")
        for i in new_name:
            print("<h3>",i,"<h3>")
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
def new():
    n=new_city
    k=new_name
    l=new_phone
