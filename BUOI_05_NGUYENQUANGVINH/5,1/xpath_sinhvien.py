from lxml import etree

# Đọc file XML
tree = etree.parse("BUOI_05_NGUYENQUANGVINH/5,1/sinhvien.xml")

print(" 1. Lấy tất cả sinh viên ")
print(tree.xpath("//student"))

print("\n 2. Liệt kê tên tất cả sinh viên ")
print(tree.xpath("//student/name/text()"))

print("\n 3. Lấy tất cả id của sinh viên ")
print(tree.xpath("//student/id/text()"))

print("\n 4. Lấy ngày sinh của sinh viên có id = 'SV01' ")
print(tree.xpath("//student[id='SV01']/date/text()"))

print("\n 5. Lấy các khóa học ")
print(tree.xpath("//enrollment/course/text()"))

print("\n 6. Lấy toàn bộ thông tin của sinh viên đầu tiên ")
first_student = tree.xpath("//student[1]")[0]
print(etree.tostring(first_student, pretty_print=True).decode())

print("\n 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203' ")
print(tree.xpath("//enrollment[course='Vatly203']/studentRef/text()"))

print("\n 8. Lấy tên sinh viên học môn 'Toan101' ")
print(tree.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"))

print("\n 9. Lấy tên sinh viên học môn 'Vatly203' ")
print(tree.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"))

print("\n 10. Lấy ngày sinh của sinh viên có id='SV01' ")
print(tree.xpath("//student[id='SV01']/date/text()"))

print("\n 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997 ")
students = tree.xpath("//student[starts-with(date,'1997')]")
names_dates = [(s.findtext("name"), s.findtext("date")) for s in students]
print(names_dates)

print("\n 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998 ")
print(tree.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()"))

print("\n 13. Đếm tổng số sinh viên ")
print(int(tree.xpath("count(//student)")))

print("\n 14. Lấy tất cả sinh viên chưa đăng ký môn nào ")
print(tree.xpath("//student[not(id = //enrollment/studentRef)]/name/text()"))

print("\n 15. Lấy phần tử <date> anh em ngay sau <name> của SV01 ")
print(tree.xpath("//student[id='SV01']/name/following-sibling::date/text()"))

print("\n 16. Lấy phần tử <id> anh em ngay trước <name> của SV02 ")
print(tree.xpath("//student[id='SV02']/name/preceding-sibling::id/text()"))

print("\n 17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'")
print(tree.xpath("//enrollment[studentRef='SV03']/course/text()"))

print("\n 18. Lấy sinh viên có họ là 'Trần' ")
print(tree.xpath("//student[starts-with(name, 'Trần')]/name/text()"))

print("\n 19. Lấy năm sinh của sinh viên SV01 ")
print(tree.xpath("substring(//student[id='SV01']/date,1,4)"))
