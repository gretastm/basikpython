class Student:
    def __init__(self,name,surname,age,arr):
        self.name=name
        self.surname=surname
        self.age=age
        self.arr=arr
    def mijin(self,arr):
        a=0
        b=0
        for i in arr:
            a+=i
            b+=1
            return a/b