J='. Le PGCD de deux nombres est le plus grand nombre qui divise a la fois les deux nombres.'
I='Le PGCD de'
H=False
G='et'
L=True
F=range
D='est'
E=int
C=input
A=print
def B(*D):
	B=''
	for E in D:B+=str(E)+' '
	for C in F(0,len(B),28):A(B[C:C+28])
def S(a,b):A=a//b;B('La division entiere de ',a,'par',b,D,A,". C'est le quotient de la division euclidienne de a par b, c'est a dire le nombre de fois que b peut être retire a a.");return A
def T(a,b,mod):A=mod;C=a%b==A;B('La congruence de',a,'modulo',b,'egale a',A,'est : ',C,'. Cela signifie que le reste de la division euclidienne de a par b est egal a ',A);return C
def U(n):
	A=[]
	for C in F(1,n+1):
		if n%C==0:A.append(C)
	B('Les diviseurs de',n,'sont :',A,'. Ce sont tous les nombres qui peuvent être utilises pour diviser ',n,' sans avoir de reste.');return A
def V(n,limite):
	D=limite;A=[];C=1
	while C*n<D:A.append(C*n);C+=1
	B('Les multiples de',n,'inferieurs a',D,'sont : ',A,'. Ce sont tous les nombres qui peuvent être obtenus en multipliant ',n,' par un entier.');return A
def O(n):
	C="n'est pas premier. Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même."
	if n<2:B(n,C);return H
	for A in F(2,E(n**0.5)+1):
		if n%A==0:B(n,C);return H
	B(n,"est premier. Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même.");return L
def P(a,b,show=L):
	if b==0:
		if show:B(I,a,G,b,D,a,J)
		return a
	else:
		for A in F(min(a,b),0,-1):
			if a%A==0 and b%A==0:
				if show:B(I,a,G,b,D,A,J)
				return A
def W(a,b):A=a*b//P(a,b,H);B('Le PPCM de',a,G,b,D,A,'. Le PPCM de deux nombres est le plus petit nombre qui est divisible a la fois par a et par b.');return A
def Q(a,b,show=L):
	if b==0:B(I,a,G,b,D,a,J);return a
	else:C=a//b;A=a%b;B(a,'=',b,'*',C,'+',A);return Q(b,A)
def K():
	R='+-----------------------------+';N='Entrez le nombre: ';M='Entrez le premier nombre: ';K='Entrez le deuxième nombre: ';I='Résultat:'
	while L:
		A(R);A('| Menu | v1 | www.androne.dev |');A(R);A('| 1. | Division entière       |');A('| 2. | Congruence             |');A("| 3. | Tous les diviseurs d'un nombre");A("| 4. | Tous les multiples d'un nombre");A('| 5. | Nombres premiers       |');A("| 6. | Fonction 'estPremier'  |");A('| 7. | PGCD                   |');A('| 8. | PPCM                   |');A("| 9. | Algorithme d'Euclide   |");A('| 0. | Quitter                |');A(R);F=C('Entrez votre choix: ')
		if F=='1':B("Division entière : La division entière de a par b est le quotient de la division euclidienne de a par b, c'est a dire le nombre de fois que b peut être retire a a.");G=E(C(M));H=E(C(K));D=S(G,H);A(I,D)
		elif F=='2':B('Congruence : Deux nombres a et b sont congrus modulo n si le reste de la division euclidienne de a par n est égal au reste de la division euclidienne de b par n.');G=E(C(M));H=E(C(K));X=E(C('Entrez le module: '));D=T(G,H,X);A(I,D)
		elif F=='3':B("Tous les diviseurs d'un nombre : Les diviseurs d'un nombre sont tous les nombres qui divisent ce nombre.");J=E(C(N));D=U(J);A(I,D)
		elif F=='4':B("Tous les multiples d'un nombre : Les multiples d'un nombre sont tous les nombres qui sont des multiples de ce nombre.");J=E(C(N));Y=E(C('Entrez la limite: '));D=V(J,Y);A(I,D)
		elif F=='5':B("Nombres premiers : Un nombre premier est un nombre entier superieur ou egal a 2 qui n'est divisible que par 1 et par lui-même.");J=E(C(N));D=O(J);A(I,D)
		elif F=='6':B("Fonction 'estPremier' : La fonction 'estPremier' renvoie True si le nombre est premier et False sinon.");J=E(C(N));D=O(J);A(I,D)
		elif F=='7':B('PGCD : Le PGCD de deux nombres est le plus grand nombre qui divise a la fois les deux nombres.');G=E(C(M));H=E(C(K));D=P(G,H);A(I,D)
		elif F=='8':B('PPCM : Le PPCM de deux nombres est le plus petit nombre qui est divisible a la fois par a et par b.');G=E(C(M));H=E(C(K));D=W(G,H);A(I,D)
		elif F=='9':B("Algorithme d'Euclide : L'algorithme d'Euclide permet de calculer le PGCD de deux nombres.");G=E(C('Entrez le premier nombe: '));H=E(C(K));D=Q(G,H);A(I,D)
		elif F=='0':break
		else:A('Choix non valide. Veuillez réessayer.')
		Z=C('Voulez-vous continuer (O/n)? ')
		if Z=='n':break
K()