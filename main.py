def print_formatted(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "

    #split string to print every 25 characters
    for i in range(0, len(text), 25):
        print(text[i:i+25])

def div_entiere(a, b):
    resultat = a // b
    print_formatted("La division entiere de ",a, "par",b,"est",resultat,". C'est le quotient de la division euclidienne de a par b, c'est a dire le nombre de fois que b peut être retire a a.")
    return resultat

def congruence(a, b, mod):
    resultat = a % b == mod
    print_formatted("La congruence de",a,"modulo",b,"egale a",mod,"est : ", resultat,". Cela signifie que le reste de la division euclidienne de a par b est egal a ",mod)
    return resultat

def diviseurs(n):
    diviseurs = []
    for i in range(1, n + 1):
        if n % i == 0:
            diviseurs.append(i)
    print_formatted("Les diviseurs de",n,"sont :",diviseurs,". Ce sont tous les nombres qui peuvent être utilises pour diviser ",n," sans avoir de reste.")
    return diviseurs

def multiples(n, limite):
    multiples = []
    i = 1
    while i * n < limite:
        multiples.append(i * n)
        i += 1
    print_formatted("Les multiples de",n,"inferieurs a",limite,"sont : ",multiples,". Ce sont tous les nombres qui peuvent être obtenus en multipliant ",n," par un entier.")
    return multiples
def est_premier(n):
    if n < 2:
        print_formatted(n,"n'est pas premier. Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même.")
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print_formatted(n,"n'est pas premier. Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même.")
            return False
    print_formatted(n,"est premier. Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même.")
    return True
def pgcd(a, b):
    if b == 0:
        print_formatted("Le PGCD de",a,"et",b,"est",a,". Le PGCD de deux nombres est le plus grand nombre qui divise a la fois les deux nombres.")
        return a
    else:
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                print_formatted("Le PGCD de",a,"et",b,"est",i,". Le PGCD de deux nombres est le plus grand nombre qui divise a la fois les deux nombres.")
                return i
def ppcm(a, b):
    resultat = a * b // pgcd(a, b)
    print_formatted("Le PPCM de",a,"et",b,"est",resultat,". Le PPCM de deux nombres est le plus petit nombre qui est divisible a la fois par a et par b.")
    return resultat
def euclide(a, b):
    if b == 0:
        print_formatted("Le PGCD de",a,"et",b,"est",a,". Le PGCD de deux nombres est le plus grand nombre qui divise a la fois les deux nombres.")
        return a
    else:
        q = a // b
        r = a % b
        print_formatted(a,"=",b,"*",q,"+",r)
        return euclide(b, r)


#menu
def menu():
    while True:
        print("+-----------------------------+")
        print("| Menu | v1 | www.androne.dev |")
        print("+-----------------------------+")
        print("| 1. | Division entière       |")
        print("| 2. | Congruence             |")
        print("| 3. | Tous les diviseurs d'un nombre")
        print("| 4. | Tous les multiples d'un nombre")
        print("| 5. | Nombres premiers       |")
        print("| 6. | Fonction 'estPremier'  |")
        print("| 7. | PGCD                   |")
        print("| 8. | PPCM                   |")
        print("| 9. | Algorithme d'Euclide   |")
        print("| 0. | Quitter                |")
        print("+-----------------------------+")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            a = int(input("Entrez le premier nombre: "))
            b = int(input("Entrez le deuxième nombre: "))
            resultat = div_entiere(a, b)
            print("Résultat:", resultat)
        elif choix == "2":
            a = int(input("Entrez le premier nombre: "))
            b = int(input("Entrez le deuxième nombre: "))
            mod = int(input("Entrez le module: "))
            resultat = congruence(a, b, mod)
            print("Résultat:", resultat)
        elif choix == "3":
            n = int(input("Entrez le nombre: "))
            resultat = diviseurs(n)
            print("Résultat:", resultat)
        elif choix == "4":
            n = int(input("Entrez le nombre: "))
            limite = int(input("Entrez la limite: "))
            resultat = multiples(n, limite)
            print("Résultat:", resultat)
        elif choix == "5":
            n = int(input("Entrez le nombre: "))
            resultat = est_premier(n)
            print("Résultat:", resultat)
        elif choix == "6":
            n = int(input("Entrez le nombre: "))
            resultat = est_premier(n)
            print("Résultat:", resultat)
        elif choix == "7":
            a = int(input("Entrez le premier nombre: "))
            b = int(input("Entrez le deuxième nombre: "))
            resultat = pgcd(a, b)
            print("Résultat:", resultat)
        elif choix == "8":
            a = int(input("Entrez le premier nombre: "))
            b = int(input("Entrez le deuxième nombre: "))
            resultat = ppcm(a, b)
            print("Résultat:", resultat)
        elif choix == "9":
            a = int(input("Entrez le premier nombe: "))
            b = int(input("Entrez le deuxième nombre: "))
            resultat = euclide(a, b)
            print("Résultat:", resultat)
        elif choix == "0":
            break
        else:
            print("Choix non valide. Veuillez réessayer.")
        continuer = input("Voulez-vous continuer (o/n)? ")
        if continuer != "o":
            break