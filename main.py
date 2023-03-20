import pythonping,os,pysnmp,pysnmp
from pysnmp.hlapi import *


def getData(ip,port,communityName,snmpVersion,ID):   #get data about certain parameter using SNMP
    request = getCmd(
    SnmpEngine(),
    CommunityData(communityName, mpModel=snmpVersion),
    UdpTransportTarget((ip,port),timeout=1.8,retries=0),
    ContextData(),
    ObjectType(ObjectIdentity(ID)))
    errorIndication, errorStatus, errorIndex, varBinds = next(request)
    if errorIndication:
        return errorIndication,404
    else:
        for x in varBinds:  
            return str(x).split("= ").pop(),200








#Cases for each option
def ping():
    ipAddress = input("Please input the ip address \n")
    try:
        ping = pythonping.ping(ipAddress,count=2)
        if ping.success():
            print("Ping has been successful")
        else:
            print("Ping has been unsuccessful")
    except:
        print("Invalid IP Format")
    return

def checkSnmp():
    ip = input("Please input the device IP: ")
    port = input("Please input the port: ")
    communityName = input("Please input the name of the community: ")
    print("Choose the SNMP version")
    print("Input 0 if SNMPVersion is 1")
    print("Input 1 if SNMPVersion is 2")
    snmpVersion = int(input(""))
    while(True):
        id = input("Please Input The OID using the following format x.x.x.x.x.x.x.x : ")
        informationFromDevice,status = getData(ip,port,communityName,snmpVersion,id)
        if status == 200:
            print(f"The value obtained was : {informationFromDevice}")
        if status == 404:
            print(f"An error has occurred : {informationFromDevice}")
        os.system('pause')
        os.system('cls')
        print("Do u want to try another OID with the same device")
        print("Input 1 for yes")
        print("Input anything else for no")
        if input() != "1":
            os.system('cls')
            break
    return
    





variable = ""
while (variable!="exit"):
    os.system('cls')
    print("Please select the function to run:")
    print("1.Check if ip is reacheable")
    print("2.Get SNMP Data from device")
    print("Type exit to leave")
    variable = input("")
    match variable:
        case "1":
            os.system('cls')
            ping()
        case "2":
            os.system('cls')
            checkSnmp()
        case "3":
            os.system('cls')
            ping()
        case "4":
            os.system('cls')
            ping()
    input("Press enter to continue \n")




