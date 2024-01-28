for x in '0123456789ABCDE':
    a = int('97968'+x+'15',15)
    b = int('7'+x+'233',15)
    if ((a+b)%14==0):
        print((a+b)//14)
        
## bank-ege.ru id: 23601 ## 
