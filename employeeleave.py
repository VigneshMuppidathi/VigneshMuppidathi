class Employee:
    def __init__(self,empname,designation,salary,leavebalance):
        self.empname=empname
        self.designation=designation
        self.salary=salary
        self.leavebalance=leavebalance
class Organisation:
    def __init__(self,elist):
        self.elist=elist
    def leaves(self,name):
        for emp in self.elist:
            if emp.empname==name:
                for a,b in emp.leavebalance.items():
                    print(a,":",b)
    def checkLeaveEligibility(self,ename,leavetype,noofdays):
        for emp in self.elist:
            
            if emp.empname==ename:
                for a,b in emp.leavebalance.items():
                    if a==leavetype:
                        if b>noofdays:
                            emp.leavebalance[a]=b-noofdays
                            print("Leave Granted")
                            self.leaves(name)
                        else:
                            print("Leave not granted")
                            self.leaves(name)
            else:
                print("Leave not granted")
                print("Employee not found")
n=int(input())
elist=[]
for i in range(n):
    empname=input()
    designation=input()
    salary=int(input())
    leavebalance={}
    N=int(input())
    for i in range(N):
        k=input()
        v=int(input())
        leavebalance[k]=v
    e=Employee(empname,designation,salary,leavebalance)
    elist.append(e)
o=Organisation(elist)
ename=input()
leavetype=input()
noofdays=int(input())
o.checkLeaveEligibility(ename,leavetype,noofdays)
    
    
