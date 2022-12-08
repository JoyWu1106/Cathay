n=int(input('輸入數字： ')) #輸入數字
a=list(range(1,n+1)) #建立一個列表，存放的是號碼數
count=0;#構造一個全局變數，使得其儲存每一位報的數
while len(a)>1:#循環直到列表只剩下一個元素
    b=a[:]#複製列表，為下一步刪除做準備
    for i in range(0,len(b)):#在len(b)的次數中，計數，並去除數
        count+=1
        if count%3==0:#如果報三，則去除a中的這一位
            a.remove(b[i])
print(a[0])# Cathay
