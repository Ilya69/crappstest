import random
print ("works bitches")
point = (random.randrange(1,6))

point = (random.randrange(1,6))
stevemoney = 1000
davemoney = 1000
davesbet_passorfail = input("dave pass or fail")

betpass = None
fail = None

davebet= int(input("hoq much is thw bet between 0 and 1000"))
firstdice = (random.randrange(1,6))
seconddice = random.randrange(1,6)



def craps( firstdice,seconddice,stevemoney, ):
    if (firstdice + seconddice) == 7:
        stevemoney / 2
        print("craps")



def roll( firstdice,seconddice,davebet,stevemoney ):
    firstdice = (random.randrange(1, 6))
    if davesbet_passorfail == "pass":

        seconddice = random.randrange(1, 6)

    print(firstdice, seconddice)
    point = int(input("pick your point"))
    point = (random.randrange(1, 6))
    #print "First, thou shalt count to {0}"
    #print("thiiiis is the point % ('walked', point,davemoney")
    #print("{0} this is your point").format(point)
    'this is your point, %s' % point
   # print('Your point' % point)

    if (point == firstdice +seconddice ):
        #davemoney = davemoney * 2
        print(point)
    if (firstdice + seconddice == 2 or 3 or 12):
        davebet = davebet * 2
        print("{0}  you win ".format(davemoney))
        print (" you alrady won on 2 3 or 12 I dont know how to make it stop doing it")

def pasorfail(firstdice,seconddice,davesbet_passorfail,davebet,point,davemoney):
    if (davesbet_passorfail == "pass")  and (firstdice + seconddice) == point :
        point = (random.randrange(1, 6))


        davemoney = davemoney * 2
        betpass = 1

    elif (davesbet_passorfail == "fail"):
        if (davesbet_passorfail == "fail") and (firstdice + seconddice) == point:
            davemoney = davemoney /2

        fail = 1





    elif seconddice == 7 or 11:
        davebet = davebet / 2
        print("{0} double up ".format(davemoney))

    elif (firstdice or seconddice) == point:
        davebet = davebet * 2
    elif firstdice + seconddice == 7:
        print("crapps unlucky")
    while (firstdice + seconddice) != 7:
        while  (point == firstdice + seconddice):
            print(point)

            stevemoney = stevemoney *2

        print("you have {0}.".format(davemoney*2))
        firstdice = (random.randrange(1, 6))
        seconddice = random.randrange(1, 6)

        break


def pasorfail(firstdice,seconddice,davesbet_passorfail):
    if (davesbet_passorfail == "pass") :
        betpass = 1
    elif (davesbet_passorfail == "pass"):
        fail = 1
craps(firstdice,seconddice,stevemoney)

pasorfail(firstdice,seconddice,davesbet_passorfail)
roll(firstdice,seconddice,davebet,stevemoney)




