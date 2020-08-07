d={}
dd={}
print('歡迎進入系統~')
while True:
    print('#################')
    print('1.金額平分')
    print('2.金額不平分')
    print('3.離開系統')
    x=int(input('請輸入選項:'))
    if x==1:
        while True:
            print('#################')
            print('1.每人應付金額')
            print('2.個別金額離均差')
            print('3.列出"2"')
            print('4.離開系統')
            a=int(input('請輸入選項:'))
            if a==1:
                while True:
                     p=int(input('請輸入總金額:'))
                     q=int(input('請輸入總人數:'))
                     o=p//q
                     o=int(o)
                     print('金額是:',o)
                     break
            if a==2:
                while True:   
                    p=input('請輸入姓名(按0退出):')
                    if p=='0':
                        break
                    q=int(input('請輸入已付金額:'))
                    k=q-o 
                    k=int(k)
                    if k>0:
                        print('多付',k,'元')
                    elif k<0:
                        print('還需再付',-k,'元')
                    else:
                        print('金額剛剛好~')
                    d[p]=k
            if a==3:
                print(d)
            if a==4:
                break
    if x==2:
        while True:
            print('#################')
            print('1.計算金額')
            print('2.列出"1"')
            print('3.離開系統')
            b=int(input('請輸入選項:'))
            if b==1:
                while True: 
                    m=input('請輸入名字(按0退出):')
                    if m=='0':
                        break
                    n=int(input('請輸入應付金額:'))
                    r=int(input('請輸入已付的金額:'))
                    w=r-n
                    w=int(w)
                    if w>0:
                        print('多付',w,'元')
                    elif w<0:
                        print('還需再付',-w,'元')
                    else:
                        print('金額剛剛好~')
                    dd[m]=w
            if b==2:
                print(dd)
            if b==3:
                break
            
    if x==3:
        break

          
                    
                    
                    
                    
                    