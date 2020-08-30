import subprocess
import random

def welcome():
    var = random.randint(0,4)
    val = random.randint(0,4)
    if val == 0:
        frase = "si vis pacem para bellum"
        frase1 = "Ancient Roman saying (If you want peace, prepare for war)"
    elif val == 1:
        frase = "Veni, vidi, vici"
        frase1 = "Julius Caesar (I came, I saw, I conquered)"
    elif val == 2:
        frase = "Two things are infinite: the universe and human stupidity, but I still have doubts about the universe"
        frase1 = "Albert Einstein"
    elif val == 3:
        frase = "A computer il like air conditioning. It become useless when you open Windows"
        frase1 = "Linus Torvalds"
    else:
        frase = "We have problems with our physical security, operational security through to management"
        frase1 = "Kevin Mitnick"
    if var == 0:
        print("    _         _                        _            ")
        print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ", frase)
        print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|", frase1)
        print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |    v.2.0.0")
        print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|    By @gasmat")
        print()
    if var == 1:
        print("   #                                                          ")
        print("  # #   #    # #####  ####  #    #   ##   ##### ###### #####  ")
        print(" #   #  #    #   #   #    # ##  ##  #  #    #   #      #    # ")
        print("#     # #    #   #   #    # # ## # #    #   #   #####  #    # ", frase)
        print("####### #    #   #   #    # #    # ######   #   #      #####  ", frase1)
        print("#     # #    #   #   #    # #    # #    #   #   #      #   #   v.2.0.0")
        print("#     #  ####    #    ####  #    # #    #   #   ###### #    #  By @gasmat")
    if var == 2:
        print("               _                        _            ")
        print("    /\        | |                      | |           ")
        print("   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ", frase)
        print("  / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|", frase1)
        print(" / ____ \ |_| | || (_) | | | | | | (_| | ||  __/ |    v.2.0.0")
        print("/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|    By @gasmat")
    if var == 3:
        print("    \          |                         |            ", frase)
        print("   _ \   |   | __|  _ \  __ `__ \   _` | __|  _ \  __|",frase1)
        print("  ___ \  |   | |   (   | |   |   | (   | |    __/ |    v.2.0.0")
        print("_/    _\\__,_|\__|\___/ _|  _|  _|\__,_|\__|\___|_|    By @gasmat ")
    if var == 4:
        print("   _       _                  _           ", frase)
        print("  /_\ _  _| |_ ___ _ __  __ _| |_ ___ _ _ ", frase1)
        print(" / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) '_| v.2.0.0")
        print("/_/ \_\_,_|\__\___/_|_|_\__,_|\__\___|_|   By @gasmat")

def help():
    welcome()
    print("This is an automated framework for newbie and for lazy people")
    print("I AM NOT RESPONSIBLE FOR THE USE YOU WILL HAVE WITH MY PROJECT!")
    print()
    print("COMMAND              DESCRIPTION")
    print("help                 Show this help message")
    print("list all             List all tool")
    print("use <MODULE>         Use the selected module")
    print("clear                Clear the screen")
    print("exit                 Exit the framework")

def list_all():
    print()
    print("Information gathering:")
    print("\tmetagoofil         Collects gathering metadata")
    print("\twhois              Provide names, physical address, phone number, etc... of a domain")
    print("\tdeep magic         Set of tools for information gathering")
    print("\thping3             Detect if the target is alive")
    print("Scanner:")
    print("\tnikto              Make a vulnerability scanner")
    print("\twafw00f            Scan for web application firewall")
    print("Website:")
    print("\thttrack            Clone a website")
    print("Password:")
    print("\thydra              Password cracker for most protocols")
    print("Wi-Fi:")
    print("\tdeauth             Make a deauth attack")

def clear():
    subprocess.run("clear", shell=True)

def use():
    module1 = command.replace("use ", "")
    module = module1.replace(" ", "")
    if module == "metagoofil":
        metagoofil()
    if module == "whois":
        whois()
    if module == "deepmagic":
        deep_magic()
    if module == "hping3":
        hping3()
    if module == "nikto":
        nikto()
    if module == "wafw00f":
        wafw00f()
    if module == "httrack":
        httrack()
    if module == "hydra":
        hydra()
    if module == "deauth":
        deauth()

