class Traveler:
    def __init__(self,travelername,countries,age,countryf):
        self.travelername=travelername
        self.countries=countries
        self.age=age
        self.countryf=countryf
class TravelAgency:
    def __init__(self,tlist):
        self.tlist=tlist
    def countTraveledcountries(self,country):
        c=0
        for traveler in self.tlist:
            for j in traveler.countries:
                if j==country:
                    c+=1
        print(c)
    def maxcountry(self,tlist):
        maxi=0
        cname=''
        for traveler in self.tlist:
            if(len(traveler.countries)>maxi):
                maxi=len(traveler.countries)
                cname=traveler.travelername
        print(cname)
n=int(input())
tlist=[]
for i in range(n):
    travelername=input()
    countries=[]
    N=int(input())
    for i in range(N):
        c=input()
        countries.append(c)
    age=int(input())
    countryf=input()
    t=Traveler(travelername,countries,age,countryf)
    tlist.append(t)
t=TravelAgency(tlist)
country=input()
t.countTraveledcountries(country)
t.maxcountry(tlist)
    
