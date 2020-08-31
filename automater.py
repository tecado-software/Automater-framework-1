import subprocess
import random

def welcome():
    var = random.randint(0,4)
    val = random.randint(0,4)
    if val == 0:
        frase = "\"si vis pacem para bellum\""
        frase1 = "Ancient Roman saying (If you want peace, prepare for war)"
    elif val == 1:
        frase = "\"Veni, vidi, vici\""
        frase1 = "Julius Caesar (I came, I saw, I conquered)"
    elif val == 2:
        frase = "\"Two things are infinite: the universe and human stupidity, but I still have doubts about the universe\""
        frase1 = "Albert Einstein"
    elif val == 3:
        frase = "\"A computer il like air conditioning. It become useless when you open Windows\""
        frase1 = "Linus Torvalds"
    else:
        frase = "\"We have problems with our physical security, operational security through to management\""
        frase1 = "Kevin Mitnick"
    if var == 0:
        print("    _         _                        _            ")
        print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ", frase)
        print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|", frase1)
        print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |    v.2.1.0")
        print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|    By @gasmat")
        print()
    if var == 1:
        print("   #                                                          ")
        print("  # #   #    # #####  ####  #    #   ##   ##### ###### #####  ")
        print(" #   #  #    #   #   #    # ##  ##  #  #    #   #      #    # ")
        print("#     # #    #   #   #    # # ## # #    #   #   #####  #    # ", frase)
        print("####### #    #   #   #    # #    # ######   #   #      #####  ", frase1)
        print("#     # #    #   #   #    # #    # #    #   #   #      #   #   v.2.1.0")
        print("#     #  ####    #    ####  #    # #    #   #   ###### #    #  By @gasmat")
    if var == 2:
        print("               _                        _            ")
        print("    /\        | |                      | |           ")
        print("   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ", frase)
        print("  / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|", frase1)
        print(" / ____ \ |_| | || (_) | | | | | | (_| | ||  __/ |    v.2.1.0")
        print("/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|    By @gasmat")
    if var == 3:
        print("    \          |                         |            ", frase)
        print("   _ \   |   | __|  _ \  __ `__ \   _` | __|  _ \  __|",frase1)
        print("  ___ \  |   | |   (   | |   |   | (   | |    __/ |    v.2.1.0")
        print("_/    _\\__,_|\__|\___/ _|  _|  _|\__,_|\__|\___|_|    By @gasmat ")
    if var == 4:
        print("   _       _                  _           ", frase)
        print("  /_\ _  _| |_ ___ _ __  __ _| |_ ___ _ _ ", frase1)
        print(" / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) '_| v.2.1.0")
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
    print("\tweevely            Generate and run webshell for website")
    print("\thttrack            Clone a website")
    print("Password:")
    print("\thydra              Password cracker for most protocols")
    print("Wi-Fi:")
    print("\taircrack-ng        Tool from the aircrack-ng suite")

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
    if module == "weevely":
        weevely()
    if module == "httrack":
        httrack()
    if module == "hydra":
        hydra()
    if module == "aircrack-ng":
        aircrack_ng()

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
    verbose = False
    vverbose = "no"
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
            print("verbose      no         ", vverbose)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
            if "verbose" in module:
                vverbose = module.replace("verbose", "")
                if vverbose == "yes" or vverbose == "no":
                    print("verbose ==>", vverbose)
                    if vverbose == "yes":
                        verbose = True
                    else:
                        verbose = False
                else:
                    print("The option verbose can be only yes or no")
                    vverbose = "no"
        if command.startswith("execute") or command.endswith("execute"):
            if verbose == False:
                shell1 = "whois " + domain
            else:
                shell1 = "whois " + domain + " --verbose"
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
    vmode = ""
    flood = False
    vflood = "no"
    verbose = False
    vverbose = "no"
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
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTION       REQUIRED    CURRENT VALUE")
            print("interface    yes        ", interface)
            print("target       yes        ", target)
            print("mode         yes        ", mode, "(must be: raw ip, icmp, udp)")
            print("flood        no         ", vflood, "(Warning: you can damage the target machine)")
            print("verbose      no         ", vverbose)
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
                if mode == "rawip" or mode == "icmp" or mode == "udp":
                    print("mode ==>", mode)
                else:
                    print("Invalid mode!")
                    mode = ""
            if "flood" in module:
                vflood = module.replace("flood", "")
                if vflood == "yes" or vflood == "no":
                    print("flood ==>", vflood)
                    if vflood == "yes":
                        flood = True
                    else:
                        flood = False
                else:
                    print("The option flood can be only yes or no")
                    vflood = "no"
            if "verbose" in module:
                vverbose = module.replace("verbose", "")
                if vverbose == "yes" or vverbose == "no":
                    print("verbose ==>", vverbose)
                    if vverbose == "yes":
                        verbose = True
                    else:
                        verbose = False
                else:
                    print("The option verbose can be only yes or no")
                    vverbose = "no"
        if command.startswith("execute") or command.endswith("execute"):
            if mode == "raw ip":
                vmode = "0"
            elif mode == "icmp":
                vmode = "1"
            elif mode == "udp":
                vmode = "2"
            if verbose == True:
                if flood == False:
                    shell1 = "hping3 -" + vmode + " -I " + interface + " " + target + " -V"
                else:
                    shell1 = "hping3 -" + vmode + " -I " + interface + " " + target + " --flood -V"
            else:
                if flood == False:
                    shell1 = "hping3 -" + vmode + " -I " + interface + " " + target
                else:
                    shell1 = "hping3 -" + vmode + " -I " + interface + " " + target + " --flood"
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
    port = "80"
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
            print("port         no         ", port)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "target" in module:
                target = module.replace("target", "")
                print("target ==>", target)
            if "port" in module:
                port = module.replace("port", "")
                print("port ==>", port)
        if command.startswith("execute") or command.endswith("execute"):
            shell1 = "nikto -host " + target + " -port " + port
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
    verbose = False
    vverbose = "no"
    listall = False
    vlistall = "no"
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
        if command.startswith("show options") or command.endswith("show options"):
            print("OPTIONS      REQUIRED    CURRENT VALUE")
            print("domain       yes        ", domain)
            print("list all     no         ", vlistall)
            print("verbose      no         ", vverbose)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "domain" in module:
                domain = module.replace("domain", "")
                print("domain ==>", domain)
            if "listall" in module:
                vlistall = module.replace("listall", "")
                if vlistall == "yes" or vlistall == "no":
                    print("list all ==>", vlistall)
                    if vlistall == "yes":
                        listall = True
                    else:
                        listall = False
                else:
                    print("The option list all can be only yes or no")
            if "verbose" in module:
                vverbose = module.replace("verbose", "")
                if vverbose == "yes" or vverbose == "no":
                    print("verbose ==>", vverbose)
                    if vverbose == "yes":
                        verbose = True
                    else:
                        verbose = False
                else:
                    print("The option verbose can be only yes or no")
        if command.startswith("execute") or command.endswith("execute"):
            if verbose == True:
                if listall == True:
                    shell1 = "wafw00f -a -v " + domain
                else:
                    shell1 = "wafw00f -v " + domain
            else:
                if listall == True:
                    shell1 = "wafw00f -a " + domain
                else:
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

