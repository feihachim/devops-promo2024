appreciation = int(
    input("Veuillez enter une note d'appréciation comprise entre 1 et 5\n")
)

if appreciation >= 1 and appreciation <= 2:
    print(":(")
elif appreciation == 3:
    print(":|")
elif appreciation >= 4 and appreciation <= 5:
    print(":)")
else:
    print("ERREUR")
