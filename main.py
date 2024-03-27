class employee:
    def __init__(self):
        self.items=[]
    def insert(self):
        n=int(input("enter the number of records"))
        for i in range(n):
            ename=input("employee name:")
            eid=int(input("employee id:"))
            salary=float(input("employee salary:"))
            self.items.append([ename,eid,salary])
    def delete(self):
        eid=int(input("enter employee id to delete"))
        for row in self.items:
            for i in row:
                if i==eid:
                    self.items.remove(row)
    def display(self):
        for i in self.items:
            print(i)
e=employee()
e.insert()
e.display()
e.delete()
e.display()

