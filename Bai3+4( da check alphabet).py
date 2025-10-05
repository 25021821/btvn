ch = input("Nhập một ký tự thường hoặc hoa (a-z): ")
ch_hoa = ch.upper()
ch_thuong = ch.lower()
if len(ch) == 1 and ch.isalpha():
	if ch == ch.lower():
		print("Ký tự hoa:", ch_hoa)
	elif ch == ch.lower():
		print("Ký tự thường:", ch_thuong)
else:
	print("Bạn đã nhập sai ký tự")
	pr