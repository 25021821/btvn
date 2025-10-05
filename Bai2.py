a = int(input("Nhập chiều rộng a: "))
b = int(input("Nhập chiều dài b: "))
print ("Diện tích của khu đất:", a*b)
print ("Diện tích của hình tròn:",(a/2)**2*3.14 )
c = (a/2)**2*3.14
print ("Diện tích trồng cây là:", round( a*b-c, 2))