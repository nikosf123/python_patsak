print "gia na grapseis esu to arxeio dwse 1 "
print "gia ena aytomato arxeio dwse 2 "
print"-------------------------------------------"
epil=raw_input("dwse epilogh  ")
while epil !="1" and epil!="2":
  print "edwses lathos epilogh janadwse"
  epil=raw_input("dwse epilogh  ")
if epil=="1":
  arxeio=raw_input("dwse ena keimeno ")
  fin =open("test.txt","w")
  fin.write(arxeio)
  fin.close()
else:
  fin =open('test.txt', 'w')
  fin.write("simera einai deutera \n")
  fin.write("exoume mathima \n")
  fin.write("alla variemai na pao")
  fin.close() 
fin=open("test.txt","r")
w=fin.read()
fin.close     
le=[]
word=""
meg=[]
gram=0
n=len(w)
sm="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range (n) :
  if w[i] !=" " and w[i] !="\n" and w[i] in sm:
    word=word+w[i]
    gram=gram+1
  else:
    le.append(word)
    meg.append(gram)
    gram=0
    word=""
le.append(word)
meg.append(gram)
print "to keimeno poy edwses"  
print w
print"-------------------------------------------"
n=len(meg)
for i in range(n-1):
  for k in range(n-1,i,-1):
    if meg[k]>meg[k-1]:
      meg[k],meg[k-1] = meg[k-1],meg[k]
      le[k],le[k-1] = le[k-1],le[k]
print "oi pente megalyteres lejeis einai"
xwris=""
fon="aeuioyAEUIOY"
for i in range (5):
  print le[i]
  w2=le[i]
  for k in w2:
    if k not in fon:
      xwris=xwris+k

  le.pop(i)
  le.insert(i,xwris)
  xwris=""
nea=""
teliko=""
print"-------------------------------------------"
print "oi pente megalyteres lejeis xwris ta foninta einai"
for i in range(5):
  print le[i]
  w3=le[i]
  n=len(w3)
  for k in range (n-1,-1,-1):
    nea=nea+w3[k]
  teliko=teliko+nea+" "
  nea=""
print"-------------------------------------------"  
print "oi pente megalyters lejeis xwris ta\n fonienta kai antestramenes einai"  
print teliko
