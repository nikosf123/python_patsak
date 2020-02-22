print "gia na grapseis esu to arxeio dwse 1 "
print "gia ena aytomato arxeio dwse 2 "
print"-------------------------------------------"
epil=raw_input("dwse epilogh  ")
while epil !="1" and epil!="2":
  print "edwses lathos epilogh janadwse"
  epil=raw_input("dwse epilogh  ")
if epil=="1":
  arxeio=raw_input("dwse ena keimeno ")
  fin =open("text.txt","w")
  fin.write(arxeio)
  fin.close()
else:
  fin = open('text.txt', 'w')
  fin.write("simera einai deutera \n")
  fin.write("exoume mathima \n")
  fin.write("alla variemai na paw")
  fin.close() 
fin=open("text.txt","r")
w=fin.read()
fin.close
le=[]
word=" "
meg=[]
gram=0
sm="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=len(w)
for i in range (n) :
  if w[i] !=" " and w[i]!="\n" and w[i] in sm:
    word=word+w[i]
    gram=gram+1
  else:
    le.append(word)
    meg.append(gram)
    gram=0
    word=" "
le.append(word)
meg.append(gram)
print "to keimeno poy edwses"  
print w
print"-------------------------------------------"
new=[]
found="False"
n2=len(le)
prwt=" "
lexi=" "
print "lejis me treia grammata kai panw vazontas to ptwto sto telos kai th katalhjh ay"
for i in range (n2):
  if meg[i]>3:
    w2=le[i]
    print (w2[2:]+w2[1]+"ay")
