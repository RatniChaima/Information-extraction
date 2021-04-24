import sys,re
res=open('subst.dic','w',encoding="utf-16-le")
res.write('\ufffe')
info=open('infos.txt','w')

if sys.version_info[0] == 3:
	from urllib.request import urlopen
else:
	from urllib import urlopen
liste=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nbT=nb=0

for x in liste:
	var=urlopen("https://www.vidal.fr/Sommaires/Substances-"+x+".htm")
	s=var.read().decode('utf-8')
	line=re.findall("<.+/\w+-[0-9]+.+>(.+)</\w>",s)

	for i in line:
		print(i)
		res.write(i+",.N+subst\n")
		nbT+=i.count(i)
		nb+=1
	info.write("Le nombre d’entités médicales qui commence par "+x+" est : "+str(nb)+"\n")
	nb=0

info.write("Le nombre total d’entités médicales par substance active du dictionnaire: "+str(nbT))
res.close()
print("l'aspiration de votre intervale est : ")
borneinf=sys.argv[1].split("-")[0]
bornesup=sys.argv[1].split("-")[1]

#print("entrer un intervale de format: lettre-lettre ") 
#v=sys.stdin.readline()
#borneinf=v[0]
#bornesup=v[2] tt ca si l'utilisateur veut saisir l'inervalle avec l'entree standard 
for y in liste:
	if (y>=borneinf and y<=bornesup):
		url=urlopen("https://www.vidal.fr/Sommaires/Substances-"+y+".htm")
		s=url.read().decode('utf-8')
		line=re.findall("<.+/\w+-[0-9]+.+>(.+)</\w>",s)
		for i in line:
			print(i)

import sys,re
res=open('subst.dic','w',encoding="utf-16-le")
info=open('infos.txt','w')

if sys.version_info[0] == 3:
	from urllib.request import urlopen
else:
	from urllib import urlopen
liste=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nbT=nb=0

for x in liste:
	var=urlopen("https://www.vidal.fr/Sommaires/Substances-"+x+".htm")
	s=var.read().decode('utf-8')
	line=re.findall("<.+/\w+-[0-9]+.+>(.+)</\w>",s,re.I)

	for i in line:
		
		convert=i.replace('\xc3\xc9','é') #pour afficher les "é" car au debut il les affiche pas , probleme d'encodage
		#print(i)
		res.write(i+",.N+subst\n")
		nbT+=i.count(i)
		nb+=1
	info.write("Le nombre d’entités médicales qui commence par "+x+" est : "+str(nb)+"\n")
	nb=0

info.write("Le nombre total d’entités médicales par substance active du dictionnaire: "+str(nbT))
res.close()
print("l'aspiration de votre intervale est : ")
borneinf=sys.argv[1].split("-")[0]
bornesup=sys.argv[1].split("-")[1]

#print("entrer un intervale de format: lettre-lettre ") 
#v=sys.stdin.readline()
#borneinf=v[0]
#bornesup=v[2] tt ca si l'utilisateur veut saisir l'inervalle avec l'entree standard stdin
for y in liste:
	if (y>=borneinf and y<=bornesup):
		url=urlopen("https://www.vidal.fr/Sommaires/Substances-"+y+".htm")
		s=url.read().decode('utf-8')
		line=re.findall("<.+/\w+-[0-9]+.+>(.+)</\w>",s)
		for i in line:
			print(i)

