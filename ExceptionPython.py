ItemsInCart = 0

if ItemsInCart != 2:
    pass
    # raise Exception("Product not available")

assert (ItemsInCart == 0)

#   try , catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("TESTING CATCH OR EXCEPT")

#   try , catch with exception message

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)


#   try , catch with exception message and finally


try:
    with open('text.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resources ..and executing finally block")
