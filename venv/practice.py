input = "12\n5"
a,b = map(int.input().split())
if a*b > 0:
    if a>0:
        print("1")
    if a<0:
        print("3")
else:
    if a>0:
        print("4")
    if a<0:
        print("2")