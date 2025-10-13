from lxml import etree


tree = etree.parse("BUOI_05_NGUYENQUANGVINH/5,2/quanlyquanan.xml")

# 1. Lấy tất cả bàn
print("1. Tất cả bàn:")
bans = tree.xpath("//BAN")
for ban in bans:
    print(ban.get('TENBAN'))

# 2. Lấy tất cả nhân viên
print("\n2. Tất cả nhân viên:")
nhanviens = tree.xpath("//NHANVIEN")
for nv in nhanviens:
    print(nv.find('TENNV').text)

# 3. Lấy tất cả tên món
print("\n3. Tất cả tên món:")
print(tree.xpath("//MON/TENMON/text()"))

# 4. Lấy tên nhân viên có mã NV02
print("\n4. Tên nhân viên có mã NV02:")
print(tree.xpath("//NHANVIEN[@MANV='NV02']/TENNV/text()"))

# 5. Lấy tên và số điện thoại của nhân viên NV03
print("\n5. Tên và SĐT nhân viên NV03:")
print(tree.xpath("//NHANVIEN[@MANV='NV03']/TENNV/text()"), tree.xpath("//NHANVIEN[@MANV='NV03']/SDT/text()"))

# 6. Lấy tên món có giá > 50000
print("\n6. Tên món giá > 50,000:")
print(tree.xpath("//MON[GIA>50000]/TENMON/text()"))

# 7. Lấy số bàn của hóa đơn HD03
print("\n7. Số bàn của hóa đơn HD03:")
print(tree.xpath("//HOADON[@SOHD='HD03']/@TENBAN"))

# 8. Lấy tên món có mã M02
print("\n8. Tên món có mã M02:")
print(tree.xpath("//MON[@MAMON='M02']/TENMON/text()"))

# 9. Lấy ngày lập của hóa đơn HD03
print("\n9. Ngày lập hóa đơn HD03:")
print(tree.xpath("//HOADON[@SOHD='HD03']/@NGAYLAP"))

# 10. Lấy tất cả mã món trong hóa đơn HD01
print("\n10. Mã món trong hóa đơn HD01:")
print([ct.get("MAMON") for ct in tree.xpath("//CTHD[@SOHD='HD01']")])

# 11. Lấy tên món trong hóa đơn HD01
print("\n11. Tên món trong hóa đơn HD01:")
mamons_hd01 = [ct.get("MAMON") for ct in tree.xpath("//CTHD[@SOHD='HD01']")]
print([tree.xpath(f"//MON[@MAMON='{m}']/TENMON/text()") for m in mamons_hd01])

# 12. Lấy tên nhân viên lập hóa đơn HD02
print("\n12. Tên nhân viên lập hóa đơn HD02:")
manv_hd02 = tree.xpath("//HOADON[@SOHD='HD02']/@MANV")
print(tree.xpath(f"//NHANVIEN[@MANV='{manv_hd02[0]}']/TENNV/text()") if manv_hd02 else [])

# 13. Đếm số bàn
print("\n13. Số bàn:")
print(int(tree.xpath("count(//BAN)")))

# 14. Đếm số hóa đơn lập bởi NV01
print("\n14. Số hóa đơn lập bởi NV01:")
print(int(tree.xpath("count(//HOADON[@MANV='NV01'])")))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
print("\n15. Tên món trong hóa đơn của bàn số 2:")
sohd_ban2 = [hd.get("SOHD") for hd in tree.xpath("//HOADON[@TENBAN='B02']")]
mamons_ban2 = [ct.get("MAMON") for ct in tree.xpath(f"//CTHD[@SOHD='{sohd_ban2[0]}']") ] if sohd_ban2 else []
print([tree.xpath(f"//MON[@MAMON='{m}']/TENMON/text()") for m in mamons_ban2] if mamons_ban2 else [])

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
print("\n16. Nhân viên từng lập hóa đơn cho bàn số 3:")
manvs_ban3 = [hd.get("MANV") for hd in tree.xpath("//HOADON[@TENBAN='B03']")]
print([tree.xpath(f"//NHANVIEN[@MANV='{m}']/TENNV/text()") for m in manvs_ban3] if manvs_ban3 else [])

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
print("\n17. Hóa đơn do nhân viên nữ lập:")
manvs_nu = [nv.get("MANV") for nv in tree.xpath("//NHANVIEN[GIOITINH='Nu']")]
print([hd.get("SOHD") for hd in tree.xpath("//HOADON") if hd.get("MANV") in manvs_nu])

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
print("\n18. Nhân viên từng phục vụ bàn số 1:")
manvs_ban1 = [hd.get("MANV") for hd in tree.xpath("//HOADON[@TENBAN='B01']")]
print([tree.xpath(f"//NHANVIEN[@MANV='{m}']/TENNV/text()") for m in manvs_ban1] if manvs_ban1 else [])

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
print("\n19. Món được gọi nhiều hơn 1 lần:")
mamons = [ct.get("MAMON") for ct in tree.xpath("//CTHD")]
from collections import Counter
counts = Counter(mamons)
print([m for m, c in counts.items() if c > 1])

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
print("\n20. Tên bàn + ngày lập hóa đơn SOHD='HD02':")
hoadon_hd02 = tree.xpath("//HOADON[@SOHD='HD02']")
if hoadon_hd02:
    tenban = hoadon_hd02[0].get("TENBAN")
    ngaylap = hoadon_hd02[0].get("NGAYLAP")
    print([(tenban, ngaylap)])
else:
    print([])
