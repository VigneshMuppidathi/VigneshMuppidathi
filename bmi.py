class Person:
    def __init__(self,name,height,weight,bmi=0,status=''):
        self.name=name
        self.height=height
        self.weight=weight
        self.bmi=bmi
        self.bmi_status=status
    def calculateBmi(self):
        self.bmi=round(self.weight/(self.height*self.height))
class Society:
    def __init__(self,bmi_status,person_list):
        self.bmi_status=bmi_status
        self.person_list=person_list
    def calculateBmiAndStatusByname(self,name):
        flag=False
        for person in self.person_list:
            if person.name.lower()==name.lower():
                flag=True
                person.calculateBmi()
                print(person.bmi,end=' ')
                for val in self.bmi_status.keys():
                    value=self.bmi_status[val]
                    if value[0]<=person.bmi<=value[1]:
                        print(val)
                        person.bmi_status=val
        return flag
    def removeInvalidPersons(self,bmi):
        list=[]
        for person in self.person_list:
            person.calculateBmi()
            if person.bmi<bmi:
                list.append(person)
        return list
list_of_persons=[]
n=int(input())
for i in range(n):
    name=input()
    height=int(input())
    weight=int(input())
    p= Person(name,height,weight)
    list_of_persons.append(p)
bmi_status={}
N=int(input())
for i in range(N):
    bmistatus=input()
    l,u=int(input()),int(input())
    if l>u:
        l,u=u,l
    bmi_status[bmistatus]=(l,u)
s=Society(bmi_status,list_of_persons)
name=input()
bmi=int(input())
flag=s.calculateBmiAndStatusByname(name)
if not flag:
    print("No Person Exist")
res=s.removeInvalidPersons(bmi)
for x in res:
    print(x.name,x.bmi)

    
