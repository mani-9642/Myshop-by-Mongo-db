print("\t\t\tWELCOME TO MY SHOP\n\t\t\t------------------")
print("1) Search\n2) Buy")
class Search:
    def Frist(self):
        ch = int(input("Enter your Choice : "))
        from pymongo import MongoClient
        mc = MongoClient("localhost:27017")
        db = mc.project
        if ch==1:
            print("1) Search by product Id : \n2) Search by Name : ")
            self.n=int(input("Enter your Choice : "))
            if self.n == 1:
                k = int(input("Enter your Product Id : "))
                s = db.product.find({"_id": k})
                for x in s:
                    for g, h in x.items():
                        if g == "pname":
                            print("Product Name : ", h)
                        if g == "cost":
                            print("Product Cost : ", h)
                            self.v = h
            elif self.n == 2:
                l = input("Enter the Product Name : ")
                z = db.product.find({"pname": l.capitalize()})
                for y in z:
                    for g, h in y.items():
                        if g == "cost":
                            print("Product Cost : ", h)
                            self.v = h
            else:
                print("Invalid input Please check again")
            Search.amt(self)

        elif ch==2:
            pid=int(input("Enter the Product Id : "))
            fin=db.product.find({"_id":pid})
            for f in fin:
                for q,w in f.items():
                    if q=="pname":
                        print('Product Name : ',w)
                    if q=="cost":
                        print("Product Cost : ",w)
                        self.v=w
            Search.amout(self)
        else:
            print("Invalid input Please check again")
        mc.close()
    def amt(self):
        b = input("Do you want to buy (Y/N) : ")
        if b == "y" or "Y":
            Search.amout(self)
    def amout(self):
        q = int(input("Enter the Quantity : "))
        tot = self.v * q
        print("Bill Amount : ", tot)
class total(Search):
    def add(self):
        Search.Frist(self)
z=total()
z.add()






