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
        name = input('Nhập tên sản phẩm: ')
        price = int(input('Nhập giá sản phẩm: '))
        qty = int(input('Nhập số lượng: '))
        order = {'name': name, 'price': price, 'qty': qty}
        orders.append(order)
        print(f'Đã thêm sản phẩm: {name}')
    
    elif choice == 2:
        if len(orders) == 0:
            print('Chưa có sản phẩm nào trong đơn hàng.')
        else:
            print("Danh sách đơn hàng:")
            for i, order in enumerate(orders):
                print(f'{i+1}. {order["name"]} - {order["price"]} - {order["qty"]}')
    
    elif choice == 3:
        if len(orders) == 0:
            print('Chưa có sản phẩm nào trong đơn hàng.')
        else:
            print("Danh sách đơn hàng:")
            for i, order in enumerate(orders):
                print(f'{i+1}. {order["name"]} - {order["price"]} - {order["qty"]}')
            
            index = int(input('Chọn số thứ tự sản phẩm bạn muốn sửa: ')) - 1
            
            if index >= len(orders) or index < 0:
                print('Số thứ tự không hợp lệ.')
            else:
                order = orders[index]
                new_name = input('Nhập tên sản phẩm mới (hoặc nhấn Enter để giữ nguyên): ')
                new_price = input('Nhập giá sản phẩm mới (hoặc nhấn Enter để giữ nguyên): ')
                new_qty = input('Nhập số lượng mới (hoặc nhấn Enter để giữ nguyên): ')
                
                if new_name:
                    order['name'] = new_name
                if new_price:
                    order['price'] = int(new_price)
                if new_qty:
                    order['qty'] = int(new_qty)
                
                print('Sản phẩm đã được cập nhật.')
    
    elif choice == 4:
        if len(orders) == 0:
            print('Chưa có sản phẩm nào để xóa.')
        else:
            print("Danh sách đơn hàng:")
            for i, order in enumerate(orders):
                print(f'{i+1}. {order["name"]} - {order["price"]} - {order["qty"]}')
            
            index = int(input('Chọn số thứ tự sản phẩm bạn muốn xóa: ')) - 1
            
            if index >= len(orders) or index < 0:
                print('Số thứ tự không hợp lệ.')
            else:
                order = orders.pop(index)
                print(f'Sản phẩm {order["name"]} đã được xóa.')
    
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')

print('Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi.')
