for i in range(1,4):

    for k in range(i,4):
        print(" ",end=" ")
    for j in range(i):
        if i>=1 and i<= 2:
            if j ==0 or j==i-1:
                print("* ",end=" ")
            else: 
                print("  ",end=" ")
        else:
            print("* ",end=" ")
    print()
# Cathay
