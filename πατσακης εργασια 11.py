s=""
print "gia na grapseis esu to arxeio me tis tetrades dwse 1 "
print "gia ena aytomato arxeio me tetrades dwse 2 "
epil=raw_input("dwse epilogh  ")
while epil !="1" and epil!="2":
  print "edwses lathos epilogh janadwse"
  epil=raw_input("dwse epilogh  ")
if epil=="1":
  print "otan thes na stamathseis dwse thn lexi  telos "
  arxeio=raw_input("dwse arithmo ")
  while arxeio =="telos":
    print "den ginetai na dwseis telos xwris na exeis grapsei kamia terada"
    arxeio=raw_input("dwse arithmo ")
  while arxeio !="telos":
      fin =open("allo.txt","w")
    
      for i in range(3):  
        fin.write(arxeio+" ")
        arxeio=raw_input("dwse arithmo ")
        while arxeio =="telos":
          print"den ginetai na dwseis thn leji telos dioti den exeis symplhrwsh tetrada"
          arxeio=raw_input("dwse arithmo ")
        
      fin.write(arxeio +"\n")
      fin.close()
      fin=open("allo.txt","r")
      k=fin.read()
      s=s+k
      fin.close()
      arxeio=raw_input("dwse arithmo ")

  fin=open("file.txt","w") 
  fin.write(s) 
  fin.close()    
else:
  fin=open ("file.txt","w")
  fin.write("7 8 13 88\n6 68 7 830\n9 100 11 12\n57 29 74 65\n9 13 11 15\n879 871 1005 666\n545 548 828 120\n1 2 3 4")
  fin.close()
fin=open ("file.txt","r")
a=fin.read()
fin.close()
print "tetrades arithmon \n",a
ar=[]
ari=""
w=a+" "
for i in w:
  if i!=" " and i!="\n":
    ari=ari+i
  else:
    ar.append(ari) 
    ari="" 
wo=[]   
for i in range(6):
  num=int(input("dwse arithmo "))
  k=str(num)
  wo.append(k) 
print "oi arithmoi poy edwses einai",wo 
print" kai me aytous toys arithmoys"
n=len(ar)
pl=0
a=0
found=False
for i in range(n/4):
  for k in range(a,a+4):
    if ar[k] in wo:
      pl=pl+1
  if pl==4:
    found=True
  else:
    pl=0
    a=a+4
if found == True:
  print"yparxei diathesimh tetrada"
else:
  print"den iparxei diadesimh tetrada"      

