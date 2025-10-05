x = float(input("Nhập giá (USD): "))
phi_vanchuyen = 10  
gia_truoc_thue = x + phi_vanchuyen
thue = gia_truoc_thue * (0.30 + 0.10)
tong_tien = gia_truoc_thue + thue
print(f"Tổng số tiền phải trả: {tong_tien:.2f} USD")