def metagoofil(): 
    print("You have chosen the module: metagoofil")
    domain = ""
    file0 = ""
    while True:
        command = str(input("#metagoofil>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module collects information (file), and shows: owner the creation date, etc...")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
            if "file" in module:
                file0 = module.replace("file", "")
                print("file ==>", file0)
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("domain       yes        ", domain)
            print("file         yes        ", file0)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "metagoofil -d " + domain + " -t " + file0
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: metagoofil")
            break

def deep_magic(): 
    print("You have chosen the module: deep magic")
    domain = ""
    while True:
        command = str(input("#deep magic>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This all-in-one tool include some of the most important tool (whois, netcraft, ecc...) for information gathering")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTION       REQUIRED    CURRENT VALUE")
            print("domain       yes        ", domain)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "dmitry -winsepfb " + domain
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: deep magic")
            break

def whois():
    print("You have chosen the module: whois")
    domain = ""
    while True:
        command = str(input("#whois>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This tool provide names, physical address, phone number, etc... of a given domain")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTION       REQUIRED    CURRENT VALUE")
            print("domain       yes        ", domain)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "whois " + domain
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: whois")
            break

def hping3(): 
    print("You have chosen the module: hping3")
    interface = ""
    target = ""
    mode = ""
    while True:
        command = str(input("#hping3>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module check if target is alive")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("interface") or command.endswith("interface"):
            interface1 = command.replace("interface", "")
            interface = interface1.replace(" ", "")
            print("interface ==>", interface)
        if command.startswith("target") or command.endswith("target"):
            target1 = command.replace("target", "")
            target = target1.replace(" ", "")
            print("target ==>", target)
        if command.startswith("mode") or command.endswith("mode"):
            mode1 = command.replace("mode", "")
            mode = mode1.replace(" ", "")
            print("mode ==>", mode)
            if not(mode == "raw ip" or mode == "icmp" or mode == "udp"):
                print("Invalid mode!")
                mode = ""
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTION       REQUIRED    CURRENT VALUE")
            print("interface    yes        ", interface)
            print("target       yes        ", target)
            print("mode         yes        ", mode, "(must be: raw ip, icmp, udp)")
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "interface" in module:
                interface = module.replace("interface", "")
                print("interface ==>", interface)
            if "target" in module:
                target = module.replace("target", "")
                print("target ==>", target)
            if "mode" in module:
                mode = module.replace("mode", "")
                if not(mode == "rawip" or mode == "icmp" or mode == "udp"):
                    print("Invalid mode!")
                    mode = ""
                else:
                    print("mode ==>", mode)
        if command.startswith("execute") or command.endswith("execute"):
            if mode == "raw ip":
                vmode = "0"
            elif mode == "icmp":
                vmode = "1"
            elif mode == "udp":
                vmode = "2"
            shell1 = "hping3 -" + vmode + " -I " + interface + " " + target
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: hping3")
            break

def nikto(): 
    print("You have chosen the module: nikto")
    target = ""
    while True:
        command = str(input("#nikto>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module make a scan of the target with the aim of finding vulnerabilities")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTION       REQUIRED    CURRENT VALUE")
            print("target       yes        ", target)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "target" in module:
                target = module.replace("target", "")
                print("target ==>", target)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "nikto -host " + target
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: nikto")
            break

def wafw00f(): 
    print("You have chosen the module: wafw00f")
    domain = ""
    while True:
        command = str(input("#wafw00f>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module scan a domain with the aim of find a Web Application Firewall (WAF)")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("domain       yes        ", domain)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "wafw00f " + domain
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: wafw00f")
            break

def httrack():
    print("You have chosen the module: httrack")
    website = ""
    directory = ""
    while True:
        command = str(input("#httrack>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This tool can copy a website in a your computer directory")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("website      yes        ", website)
            print("directory    yes        ", directory)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "website" in module:
                website = module.replace("website", "")
                print("website ==>", website)
            if "directory" in module:
                directory = module.replace("directory", "")
                print("directory ==>", directory)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "httrack " + website + " " + directory + " -v"
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: httrack")
            break


def hydra():
    print("You have chosen the module: hydra")
    protocol = ""
    host = ""
    login = ""
    password = ""
    protocol = ""
    while True:
        command = str(input("#hydra>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("One of the best tool for password cracking")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("host         yes        ", host)
            print("login        yes        ", login, "(must be a file)")
            print("password     yes        ", password, "(must be a file)")
            print("protocol     yes        ", protocol, "(ftp, smb, pop3, imap, mysql, vnc, ssh and telnet)")
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "host" in module:
                host = module.replace("host", "")
                print("host ==>", host)
            if "login" in module:
                login = module.replace("login", "")
                print("login ==>", login)
            if "password" in module:
                password = module.replace("password", "")
                print("password ==>", password)
            if "protocol" in module:
                protocol = module.replace("protocol", "")
                if protocol == "ftp" or protocol == "smb" or protocol == "pop3" or protocol == "imap" or protocol == "mysql" or protocol == "vnc" or protocol == "ssh" or protocol == "telnet":
                    print("protocol ==>", protocol)
                else:
                    protocol = ""
                    print("Invalid protocol!")
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "hydra -L " + login + " -P " + password + " " + protocol + "://" + host
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
            except:
                print("There is some trouble...")
                print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                print("Are you running this script on Linux?")
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: hydra")
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
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow options       Show the options to set")
            print("\tset <OPTION>       Set the value of the <OPTION>")
            print("\texecute            Start the tool")
            print("\tback               Go back to the main menu")
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("interface    yes        ", interface, "(not in monitor mode)")
            print("bssid        yes        ", bssid, "(in the column BSSID)")
            print("mac          yes        ", mac, "(in the column STATION, on the same line as the target's bssid)")
            print("number       yes        ", number)
            print("channel      recommended", channel, "(in the column CH, on the same line as the target's bssid)")
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "interface" in module:
                interface = module.replace("interface", "")
                print("interface ==>", interface)
            if "bssid" in module:
                bssid = module.replace("bssid", "")
                print("bssid ==>", bssid)
            if "mac" in module:
                mac = module.replace("mac", "")
                print("mac ==>", mac)
            if "number" in module:
                number = module.replace("number", "")
                print("number ==>", "")
            if "channel" in module:
                channel = module.replace("channel", "")
                print("channel ==>", channel)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "airmon-ng start " + interface + " " + channel
            interface2 = interface + "mon"
            shell2 = "aireplay-ng -0 " + number + " -a " + bssid + " -c " + mac + " " + interface2
            try:
                print("[+] Running command:", shell1)
                subprocess.run(shell1, shell=True)
                print("[+] Running command:", shell2)
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
    if command.startswith("list all") or command.endswith("list all"):
        list_all()
    if "use" in command:
        use()
    if command.startswith("clear") or command.endswith("clear"):
        clear()
    if command.startswith("exit") or command.endswith("exit"):
        print("See you at the next hack ;-)")
        break
