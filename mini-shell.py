import os

history = []

def mini_shell():
    while True:  #Boucle principale : lire les commandes 
        cmd = input("myshell> ").strip()
        if not cmd:
            continue
        history.append(cmd)

        if cmd == "exit":                       # Quitter le shell
            break
        elif cmd == "pwd":                      # Afficher le répertoire courant
            print(os.getcwd())
        elif cmd.startswith("cd "):             # Changer de répertoire
            path = cmd[3:].strip()
            try:
                os.chdir(path)
            except Exception as e:
                print("Erreur :", e)
        elif cmd == "clear":                    # Nettoyer le terminal
            os.system("cls" if os.name == "nt" else "clear")
        elif cmd == "help":                     # Aide affichée à l'utilisateur
            print("Commandes disponibles : cd <chemin>, pwd, clear, help, history, exit")
        elif cmd == "history":                  # Historique des commandes
            for i, h in enumerate(history, 1):
                print(f"{i}: {h}")
        else:
            try:
                os.system(cmd)
            except Exception as e:
                print("Erreur :", e)

if __name__ == "__main__":
    mini_shell()