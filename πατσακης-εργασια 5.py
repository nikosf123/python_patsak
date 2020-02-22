print "gia na grapseis esu to arxeio dwse 1 "
print "gia ena aytomato arxeio dwse 2 "
print"-------------------------------------------"
epil=raw_input("dwse epilogh  ")
while epil !="1" and epil!="2":
  print "edwses lathos epilogh janadwse"
  print"-------------------------------------------"
  epil=raw_input("dwse epilogh  ")
if epil=="1":
  arxeio=raw_input("dwse ena keimeno ")
  fin =open("text.txt","w")
  fin.write(arxeio)
  fin.close()
  fin=open("text.txt","r")
  w=fin.read()
  fin.close
  le=[]
  word=" "
  meg=[]
  gram=0
  sm=",,.,;,!,:,-,?,/,[,],(,),%,&,@,#,$,*,+"
  n=len(w)
  for i in range (n) :
    if w[i] !=" " and w[i]!="\n" and w[i] not in sm:
      word=word+w[i]
      gram=gram+1
    else:
      le.append(word)
      meg.append(gram)
      gram=0
      word=" "
  le.append(word)
  meg.append(gram)
  plithos=0
  pl=0
  nub="0123456789"
  for i in meg:
    if i>3:
      plithos=plithos+1
  for i in le:
    for k in i:
      if k in nub:
        pl=pl+1
  while plithos==0 or pl>0:
    if plithos ==0 and pl==0:
      print "to keimeno poy edwses den exei kamia leji megalyteri apo treis xaraktires janadwse"
      print"-------------------------------------------"
    if pl>0:
      print "den mporei to keimeno na periexei arithmoys"
      print"-------------------------------------------"     

    arxeio=raw_input("dwse ena keimeno ")
    fin =open("text.txt","w")
    fin.write(arxeio)
    fin.close()
    fin=open("text.txt","r")
    w=fin.read()
    fin.close
    le=[]
    word=" "
    meg=[]
    gram=0
    sm=",,.,;,!,:,-,?,/,[,],(,),%,&,@,#,$,*,+"
    n=len(w)
    for i in range (n) :
      if w[i] !=" " and w[i]!="\n" and w[i] not in sm:
        word=word+w[i]
        gram=gram+1
      else:
        le.append(word)
        meg.append(gram)
        gram=0
        word=" "
    le.append(word)
    meg.append(gram)
    plithos=0
    pl=0
    nub="0123456789"
    for i in meg:
      if i>2:
        plithos=plithos+1
    for i in le:
      for k in i:
        if k in nub:
          pl=pl+1    
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
  sm="!,.,:,-"
  n=len(w)
  for i in range (n) :
    if w[i] !=" " and w[i]!="\n" and w[i] not in sm:
      word=word+w[i]
      gram=gram+1
    else:
      le.append(word)
      meg.append(gram)
      gram=0
      word=" "
  le.append(word)
  meg.append(gram)
print"-------------------------------------------"  
print "to keimeno poy edwses"  
print w  
new=[]
found="False"
n2=len(le)
prwt=" "
lexi=" "
print"-------------------------------------------"
print "lejis me treia grammata kai panw vazontas to ptwto sto telos kai th katalhjh ay"
for i in range (n2):
  if meg[i]>3:
    w2=le[i]
    print (w2[2:]+w2[1]+"ay")





