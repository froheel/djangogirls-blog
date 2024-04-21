def test_hello(name):
    # print hello based on the name
    if name == "Feza":
        print("Hello Feza")
    elif name == "John":
        print("Hello John")
    elif name == "Tea":
        print("Hello Tea")
    else:
        print("Hello World")
    
    
names = ["Feza", "Tea", "Jane"]
for name in names:
    test_hello(name)

for i in range(1, 5):
    print(i)