def weevely():
    print("You have chosen the module: weevely")
    while True:
        command = str(input("#weevely>>>"))
        if command.startswith("help") or command.endswith("help"):
            print()
            print("This tool generate a webshell for website that use PHP.")
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow modules       Show the modules")
            print("\tuse <MODULE>       Use a module")
            print("\tback               Go back to the main menu")
        if command.startswith("show modules") or command.endswith("show modules"):
            print("MODULE       DESCRIPTION")
            print("generate     Generate the shell")
            print("run          Run the shell")
        if "use" in command:
            module1 = command.replace("use", "")
            module = module1.replace(" ", "")
            if module == "generate":
                print("You have chosen the module: generate")
                password = ""
                file0 = ""
                while True:
                    command1 = str(input("#weevely/generate>>>"))
                    if command1.startswith("help") or command1.endswith("help"):
                        print()
                        print("\tCOMMAND            DESCRIPTION")
                        print("\thelp               Show this help message")
                        print("\tshow options       Show the options to set")
                        print("\tset <OPTION>       Set the value of the <OPTION>")
                        print("\texecute            start the module")
                        print("\tback               Go back to the weevely menu")
                    if command1.startswith("show options") or command1.endswith("show options"):
                        print("OPTIONS      REQUIRED    CURRENT VALUE")
                        print("password     yes        ", password)
                        print("file         yes        ", file0, "(must finish with .php")
                    if "set" in command1:
                        module1 = command1.replace("set", "")
                        module = module1.replace(" ", "")
                        if "password" in module:
                            password = module.replace("password", "")
                            print("password ==>", password)
                        if "file" in module:
                            file0 = module.replace("file", "")
                            print("file ==>", file0)
                    if command1.startswith("execute") or command1.endswith("execute"):
                        shell1 = "weevely generate " + password + " " + file0
                        try:
                            print("[+] Running command:", shell1)
                            subprocess.run(shell1, shell=True)
                        except:
                            print("There is some trouble...")
                            print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                            print("Are you running this script on Linux?")
                    if command1.startswith("back") or command1.endswith("back"):
                        print("Exiting from module: generate")
                        break
            if module == "run":
                print("You have chosen the module: run")
                url = ""
                password = ""
                while True:
                    command1 = str(input("#weevely/run>>>"))
                    if command1.startswith("help") or command1.endswith("help"):
                        print()
                        print("\tCOMMAND            DESCRIPTION")
                        print("\thelp               Show this help message")
                        print("\tshow options       Show the options to set")
                        print("\tset <OPTION>       Set the value of the <OPTION>")
                        print("\texecute            Start the module")
                        print("\tback               Go back to the weevely menu")
                    if command1.startswith("show options") or command1.endswith("show options"):
                        print("OPTIONS      REQUIRED    CURRENT VALUE")
                        print("url          yes        ", url, "(the URL of the uploaded shell)")
                        print("password     yes        ", password)
                    if "set" in command1:
                        module1 = command1.replace("set", "")
                        module = module1.replace(" ", "")
                        if "url" in module:
                            url = module.replace("url", "")
                            print("url ==>", url)
                        if "password" in module:
                            password = module.replace("password", "")
                            print("password ==>", password)
                    if command1.startswith("execute") or command.endswith("execute"):
                        shell1 = "weevely " + url + " " + password
                        try:
                            print("[+] Running command:", shell1)
                            subprocess.run(shell1, shell=True)
                        except:
                            print("There is some trouble...")
                            print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                            print("Are you running this script on Linux?")
                    if command1.startswith("back") or command1.endswith("back"):
                        print("Exiting from module: run")
                        break
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: weevely")
            break

