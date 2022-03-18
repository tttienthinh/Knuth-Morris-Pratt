import numpy as np

class Automate: # Automate fini à repli
    def __init__(self, n_alphabet):
        self.n_alphabet = n_alphabet
        self.n_etats = 1
        self.finaux = [False]

        self.transitions = np.zeros((1, n_alphabet))
        self.repli = [0]

        self.etat = 0
        self.mots = {}

    def parcours(self, c):
        c = int(c)
        q0 = self.etat
        q1 = self.transitions[q0, c]
        while q1 == -1:
            q0 = self.repli[q0]
            q1 = self.transitions[q0, c]
        self.etat = q1
        return q1
    
    def parcours_liste(self, l):
        finaux = []
        for i in range(len(l)):
            c = l[i]
            q = self.parcours(c)
            if self.finaux[q]:
                finaux.append((i, self.mots[q]))
        return q, finaux

    def automate_partiel(self, mot):
        n = len(mot)

        # Ajout états finaux
        finaux = [False]*n + [True]

        # Ajout Transition
        transitions = -np.ones((n+1, self.n_alphabet), dtype=int)
        transitions[0, :] = np.zeros(self.n_alphabet, dtype=int)
        for i in range(n):
            c = mot[i]
            transitions[i, c] = i+1
        
        # Ajout Repli
        repli = [0, 0]
        for i in range(1, n):
            c = mot[i]
            q = i-1
            while transitions[q, c] == -1:
                q = repli[q]
            repli.append(transitions[q, c])

        return n+1, transitions, repli

    def concate_automate(self, n1, n2, t1, t2, r1, r2): # Ajouter 2 automates ensembles
        q = 0
        t = -np.ones((n1+n2, self.n_alphabet), dtype=int)
        while (t1[q] == t2[q]).all():
            t[q] = t1[q]
            q += 1
        shift = n1 - q
        for c in range(self.n_alphabet):
            if t1[q, c] > t2[q, c]:
                t[q, c] = t1[q, c]
            else:
                t[q, c] = t2[q, c]+shift-1
        for i in range(q+1, n1):
            t[i] = t1[i]
        for i in range(q+1, n2):
            t[shift-1+i] = t2[i] + (shift-1)*(t2[i]>0)
        n = shift-1+n2
        t = t[:n, :]
        print(t)
        r = [-1]*n
        r[0] = 0
        def recherche(q, c0):
            for c in range(self.n_alphabet):
                if t[q, c] > 0:
                    print("hi", r)
                    rempli_r(q, t[q, c], c0, c)

        def rempli_r(q0, q1, c0, c1):
            if r[q1] == -1:
                i = r[q0]
                while t[i, c1] == -1:
                    i = r[i]
                r[q1] = t[i, c1]
                recherche(q1, c1)
                
        for c in range(self.n_alphabet):
            print(t[0, c], "hello")
            if t[0, c] > 0:
                r[t[0, c]] = 0
                recherche(t[0, c], c)
        return n, t, r

    def ajout(self, mot):
        n1, t1, r1 = self.n_etats, self.transitions, self.repli
        n2, t2, r2 = self.automate_partiel(mot)

        n, t, r = self.concate_automate(n1, n2, t1, t2, r1, r2)
        self.n_etats, self.transitions, self.repli = n, t, r
        self.finaux += (n-n1-1)*[False] + [True]
        self.mots[n-1] = mot


            

# Exemple
n_alphabet = 2
n_etats = 6
transitions = -np.ones((n_etats, n_alphabet), dtype=int)
transitions[0] = np.zeros(n_alphabet, dtype=int)
t = [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4), (2, 0, 5)]
for q, c, qt in t:
    transitions[q, c] = qt
repli = [0, 0, 0, 1, 2, 1]
finaux = [False, False, False, True, True, True]
mots = {
    3: "aa", 4: "ab", 5: "ba"
}
a1 = Automate(n_alphabet)
a1.n_alphabet = n_alphabet
a1.n_etats = n_etats
a1.finaux = finaux

a1.transitions = transitions
a1.repli = repli

a1.etat = 0
a1.mots = mots

s = "010111010000111110010"
L = a1.parcours_liste("010111010000111110010")
L



a = Automate(2)
a.ajout([0, 0])
a.ajout([0, 1])
a.ajout([1, 0])
a.transitions
a1.transitions
a.repli
a1.repli
a.finaux
a1.finaux
a.mots
a.parcours_liste(s)