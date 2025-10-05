c = input("Nhập chữ cái hoa: ")
while True:
	if len(c) == 1 and c.isalpha():
		if c == c.lower():
			print("Sai kí tự")
			break 
		if c == 'A':
		    print("Không có chữ cái trước a")
		    break
		else:
		    lower_c = c.lower()
		    prev_char = chr(ord(lower_c) - 1)
		    print("Kết quả:", prev_char)
		    break