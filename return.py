def calcDollar(c,m):
    amount = float(m) - float(c)
    if '.' in c:
        s = c.split('.')
        return (int(amount),100 - int(s[1]))
    else:
        return (int(amount),0)

def calcQuarter(changeDollar):
    q=0
    changeQuarter = changeDollar
    while changeQuarter >= 25:
        q+=1
        changeQuarter = changeQuarter - 25
    return (q,changeQuarter)

def calcDime(changeQuarter):
    dime = 0
    changeDime = changeQuarter
    while changeDime >= 10:
        dime+=1
        changeDime = changeDime - 10
    return (dime,changeDime)

def calcNickel(changeDime):
    nickel = 0
    changeNickel = changeDime
    while changeNickel >= 5:
        nickel+=1
        changeNickel = changeNickel - 5
    return (nickel,changeNickel)

def calcPenny(changeNickel):
    penny=0
    changePenny = changeNickel
    while changePenny >=1:
        penny+=1
        changePenny = changePenny - 1
    return (penny,changePenny)

def userInput():
    c = raw_input("Enter cost of item")
    m = raw_input("Enter money given")
    return (c,m)

def main():
    (c,m) = userInput()

    (d,changeDollar) = calcDollar(c,m)
    if changeDollar > 0:
        if d > 0:
            print "You get back %s dollar" % int(d)

        (q,changeQuarter) = calcQuarter(changeDollar)
        if q > 0:
            print "You get back %s quarter" % int(q)

        (dime,changeDime) = calcDime(changeQuarter)
        if dime > 0:
            print "You get back %s dime" % int(dime)

        (nickel,changeNickel) = calcNickel(changeDime)
        if nickel > 0:
            print "You get back %s nickel" % int(nickel)

        (penny,changePenny) = calcPenny(changeNickel)
        if penny > 0:
            print "You get back %s penny" % int(penny)

if __name__ == "__main__":
    main()