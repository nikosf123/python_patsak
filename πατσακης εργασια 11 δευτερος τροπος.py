fin=open ("file.txt","w")
fin.write("7 8 13 88\n6 68 7 830\n9 100 11 12\n57 29 74 65\n9 13 11 15\n879 871 1005 666\n545 548 828 120\n11 22 33 44")
fin.close()
fin=open ("file.txt","r")
a=fin.read()
fin.close()
a=a+" "
k=[]
o=[]
noum=""
ar="1234567890"
n=len(a)
for i in range(n):
    if a[i] in ar:
      noum=noum+a[i]
    if a[i:i+1]==" " or a[i:+i+1]=="\n":
      k.append(noum)
      noum=""
    if len(k)==4:
      o.append(k) 
      k=[] 
pl=0
found=False
x=[]
for i in range(6):
  r=raw_input("dwse ")
  x.append(r)
n2=len(o)
for i in o:
  for k in i:
    if k in x:
      pl=pl+1  
  if pl==4:
    found=True 
  pl=0
if found== True:
  print"yparxei diadesimh tetrada"
else:
  print"den yparxei diadesimh tetrada"         
