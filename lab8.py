from abc import ABC

class Abstract(ABC):
 def _init_(self,addr):
    self.address=addr
 def calculateFreqs(self):
  pass

class ListCount(Abstract):
 def _init_(self,addr):
  super()._init_(addr)

 def calculateFreqs(self):
  file=open(self.address,"r")
  content = []
  for line in file:
   for word in line.split():
    content.append(word)
  content2=[]
  content3=[]
  for word in content:
   if word in content2:
    continue
   else:
    content3.append(str(word)+" = "+str(content.count(word)))
    content2.append(word)
  print(content3)

class DictCount(Abstract):
 def _init_(self,addr):
  super()._init_(addr)

 def calculateFreqs(self):
  file = open(self.address, "r")
  content={}
  for line in file:
   for word in line.split():
    content[word] = content.get(word,0)+1
  print(content)

y=ListCount("strange.txt")
y.calculateFreqs()


x=DictCount("strange.txt")
x.calculateFreqs()