def httrack():
    print("You have chosen the module: httrack")
    website = ""
    directory = ""
    verbose = False
    vverbose = "no"
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
            print("directory    no         ", directory)
            print("verbose      no         ", vverbose)
        if "set" in command:
            module1 = command.replace("set", "")
            module = module1.replace(" ", "")
            if "website" in module:
                website = module.replace("website", "")
                print("website ==>", website)
            if "directory" in module:
                directory = module.replace("directory", "")
                print("directory ==>", directory)
            if "verbose" in module:
                vverbose = module.replace("verbose", "")
                if vverbose == "yes" or vverbose == "no":
                    print("verbose ==>", vverbose)
                    if vverbose == "yes":
                        verbose = True
                    else:
                        verbose = False
                else:
                    print("The option verbose can be only yes or no")
        if command.startswith("execute") or command.endswith("execute"):
            if verbose == True:
                if directory != "":
                    shell1 = "httrack " + website + " " + directory + " -v"
                else:
                    shell1 = "httrack " + website + " -v"
            else:
                if directory != "":
                    shell1 = "httrack " + website + " " + directory
                else:
                    shell1 = "httrack " + website
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
    verbose = False
    vverbose = "no"
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
            print("verbose      no         ", vverbose)
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
            if "verbose" in module:
                vverbose = module.replace("verbose", "")
                if vverbose == "yes" or vverbose == "no":
                    print("verbose ==>", vverbose)
                    if vverbose == "yes":
                        verbose = True
                    else:
                        verbose = False
                else:
                    print("The option verbose can be only yes or no")
        if command.startswith("execute") or command.endswith("execute"):
            if verbose == True:
                shell1 = "hydra -v -L " + login + " -P " + password + " " + protocol + "://" + host
            else:
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

