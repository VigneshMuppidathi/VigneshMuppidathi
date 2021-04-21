class Product:
    def __init__(self,productname,producttype,unitprice,qtyonhand):
        self.productname=productname
        self.producttype=producttype
        self.unitprice=unitprice
        self.qtyonhand=qtyonhand
class Store:
    def __init__(self,plist):
        self.plist=plist
    def purchaseproduct(self,name,qty):
        for product in self.plist:
            if (product.productname==name and product.qtyonhand>=qty):
                product.qtyonhand=product.qtyonhand-qty
                bill=product.unitprice*qty
                return bill
        return 0
n=int(input())
plist=[]
for i in range(n):
    productname=input()
    producttype=input()
    unitprice=int(input())
    qtyonhand=int(input())
    p=Product(productname,producttype,unitprice,qtyonhand)
    plist.append(p)
name=input()
qty=int(input())
s=Store(plist)
res=s.purchaseproduct(name,qty)
if res==0:
    print("Product Not Available")
    for i in s.plist:
        print(i.productname,i.qtyonhand)
else:
    print("Product Available")
    for i in s.plist:
        print(i.productname,i.qtyonhand)
