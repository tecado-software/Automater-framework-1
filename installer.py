import subprocess
try:
    print("    _         _                        _            ")
    print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
    print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
    print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |   ")
    print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @Kr0n0s")
    print()
    print("Installer for OS that have apt for package manager")
    print("[+] Updating repository...")
    subprocess.run("apt update", shell=True)
    print("[+] Installing aircrack-ng...")
    subprocess.run("apt install -y aircrack-ng", shell=True)
    print("[+] Installing nikto...")
    subprocess.run("apt install -y nikto", shell=True)
except:
    print("There is some error... Quitting")