def aircrack_ng():
    print("You have chosen the module: aircrack-ng")
    while True:
        command = str(input("#aircrack-ng>>>"))
        if command.startswith("help") or command.endswith("help"):
            print("This module make a deauth attack")
            print("Before you use this module you have to run, in another terminal, \"airmon-ng start wlan0\" and then \"airodump-ng wlan0\"")
            print("when you see your victim hit Ctrl-C and enter the command \"airmon-ng stop wlan0mon\". This allows you to get what you need")
            print()
            print("\tCOMMAND            DESCRIPTION")
            print("\thelp               Show this help message")
            print("\tshow modules       Show the modules")
            print("\tuse <MODULE>       Use a module")
            print("\tback               Go back to the main menu")
        if command.startswith("show modules") or command.endswith("show modules"):
            print("MODULE       DESCRIPTION")
            print("scan         Scan for Acces Point")
            print("deauth       Make a deauthentication attack")
        if "use" in command:
            module1 = command.replace("use", "")
            module = module1.replace(" ", "")
            if "scan" in module:
                print("You have chosen the module: scan")
                interface = ""
                channel = ""
                while True:
                    command1 = str(input("#aircrack-ng/scan>>>"))
                    if command1.startswith("help") or command1.endswith("help"):
                        print("This module make a scan for Acces Point")
                        print()
                        print("\tCOMMAND            DESCRIPTION")
                        print("\thelp               Show this help message")
                        print("\tshow options       Show the options to set")
                        print("\tset <OPTION>       Set the value of the <OPTION>")
                        print("\tstart              Start the module")
                        print("\tstop               Stop the module")
                        print("\tback               Go back to the main menu")
                    if command1.startswith("show options") or command.endswith("show options"):
                        print("OPTIONS      REQUIRED    CURRENT VALUE")
                        print("interface    yes        ", interface, "(not in monitor mode)")
                    if "set" in command1:
                        module1 = command1.replace("set", "")
                        module = module1.replace(" ", "")
                        if "interface" in module:
                            interface = module.replace("interface", "")
                            print("interface ==>", interface)
                    if command1.startswith("start") or command1.endswith("start"):
                        shell1 = "airmon-ng start " + interface
                        interface2 = interface + "mon"
                        shell2 = "airodump-ng " + interface2
                        try:
                            print("[+] Running command:", shell1)
                            subprocess.run(shell1, shell=True)
                            print("[+] Running command:", shell2)
                            subprocess.run(shell2, shell=True)
                        except:
                            print("There is some trouble...")
                            print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                            print("Are you running this script on Linux?")
                    if command1.startswith("stop") or command1.endswith("stop"):
                        interface2 = interface + "mon"
                        shell1 = "airmon-ng stop " + interface2
                        try:
                            print("[+] Running command:", shell1)
                            subprocess.run(shell1, shell=True)
                        except:
                            print("There is some trouble...")
                            print("Did you install the dependency? (there is the installer if you are using a OS with use apt as package manager)")
                            print("Are you running this script on Linux?")
                    if command1.startswith("back") or command1.endswith("back"):
                        print("Exiting from module: deauth")
                        break
            if "deauth" in module:
                print("You have chosen the module: deauth")
                interface = ""
                bssid = ""
                mac = ""
                number = ""
                channel = ""
                while True:
                    command1 = str(input("#aircrack-ng/deauth>>>"))
                    if command1.startswith("help") or command1.endswith("help"):
                        print("This module make a deauth attack")
                        print("Before you use this module you have to run, in another terminal, the module scan, and then write start")
                        print("when you see your victim hit Ctrl-C and reenter in Automater reuse the module scan, and then write stop. This allows you to get what you need")
                        print()
                        print("\tCOMMAND            DESCRIPTION")
                        print("\thelp               Show this help message")
                        print("\tshow options       Show the options to set")
                        print("\tset <OPTION>       Set the value of the <OPTION>")
                        print("\texecute            Start the module")
                        print("\tback               Go back to the main menu")
                    if command1.startswith("show options") or command.endswith("show options"):
                        print("OPTIONS      REQUIRED    CURRENT VALUE")
                        print("interface    yes        ", interface, "(not in monitor mode)")
                        print("bssid        yes        ", bssid, "(in the column BSSID)")
                        print("mac          yes        ", mac, "(in the column STATION, on the same line as the target's bssid)")
                        print("number       yes        ", number)
                        print("channel      recommended", channel, "(in the column CH, on the same line as the target's bssid)")
                    if "set" in command1:
                        module1 = command1.replace("set", "")
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
                    if command1.startswith("execute") or command1.endswith("execute"):
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
                    if command1.startswith("back") or command1.endswith("back"):
                        print("Exiting from module: deauth")
                        break
        if command.startswith("back") or command.endswith("back"):
            print("Exiting from module: aircrack-ng")
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
