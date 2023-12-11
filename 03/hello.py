largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        fn = float(num)
    except:
        print('Invalid input')
        continue
   
    if largest is None or fn < largest:
        largest = fn
    if smallest is None or fn > smallest:
        smallest = fn
        
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)