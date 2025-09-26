#### Fonctions secondaires
"""
utilisation de listes pour la suite de syracuse 
et création d'un graphique 
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    création d'un graphique avec l'utilisation de la liste
    crée par notre deuxième fonction
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    liste = [n]
    # tant que la suite n'est pas terminée :
    while n!=1 :
    #   - calcul du n suivant
        if n%2==0 :
            n=n//2
        else :
            n=n*3+1
        liste.append(n)
    return liste
def temps_de_vol(liste):
    """Retourne le temps de vol d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol
    """
    return len(liste) - 1
def temps_de_vol_en_altitude(liste):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici

    u0 = liste[0]
    for k in range(len(liste) - 1):
        if liste[k+1] < u0:
            return k
    return 0


def altitude_maximale(liste):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(liste)


#### Fonction principale


def main():
    """
    permet d'appliquer toutes les fonctions crées avec 15 en départ 
    """
# vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))
if __name__ == "__main__":
    main()
