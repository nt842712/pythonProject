print("Test")
a = 3
print(a)
test = "Testing"
print(test)

b, c, d = 3, 5, "Great"

print(b)
print("{} {} {}".format("Value is", b, c))


print(type(b))
print(type(d))
print(b, c)
print(b+c)

print(test+d)

value = [1, 2, "Rahul", 4, 5]

print(value[0])
print(value[1])
print(value[2])
print(value[3])
print(value[-1])
print(value[1:1])
value.insert(3, "Testing")
print(value[3])
print(value)
value.append("End")
print(value)
value[2] = "TESTING"
print(value)
del value[0]
print(value)

val = (1, 2, "Rahul", 4, 5)
print(val[1])

a = {"a": 2, 4: "fhf", "c": "Hello world"}

print(a["c"])



dist = {}

dist["firstName"] = "Naresh"

print(dist)
greeting="Good Morning"
if greeting == "Morning":
    print("true")
else:
    print("false")
print("Done")

#for loop

obj=[1,2,3,4,5]

for i in obj:
    print(i*2)

# sum of natural number
summation = 0
for j in range(1, 6):
    summation = summation+j
print(summation)
print("****************")

for k in range(1,10,5):
    print(k)
print("****************")
for k in range(10):
    print(k)






