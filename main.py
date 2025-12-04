"""Code permettant de compter les occurences à la suite de lettres dans une chaine de caractères"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
       passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    char = [s[0]]
    iterations = [1]
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            iterations[-1] += 1
        else:
            char.append(s[i])
            iterations.append(1)
    return list(zip(char, iterations))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
       passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if len(s)==0:
        return []
    char = s[0]
    iterations = 1
    while(iterations <len(s) and s[iterations] == s[0]):
        iterations += 1
    return[(char,iterations)] + artcode_r(s[iterations:])

def main():
    """Permet de tester nos fonctions"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
