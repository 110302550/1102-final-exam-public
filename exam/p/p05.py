def p05(l1=[1,4,3,2,5,2], x=3):
    output_list=None
    # ↓程式區域↓
    l2 = []
    l3 = []

    for n in l1:
        if n < x:
            l2.append(n)
        else:
            l3.append(n)

    l2.sort()

    output_list = l2 + l3
    
    # ↑程式區域↑
    return output_list
