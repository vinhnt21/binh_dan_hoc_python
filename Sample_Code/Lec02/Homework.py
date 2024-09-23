students = []

menu = '''--------------------------------
Menu Quản Lý Lớp Học:
1. Thêm sinh viên
2. Hiển thị danh sách sinh viên
3. Sửa thông tin sinh viên
4. Xóa sinh viên
0. Thoát chương trình
--------------------------------
'''

while True:
    choice = int(input(menu))

    if choice == 0:
        break
    
    elif choice == 1:
        name = input('Nhập tên sinh viên: ')
        age = int(input('Nhập tuổi sinh viên: '))
        grade = input('Nhập lớp của sinh viên: ')
        student = {'name': name, 'age': age, 'grade': grade}
        students.append(student)
        print(f'Đã thêm sinh viên: {name}')
    
    elif choice == 2:
        if len(students) == 0:
            print('Chưa có sinh viên nào trong danh sách.')
        else:
            print("Danh sách sinh viên:")
            for i, student in enumerate(students):
                print(f'{i+1}. Tên: {student["name"]} - Tuổi: {student["age"]} - Lớp: {student["grade"]}')
    
    elif choice == 3:
        # Gợi ý: Học sinh tự thêm logic để chỉnh sửa thông tin sinh viên
        print("Chức năng sửa thông tin sinh viên.")
        # Học sinh có thể thêm vòng lặp để chọn sinh viên và cập nhật thông tin tại đây.
    
    elif choice == 4:
        # Gợi ý: Học sinh tự thêm logic để xóa sinh viên khỏi danh sách
        print("Chức năng xóa sinh viên.")
        # Học sinh có thể thêm vòng lặp để chọn và xóa sinh viên tại đây.
    
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')

print('Cảm ơn bạn đã sử dụng chương trình.')
