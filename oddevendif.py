class Number:
    def findOddEvenDifference(self,numlist):
        oddcount=0
        evencount=0
        for number in numlist:
            
            if(number%2)==0:
                evencount+=number
            else:
                oddcount+=number
            diff=oddcount-evencount
        print(diff)
if '__main__':
    numlist=[]
    n=int(input())
    for i in range(n):
        num=int(input())
        numlist.append(num)
    o=Number()
    o.findOddEvenDifference(numlist)
