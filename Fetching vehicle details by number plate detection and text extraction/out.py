#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("x")


if plate_no == "CZ20FSE":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Amaram Divija 
    License No : 100012134512
    Make / Model : BABA HYUNDAI / VERNA
    Registration Date : 17/10/2020
    Registering Authority : UJJAIN , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1854538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2031
    Fitness Upto : 4/8/2039
    </pre>''')
    print("</body>")

elif plate_no == "HR26DK8337":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Srilasya Kotagiri
    License No : 018364350292
    Make / Model : HONDA / CITY
    Registration Date : 1/12/2021
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2032
    Fitness Upto : 4/8/2040
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
