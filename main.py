F=print
C='temp'
import requests as B,string as G,os,time
os.system('clear')
H=input('fluxus key link: ')
D={'referer':'https://linkvertise.com','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36'}
try:I=B.get(H)
except:F('Error requesting to the server, Are you sure you put the correct link?');time.sleep(5);exit(1)
J=B.get('https://fluxteam.net/android/checkpoint/check1.php',headers=D)
with open(C,'a')as A:E=B.get('https://fluxteam.net/android/checkpoint/main.php',headers=D);A.write(E.text);A.close()
A=open(C)
F(E.readlines()[184].replace('</code>','').translate({ord(A):None for A in G.whitespace}))
A.close()
os.remove(C)
