msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

running = True
while running:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    valid_oper = "+-*/"
    if oper not in valid_oper:
        print(msg_2)
        continue

    result = 0
    if oper == "+":
        result = x + y
        print(result)
    elif oper == "-":
        result = x - y
        print(result)
    elif oper == "*":
        result = x * y
        print(result)
    elif oper == "/":
        if y == 0.0:
            print(msg_3)
            continue
        else:
            result = x / y
            print(result)

    running = False
