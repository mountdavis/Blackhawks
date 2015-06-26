import os
import string
import time

prompt = ">"

def isdatevalid (yyyy,mm,dd):
    correctDate = None
    try:
        newDate = datetime.datetime(yyyy,mm,dd)
        correctDate = True
    except ValueError:
        correctDate = False
    print(str(correctDate))

print "enter your date of birth and your last name"
print "Please enter your date of birth:"
print "year of birth: (yyyy)"
dobyyyy = raw_input(prompt)
print "month of birth: (mm)"
dobmm = raw_input(prompt)
print "days of birth: (dd)"
dobdd = raw_input(prompt)
#check the date is valid or not
isdatevalid(dobyyyy, dobmm, dobdd)
print "Please enter your last name"
lastname = raw_input(prompt2)

print "your date of birth and last name as follow"
print lastname +" "+ dob
