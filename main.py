import ephem#module d'éphémérides astronomiques
import matplotlib.pyplot as plt
import datetime#Gestion des dates
import matplotlib.font_manager#pour un caractère spécifique d'une police

#Récupération du caractère "Demi-Lune" dans la police DejaVuSans :
"""
ATTENTION : le chemin indiqué entre guillemets ci-dessous est celui de la police DeJaVuSans,
installée sur l'ordinateur.
Ce chemin doit  être adapté à votre ordinateur.
"""
path ='C:\\Users\\HP\\dejavu-sans\\DejaVuSans.ttf'#chemin de cette police sur le disque
f0 = matplotlib.font_manager.FontProperties()
f0.set_file(path)

annee=2024#AU CHOIX DE L'UTILISATEUR

#Définitions des fonction de recherche des phases, au cours d'un mois
def NouvelleLune(date_debut, date_fin):
    Date=date_debut
    while Date<date_fin:
        NL=ephem.next_new_moon(Date)#calcul de la prochaine date de la phase
        Date=ephem.localtime(NL)#conversion en temps local
        if Date<date_fin:
            Y=float(Date.strftime('%d'))#numéro du jour
            ax=axs[N-1]
            ax.scatter(0, -Y, c='k')#point noir
            ax.text(0.1, -Y, Date.strftime('%d %b'), va='center')

def PremierQuartier(date_debut, date_fin):
    Date=date_debut
    while Date<date_fin:
        PQ=ephem.next_first_quarter_moon(Date)#calcul de la prochaine date de la phase
        Date=ephem.localtime(PQ)#conversion en temps local
        if Date<date_fin:
            Y=float(Date.strftime('%d'))#numéro du jour
            ax=axs[N-1]
            ax.text(0, -Y, u'\u25D0', fontproperties=f0, ha='center', va='center')#symbole quartier de Lune
            ax.text(0.1, -Y, Date.strftime('%d %b'), va='center')

def PleinLune(date_debut, date_fin):
    Date=date_debut
    while Date<date_fin:
        PL=ephem.next_full_moon(Date)#calcul de la prochaine date de la phase
        Date=ephem.localtime(PL)#conversion en temps local
        if Date<date_fin:
            Y=float(Date.strftime('%d'))#numéro du jour
            ax=axs[N-1]
            ax.scatter(0,  -Y, c='w', edgecolor='k')#point blanc
            ax.text(0.1, -Y, Date.strftime('%d %b'), va='center')

def DernierQuartier(date_debut, date_fin):
    Date=date_debut
    while Date<date_fin:
        DQ=ephem.next_last_quarter_moon(Date)#calcul de la prochaine date de la phase
        Date=ephem.localtime(DQ)#conversion en temps local
        if Date<date_fin:
            Y=float(Date.strftime('%d'))#numéro du jour
            ax=axs[N-1]
            ax.text(0, -Y, u'\u25D0', fontproperties=f0, rotation=180, ha='center', va='center')#symbole quartier de Lune
            ax.text(0.1, -Y, Date.strftime('%d %b'), va='center')

#Paramètres du graphique :
plt.rcParams["font.family"] = "Ubuntu"#ou autre police installée
plt.rcParams["font.size"] = 10#à adapter aux dimensions des axes

fig, axs=plt.subplots(nrows=2, ncols=6)#création d'une figure et de 12 axes (1 par mois)
#Les graphes forment une grille de 2 lignes et 6 colonnes
#on peut modifier le nombre de grilles et colonnes, pourvu que le produit fasse 12.
axs=axs.flatten()#pour accéder à chaque graphe par axs[N]
fig.set_size_inches(7, 6)#dimensions de la figure, en pouces
"""
En modifiant les dimensions de la figure, il faudra peut-être ajuster :
- la taille de la police
- les limites des axes en x et en y
Et réciproquement.
"""
plt.suptitle("Éphémérides de la lune en %i"%(annee), fontsize=16, color='royalblue', fontweight='bold')

for N in range(1, 12+1):#N : numéro du mois courant, de 1 à 12
    ax=axs[N-1]
    date_debut=datetime.datetime(annee, N, 1)
    ax.set_title(date_debut.strftime("%B"), fontsize=13)#nom complet du mois
    ax.set_xticks([])#suppression des graduations
    ax.set_yticks([])#suppression des graduations
    ax.set_ylim(-32, 0.5)#hauteur suffisante pour les listes de dates
    ax.set_xlim(-0.1, 0.5)#largeur suffisante pour le texte
    if N==12:
        date_fin=datetime.datetime(annee+1, 1, 1)
    else:
        date_fin=datetime.datetime(annee, N+1, 1)
    NouvelleLune(date_debut, date_fin)
    PremierQuartier(date_debut, date_fin)
    PleinLune(date_debut, date_fin)
    DernierQuartier(date_debut, date_fin)

plt.tight_layout()
NomFichier="ephemeridesLune"+str(annee)
#Le nom de fichier se terminera par l'année
fig.savefig(NomFichier+".png", dpi=200)#création d'un fichier image PNG
fig.savefig(NomFichier+".pdf")#création d'un fichier PDF
plt.show()