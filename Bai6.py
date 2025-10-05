import math
print (" Nhập độ dài ba cạnh a,b,c:")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a+b>c and a+c>b and b+c>a:
	s = (a + b + c) / 2.0
	area_sq = s * (s - a) * (s - b) * (s - c)
	area = math.sqrt(area_sq)
	print("Diện tích hình tam giác là:",  f"{area:.1f}")
else:
	print("Đây không phải hình tam giác")