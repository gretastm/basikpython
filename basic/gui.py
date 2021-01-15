from tkinter import *
import requests
root=Tk()
root.geometry("500x600")
root.title("Request sender")

def g():
    res = requests.request("GET", "https://httpbin.org/get")
    print(res.content)

def p():
    res2 = requests.request("POST", "https://httpbin.org/post")
    print(res2.content)
def d():
    res3 = requests.request("DELETE", "https://httpbin.org/delete")
    print(res3.content)

lebel_0=Label(root,text="Request sender",relief="solid",width=20,font=("arial",19,"bold"))
lebel_0.place(x=90,y=150)
lebel_1=Label(root,text="URL:httpbin.org",relief="solid",width=20,font=("arial",15,"bold"))
lebel_1.place(x=100,y=200)

b1=Button(root,text="GET",width=20,bg="brown",fg="white",command=g)
b1.place(x=150,y=350)
b2=Button(root,text="POST",width=20,bg="brown",fg="white",command=p)
b2.place(x=160,y=400)
b3=Button(root,text="DELETE",width=20,bg="brown",fg="white",command=d)
b3.place(x=170,y=450)
root.mainloop()