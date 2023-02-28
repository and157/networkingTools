import pythonping,os,pysnmp
from IPy import IP

def ping():
    ipAddress = input("Please input the ip address \n")
    try:
        ping = pythonping.ping(ipAddress,count=4)
        if ping.success():
            print("Ping has been successful")
        else:
            print("Ping has been unsuccessful")
    except:
        print("Invalid IP Format")
    return

def checkSnmp():
    return
    





variable = ""
while (variable!="exit"):
    os.system('cls')
    print("Please select the function to run:")
    print("1.Check if ip is reacheable")
    print("Type exit to leave")
    variable = input("")
    match variable:
        case "1":
            ping()
        case "2":
            checkSnmp()
        case "3":
            ping()
        case "4":
            ping()
    input("Press enter to continue \n")




