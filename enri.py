import re,sys 
d= open('subst.dic','a',encoding='utf-16-le')
d.write('\ufeff')
res= open('subst_enri.dic','w',encoding='utf-16-le')
res.write('\ufffe')
var=open(sys.argv[1],'r',encoding="utf-8").readlines() 
for i in var:
	x=re.findall("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml)",i,re.I)
	for j in x:
		d.write(j[0].lower()+",.N+subst\n")

d.close()
a=open('subst.dic','r',encoding='utf-16-le').readlines()
for j in a:
	res.write(j)
res.close()

mf = open('subst.dic', 'r',encoding='utf-16-le').readlines()
mf_set=set(mf)
out  = open('temp.dic', 'w',encoding='utf-16-le')
out.write('\ufeff')
for ligne in mf_set:
    out.write(ligne)
out.close()

l=list()
fichL='temp.dic'
with open(fichL,encoding='utf-16-le')as fin:
	for line in fin:
		l.append(line.strip())
l.sort()
#print(l)
cpt=0
fichE='subst.dic'
with open(fichE,'w',encoding='utf-16-le')as fout:
	for i in l:
		fout.write(i+'\n')
		cpt+=1
		print(str(cpt)+"-"+i+"\n")
