ten = input("Nhập tên chủ hộ: ")
cs_truoc = int(input("Nhập chỉ số tháng trước: "))
cs_sau = int(input("Nhập chỉ số tháng này: "))
so_dien = cs_sau - cs_truoc
tien = 0
if so_dien <= 50:
    tien = so_dien * 1984
elif so_dien <= 100:
    tien = 50 * 1984 + (so_dien - 50) * 2050
elif so_dien <= 200:
    tien = 50 * 1984 + 50 * 2050 + (so_dien - 100) * 2380
elif so_dien <= 300:
    tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + (so_dien - 200) * 2998
elif so_dien <= 400:
    tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (so_dien - 300) * 3350
else:
    tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (so_dien - 400) * 3460
tien_tra = round(tien * 1.08)
print("Ho va ten:", ten)
print("Tien phai tra la:", tien_tra)
