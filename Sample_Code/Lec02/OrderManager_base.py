orders = []

menu = '''--------------------------------
Menu:
1. Thêm sản phẩm
2. Hiển thị đơn hàng
3. Sửa một sản phẩm
4. Xóa một sản phẩm
0. Thoát chương trình
--------------------------------
'''

while True:
    choice = int(input(menu))

    if choice == 0:
        break
    
    elif choice == 1:
        print("Chức năng thêm sản phẩm")
    
    elif choice == 2:
        print("Chức năng hiển thị đơn hàng")
    
    elif choice == 3:
        print("Chức năng sửa một sản phẩm")
    
    elif choice == 4:
        print("Chức năng xóa một sản phẩm")
    
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')

print('Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi.')
