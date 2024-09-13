#sliceing instring
name="ali akbar khan"
# result=name[4:9]
# print(result)
print(name[10:-1])

num="0123456789"
result=num[0:9:3] #third parameter used to include multiple of that value position
print(result)
rs=name[0:7:2]
print(rs)


#Methods
print(name.split().pop())

#place holders {}
chai="vital"
quantity=2
order=f"i ordered {quantity} cup of {chai} chai"
print(order)

#conversion of list into string by using join
li=["ali","akbar","khan"]
print(" ".join(li))