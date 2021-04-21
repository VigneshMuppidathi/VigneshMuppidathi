class Player:
    def __init__(self,playername,countries,age,countryf):
        self.playername=playername
        self.countries=countries
        self.age=age
        self.countryf=countryf
def countPlayers(plist,icountry):
    c=0
    for player in plist:
        if(player.countryf==icountry):
            c+=1
    print(c)
def maxcountry(plist):
    maxi=0
    c_name=''
    for player in plist:
        if(len(player.countries)>maxi):
           maxi=len(player.countries)
           c_name=player.playername
    print(c_name)
n=int(input())
plist=[]
for i in range(n):
    playername=input()
    countries=[]
    N=int(input())
    for i in range(N):
        c=input()
        countries.append(c)
    age=int(input())
    countryf=input()
    p=Player(playername,countries,age,countryf)
    plist.append(p)
icountry=input()
countPlayers(plist,icountry)
maxcountry(plist)
    
