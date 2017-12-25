#  
#  ContactList.py
#  ContactList
#  
#  Created by tangluna on 06.27.2017.
#  Copyright © 2017 tangluna. All rights reserved.
#  

"""what the program does... BLAH BLAH BLAH"""
Contacts = open("Contacts.csv", "r+")
na = ""
nu = ""
ad = ""
co = ""

ok = 0
def rightFunc(right, Contacts, na, nu, ad, co):
    if right == "Y":
        print "Adding contact..."
        newCont = "\n" + na + "," + nu + "," + ad + "," + co
        Contacts.close()
        C = open("Contacts.csv", "a")
        C.write(newCont)
        C.close()
        Contacts = open("Contacts.csv", "r")
        print "Contact Added!"
        lookup = raw_input("Would you like to look up another name in the address book?(Y/N) ")
        lookUpFunc(lookup.upper(), Contacts)
    elif right == "N":
        print "Okay! Please re-enter the information."
        addContact(Contacts)
    else:
        print "Sorry! I don't understand what you're trying to say! Please only use \"Y\" or \"N\" as an answer."
        right = raw_input("Is this information correct?(Y/N)")
        rightFunc(right.upper(), Contacts, na, nu, ad, co)
def addContact(Contacts):
    na = raw_input("Full Name? ")
    nu = raw_input("Number? ")
    ad = raw_input("Address? ")
    co = raw_input("Comment? ")
    print ""
    print "Name: " + na
    print "Phone Number: " + nu
    print "Address: " + ad
    print "Comment: " + co
    right = raw_input("Is this information correct?(Y/N)")
    rightFunc(right.upper(), Contacts, na, nu, ad, co)

def addOrNotFunc(addOrNot, Contacts):
    if addOrNot == "Y":
        addContact(Contacts)
    elif addOrNot == "N":
        startOverOrNot = raw_input("Okay! Would you like to look up another name in the address book?(Y/N) ")
        if startOverOrNot == "Y":
            lookup = "Y"
            lookUpFunc(lookup.upper(), Contacts)
        elif startOverOrNot == "N":
            print "Okay! Closing address book."
        else:
            print "Sorry! I don't understand what you're trying to say! Please only use \"Y\" or \"N\" as an answer."
            lookup = raw_input("Would you like to look up another name?(Y/N) ")
            lookUpFunc(lookup.upper(), Contacts)
    else:
        print "Sorry! I don't understand what you're trying to say! Please only use \"Y\" or \"N\" as an answer."
        addOrNot = raw_input("Would you like to add a name to the address book?(Y/N) ")
        addOrNotFunc(addOrNot.upper(), Contacts)

def pullName(name, Contacts):
    print ""
    n = ""
    b = 0
    tl = "."
    while tl != "":
        n = ""
        tl = Contacts.readline()
        for i in tl:
            if i != ",":
                n += i
            else:
                if n.lower() == name.lower():
                    print "Name: " + n
                    p = ""
                    a = ""
                    charNum = 0
                    for l in range(1, len(tl)):
                        if tl[l] == ",":
                            for j in range(1, len(tl)):
                                if tl[l + j] != ",":
                                    p += tl[l + j]
                                elif tl[l + j] == ",":
                                    for k in range(1, len(tl)):
                                        if tl[l + j + k] != ",":
                                            a += tl[l + j + k]
                                            charNum = l + k + j
                                        else:
                                            break
                                    break
                            break
                    print "Phone Number: " + p
                    print "Address: " + a
                    print "Comment: " + tl[(charNum + 2):len(tl)]
                    print ""
                    b = 1
    else:
        if b == 0:
            print "Sorry, that name is not in the address book!"
            Contacts.seek(0)
            addOrNot = raw_input("Would you like to add it?(Y/N) ")
            addOrNotFunc(addOrNot.upper(), Contacts)
    if b == 1:
        Contacts.seek(0)
        lookup = raw_input("Would you like to look up another name in the address book?(Y/N) ")
        lookUpFunc(lookup.upper(), Contacts)
def lookUpFunc(look, Contacts):
    if look == "Y":
        name = raw_input("Name? ")
        pullName(name.upper(), Contacts)
    elif look == "N":
        print "Okay! Closing address book."
    else:
        print "Sorry! I don't understand what you're trying to say! Please only use \"Y\" or \"N\" as an answer."
        lookup = raw_input("Would you like to look up a name?(Y/N) ")
        lookUpFunc(lookup.upper(), Contacts)

lookUp = raw_input("Welcome! You have opened the address book! Would you like to look up a name?(Y/N) ")
lookUpFunc(lookUp.upper(), Contacts)
Contacts.close()
