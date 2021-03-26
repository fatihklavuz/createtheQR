import qrcode


with open('F:/Project/python/ip.txt','r') as liste:
 for a in liste: 
     a=a.replace("\n", "")
     qresim=qrcode.make(a)

     qresim.save('F:/Project/python/'+a+'.png')
