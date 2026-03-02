# Initiation à la sécurité informatique

## Introduction
Durant la suite des exercices, nous allons travailler avec le système d’exploitation Linux. Vous pouvez utiliser votre système linux ou WSL sous windows 10/11 ou encore celui d'un Raspberry Pi.

Nous aborderons quelques éléments et outils de la sécurité : intégrité de données, attaque par force brute, cryptage et stéganographie.

## Empreintes md5 / SHA-1
En cryptographie, [MD5](https://en.wikipedia.org/wiki/MD5) (Message Digest algorithm 5 défini par Ronald Rivest en 1991 au MIT) et [SHA-1](https://en.wikipedia.org/wiki/SHA-1) (Secure Hash Algorithm 1 défini par la NSA en 1993) sont des [fonctions de hachage](https://zestedesavoir.com/tutoriels/1895/les-fonctions-de-hachage-cryptographiques) utilisées pour vérifier l’intégrité des fichiers (aujourd'hui, ces algorithmes sont considérés **comme obsolètes** et il est fortement recommandé d'utiliser *SHA-2* ou *SHA-3* quand c'est possible)

Devenu un standard internet, [MD5](http://www.ietf.org/rfc/rfc1321.txt) est employé dans beaucoup d’applications de sécurité et permet rapidement de s’assurer de l’intégrité de fichiers (utile lors de téléchargement). Il est à noter que ces algorithmes 

Ainsi, en comparant  l’empreinte  md5  du  fichier  que  vous  venez  de  récupérer  à  l’empreinte  que  le  site  de téléchargement vous donne, vous pouvez vous assurer que vous possédez le même fichier que l’original.

**Nota**

*md5sum* est un outil de calcul d’empreinte déjà présent sur les systèmes linux.

Installez ensuite 7zip sur votre machine en tapant 
```bash
sudo apt-get install p7zip
```

### Exercice
* Téléchargez les fichiers images [canal.jpg](https://github.com/truillet/UToulouse/blob/master/m2issd/ressources/canal.jpg) et [pigeonnier.jpg](https://github.com/truillet/UToulouse/blob/master/m2issd/ressources/pigeonnier.jpg) à l’adresse
* Comparez les fichiers reçus avec les empreintes MD5 données sur le même site (fichier [md5sum.txt](https://github.com/truillet/UToulouse/blob/master/m2issd/ressources/md5sum.txt))
* Qu’en concluez-vous ?
* Que feriez-vous ?

## Cacher l’information au vu de tous : stéganographie
La stéganographie est *l’art de la dissimulation*. Cela consiste à cacher un message/fichier dans un objet anodin.
Il y a de nombreux exemples d’usage de cette technique depuis l’antiquité (tatouage sur le crâne, encre invisible, micropoint, ...)

L’informatique permet d’affiner cette technique en ajoutant soit des fichiers d’apparence anodine un autre fichier (utilisation par exemple de la technique LSB – Least Significant Bit)

* **Lien** : [Stéganographie](https://www.securiteinfo.com/attaques/divers/steganographie.shtml)

### Exercice
* Commençons par installer steghide en tapant :
```bash
sudo apt-get install steghide
``` 
* Téléchargez le fichier image [canal_midi.jpg](https://github.com/truillet/UToulouse/blob/master/m2issd/ressources/canal_midi.jpg)
* Vous avez appris par ailleurs que la passphrase utilisée est *canal*.
* Vérifiez que la photo contient bien du contenu caché en utilisant 
```bash
steghide info canal_midi.jpg
```
* Extrayez ensuite le contenu en tapant : 
```bash
steghide extract -sf canal_midi.jpg
```

### attaque de mots de passe par force brute
Nous  allons  maintenant  essayer  de  cracker  un  mot  de  passe  par  force  brute  (essai  de  toutes  les  combinaisons possibles). Il existe de nombreux logiciels permettant de tester toutes les combinaisons, alliant usage de la puissance
du processeur comme celle de la carte graphique (GPU).

* Téléchargez le fichier [perdu.zip](https://drive.google.com/open?id=1kvN-gujuvr9Yod5VYtphypExk05PxXTw)
* Par *chance*, vous avez appris par ailleurs que le mot de passe est au maximum composé de **4 éléments** et seulement composé de caractères en *minuscules* ... Trouvez-le !
* Enfin, vérifiez le contenu !
* Estimer le nombre d’essais à effectuer maximum pour cracker le mot de passe. Estimer ce nombre d’essais si on utilise des majuscules. Qu’en concluez-vous ?
* Pour essayer de décrypter le mot de passe, installons le logiciel fcrackzip (outil de décryptage) : 
```bash
sudo apt-get install fcrackzip
```
* Décodons ensuite le fichier en utilisant : 
```bash
fcrackzip -u -c a -p aaaa fichier.zip
```
*Options*
- -u permet d’essayer le mot de passe trouvé avec unzip
- -c a indique que vous allez utiliser tous les caractères en minuscules pour essayer de décrypter le mot de passe
- -p aaaa indique que vous voulez décoder jusqu’à 4 caractères

*Nota*
Si  vous  désirez  protéger  votre  fichier  zip,  utilisez  la  commande :  
```bash
zip  -e  fichier.zip fichiers_à_zipper
```
Vous devrez certainement installer zip en utilisant : 
```bash
sudo apt-get install zip
```

###  GPG
GnuPG  (GNU  Privacy  Guard)  est  l’implémentation  GNU  (GNU’s  Not  Unix)  du  standard  OpenPGP  (format  de cryptographie à clés publique/privée normalisé par la RFC 4880) et disponible dans les distributions Linux. GPG permet de signer et de chiffrer tout document numérique.

Nous allons commencer par générer la paire de clés publiques/privées en utilisant la commande
```bash
gpg --gen-key
```
* Choisir successivement les valeurs suivantes : 1 (RSA et RSA) / 2048 (taille de la clé) / 0 (pas d’expiration de la clé) / o (Oui) / (votre nom) / (votre adresse) / (éventuel commentaire) / (votre phrase secrète) / (encore votre phrase secrète) / (faire des choses pour générer de l’entropie) puis attendre ...
* Vérifiez ensuite que les clés ont bien été créées avec la commande gpg --list-keys
La commande *gpg --fingerprint* va nous permettre de trouver l’empreinte (fingerprint) de la clé publique.

* Il va falloir maintenant stocker sur un serveur notre clé publique avec de pouvoir recevoir par exemple de méls chiffrés.

Créons d’abord un certificat de révocation (au cas où) avec la commande 
```bash
gpg --gen-revoke (votre adresse mél) > revoc_(votre adresse mél).txt
```
Répondez aux questions posées.

* Ensuite, envoyez votre clé publique sur le serveur (par exemple https://pgp.mit.edu) en utilisant :
```bash
gpg --keyserver hkp://pgp.mit.edu --send-keys (la clé publique)
```

Nous  allons  maintenant  chiffrer  notre  premier  fichier.  Ouvrez  un  document par  exemple  en  utilisant :
```bash
nano mondoc.txt 
```

Ecrivez du texte puis sauver.
Pour chiffrer, rien de plus simple, utilisez la commande : 
```bash
gpg -er (votre adresse mél) mondoc.txt
```
(-e signifie que vous allez chiffrer – *encrypt* – et -r que vous allez utiliser la clé publique spécifiée après).

Normalement, vous devriez avoir un fichier de type mondoc.txt.gpg qui est apparu :)
Pour déchiffrer un texte, il faut avoir la clé secrète ce qui tombe bien puisque vous la possédez ! Pour déchiffrer, rien de plus simple, il suffit de taper 
```bash
gpg mondoc.txt.gpg
```
*  Chiffrez un texte et envoyez-le à quelqu’un.
*  Que faire pour que cela fonctionne et que la personne puisse le déchiffrer ?

## codage RSA (Rivest, Shamir, Adleman, 1977)
**[RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA)** (du nom de ses inventeurs et un codage de cryptographie dit *asymétrique* (à clé publique et clé privée). RSA permet d’assurer la confidentialité (seul le propriétaire de la clé privée peut déchiffrer le message reçu) et la non-altération et non-répudiation. Seul le propriétaire de la clé privée peut signer un message. Une signature déchiffrée avec la clé publique permet de prouver l’authenticité du message. L’algorithme étant public, sa difficulté réside dans la difficulté à factoriser un grand nombre.

Une  clé  RSA  de  2048  bits  a  pu  être  craquée  en  2016.  L’ANSSI  préconise  l’emploi  de  clés  [RSA  de  3072  bits]
(https://cyber.gouv.fr/sites/default/files/2021/03/anssi-guide-selection_crypto-1.0.pdf).

### Fonctionnement
Bob possède un message confidentiel qu'il souhaite transmettre à Alice. Alice construit deux clés :
* une clé de chiffrement publique qu'elle transmet à Bob.
* une clé de déchiffrement privée qu'elle conserve soigneusement.

Bob utilise la clé publique pour chiffrer le message, et le transmets à Alice. Alice utilise la clé privée pour déchiffrer le message reçu.

**Génération des clés**

Soient deux grands nombres premiers *aléatoirement* choisis : p et q. Notons n = p.q et phi(n) = (p-1).(q-1)

Soient d un grand entier *aléatoirement* choisi premier avec phi(n) et e l'inverse de d modulo phi(n). (soit e.d
= 1 mod phi(n))

La clé publique de chiffrement est le couple (n,e), la clé privée de déchiffrement le couple (n,d).

**Exercice**

René utilise RSA et publie sa clé publique (n=187, e=3)

* Encoder le message (ASCII) suivant : BOB avec la clé publique de René (B possède le code ASCII 66)

**Rappel**
chiffrement du caractère (x) --> C=(x)e mod n

En utilisant le fait que l’indicatrice d’Euler phi(n)=(p-1).(q-1) est égal à 160 dans notre cas, retrouvez les facteurs premiers **p** et **q** (permettant le calcul de la clé secrète de René)
* Qu’en concluez-vous sur l’algorithme en général ?

**Liens**
*  https://www.securiteinfo.com/cryptographie/cracked.shtml
*  https://www.nextinpact.com/news/99301-une-intelligence-artificielle-a-casse-chiffrement-rsa-sur-2048-bits.htm

### exercice général
En sachant que pour encoder un fichier, il faut utiliser la commande
```bash
steghide embed -cf fichier.jpg -ef fichier_à_cacher
```
* Créez un fichier zip contenant n’importe quoi protégé par un mot de passe de 5 lettres.
*  Créez un deuxième fichier zip protégé par un autre mot de passe (à vous de décider lequel avec la taille de votre choix) contenant votre clé publique.
*  Cachez votre fichier zip dans une image jpeg en utilisant le premier mot de passe
*  Partagez deux images jpeg dont l’une contenant le message caché et le premier fichier zip
*  Récupérez le travail d’un de vos collègues et essayez de retrouver la clé publique partagée !
* Codez un message secret avec la clé publique trouvée et la transmettre à votre collègue
* Récupérez le message codé et le décoder ...

### Aller plus loin
* distribution  Kali : Linux  2025.4, *[The  most  advanced  penetration testing  distribution](https://www.kali.org/get-kali/#kali-installer-images)*
