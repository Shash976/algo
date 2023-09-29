while True:
    try:
        op_str = input("Enter operation in a {operator} b format: ").split(" ")
        objects = []
        operator = ''
        for i in op_str:
            try:
                objects.append(int(i))
            except:
                operator = i
        a, b = objects
        ans = 0
        if operator == "+":
            ans = a+b
        elif operator == "-":
            ans = a-b
        elif operator in ["/", "÷"]:
            ans = a/b
        elif operator in ["*", "×"]:
            ans=a*b
        print("Answer is ", ans)
    except:
        break