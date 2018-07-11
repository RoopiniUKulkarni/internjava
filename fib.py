def fibonnaci(n):
    if(n<=1):
        return(n)
    else:
        return (fibonnaci(n-1))+(fibonnaci(n-2))
n=int(input("enter the no,of terms:"))
print("fibbonaci sequence:")
for i in range(n):
    print(fibonnaci(i))
        
