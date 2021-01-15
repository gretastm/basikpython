import requests
res=requests.request("GET","https://httpbin.org/get")
print(res.status_code)
print(res.content)

res2=requests.request("GET","https://httpbin.org/headers")
print(res2.status_code)
print(res.content)

res3=requests.request("GET","https://httpbin.org/ip")
print(res3.status_code)
print(res3.content)

res4=requests.request("GET","https://httpbin.org/cache")
print(res4.status_code)
print(res4.content)

res5=requests.request("GET","https://httpbin.org/brotli")
print(res5.status_code)
print(res5.content)

res6=requests.request("POST","https://httpbin.org/response-headers")
print(res6.status_code)
print(res6.content)

res7=requests.request("POST","https://httpbin.org/anything")
print(res7.status_code)
print(res7.content)

res8=requests.request("POST","https://httpbin.org/post")
print(res8.status_code)
print(res8.content)

res9=requests.request("PUT","https://httpbin.org/put")
print(res9.status_code)
print(res9.content)

res10=requests.request("PUT","https://httpbin.org/anything")
print(res10.status_code)
print(res10.content)

res11=requests.request("DELETE","https://httpbin.org/delete")
print(res11.status_code)
print(res11.content)

res12=requests.request("PUT","https://httpbin.org/status")
print(res12.status_code)
print(res12.content)

res13=requests.request("POST","https://httpbin.org/status")
print(res13.status_code)
print(res13.content)