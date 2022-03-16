"""
Code Inplémentant l'algorithme Knuth Morris Pratt
"""
def Naif(P, S): # P : Pattern, S: String
    p, s = len(P), len(S) # Longueur des chaines
    resultat = []
    for i in range(s-p): # Parcours de S
        j = 0
        while j < p and P[j] == S[j+i]: 
            j += 1 # caractere similaire
        if j == p: # p caracteres similaires
            resultat.append(i)
    return resultat
"""
>>> Naif("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
[15]
>>> Naif("AAAB", "AAAAAAAAAAAA") 
[]
"""
Naif("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
Naif("AAAB", "AAAAAAAAAAAA")


def Tableau(P): # P : Pattern
    T = [0] # Tableau d'indice
    j, p = 0, len(P)
    for i in range(1, p+1): # Recherche pour i
        while P[i] != P[j] and j > 0:
            j = T[j-1] 
        if P[i] == P[j]:
            j += 1
        else:
            j = 0
        T.append(j)
    return T
"""
>>> Tableau("ABCDABD")
[0, 0, 0, 0, 1, 2, 0]
>>> Tableau("AAAB")
[0, 1, 2, 0]
>>> Tableau("ABBAB")
[0, 0, 0, 1, 2]
"""
Tableau("ABCDABD")
Tableau("AAAB")
Tableau("ABBAB")
    
def Recherche(P, S, T): # Pattern String Tableau
    p, s = len(P), len(S)
    i, m = 0, 0 # i parcourt P, m parcourt S
    resultat = []
    while m + i < s: # Parcourt de S
        if P[i] == S[m + i]: # Meme caractere
            i += 1
            if i == p: # On trouve P dans S
                resultat.append(m)
                m += i - T[i-1]
                i = T[i-1]
        elif i > 0: # Modifie m en fonction de T
            m += i - T[i-1]
            i = T[i-1]
        else:
            m += i + 1
    return resultat

"""
>>> P = "ABCDABD"
>>> S = "ABC ABCDAB ABCDABCDABDE"
>>> Recherche(P, S, Tableau(P))
[15]
>>> Recherche("AAAB", "AAAAAAAAAAAA", Tableau("AAAB"))
[]
>>> Recherche("ABBAB", "ABBABBABCD", Tableau("ABBAB"))
[0, 3]
"""

P = "ABCDABD"
S = "ABC ABCDAB ABCDABCDABDE"
Recherche(P, S, Tableau(P))
Recherche("AAAB", "AAAAAAAAAAAA", Tableau("AAAB"))
Recherche("ABBAB", "ABBABBABCD", Tableau("ABBAB"))


