import requests
res=requests.request("PATCH","https://httpbin.org/patch")
print(res.status_code)
print(res.content)

res2=requests.request("PATCH","https://httpbin.org/anything")
print(res2.status_code)
print(res2.content)

res3=requests.request("GET","https://httpbin.org/drip")
print(res3.status_code)
print(res3.content)

res4=requests.request("GET","https://httpbin.org/uuid")
print(res4.status_code)
print(res4.content)

res5=requests.request("GET","https://httpbin.org/user-agent")
print(res5.status_code)
print(res5.content)