def hello():
    print("Hello, User")

def pack(a,b,c):
    return[a,b,c]

def eat_lunch(list):
    if len(list) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            else:
                print(f"next I eat {list[i]}")

hello()
print(pack("a","b","c"))  
print(pack(1,2,3))  
eat_lunch([])
eat_lunch(["taco"])
eat_lunch(["tamale","quesadilla","torta","soup"])          