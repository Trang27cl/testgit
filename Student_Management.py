#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ListStudent import ListStudent

class Program:
    def __init__(self):
        self.dssv = ListStudent()
        #self.dssv.load()
        self.dssv.loadFromFile('students.txt')
        
        
    def run(self):
        while 1:
            print('============ QUẢN LÝ SINH VIÊN ============')
            print('=== 1. Hiển thị danh sách (load data)   ===')
            print('=== 2. Thêm sinh viên                   ===')
            print('=== 3. Chỉnh sửa thông tin              ===')
            print('=== 4. Xoá thông tin sinh viên          ===')
            print('=== 5. Tìm kiếm thông tin               ===')
            print('=== 6. Sắp xếp                          ===')
            print('=== 7. Lưu dữ liệu (*.txt)              ===')
            print('=== 8. Đóng chương trình                ===')
            print('===========================================')
            choice = input('Nhập lựa chọn: ')
            if choice=='1':
                self.dssv.info()
            elif choice =='2':
                code = input('Nhập mã sinh viên: ')
                name = input('Nhập họ tên sinh viên: ')
                date = input('Nhập ngày sinh sinh viên: ')
                residence = input('Nhập quê quán sinh viên: ')
                new_stud = Student(code, name, date, residence)
                self.dssv.add(new_stud)
                print('Thêm sinh viên mới thành công!')
            elif choice =='3':
                code_updating = input('Nhập mã sinh viên cần chỉnh sửa: ')
                exist = False
                for st in self.dssv.L:
                    if st.code == code_updating:                                        
                        name = input('Nhập họ tên sinh viên (Nếu không cập nhật thì để trống): ')
                        date = input('Nhập ngày sinh sinh viên (Nếu không cập nhật thì để trống): ')
                        residence = input('Nhập quê quán sinh viên (Nếu không cập nhật thì để trống): ')
                        newinfo = Student(code_updating, name, date, residence)
                        succeded = self.dssv.update(code_updating, newinfo)
                        if succeded:
                            print('Cập nhật thành công!')
                        else:
                            print('Cập nhật thất bại.')
                        exist = True
                        break
                if not exist:
                    print(f'Mã sinh viên {code_updating} không tồn tại.')
            elif choice =='4':
                deleting = input('Nhập mã sinh viên cần xoá: ')
                succeded = self.dssv.delete(deleting)
                if succeded:
                    print('Xoá thành công')
                else:
                    print(f'Xoá thất bại. Có thể mã sinh viên {deleting} không tồn tại')
            elif choice =='5':
                keyword = input('Nhập từ khoá tìm kiếm: ')
                result = self.dssv.search(keyword)
                if len(result.L)==0:
                    print('Không tìm thấy kết quả')
                else:
                    print(f'Tìm thấy {len(result.L)} kết quả phù hợp.')
                    result.info()
            elif choice =='6':
                column = input('Nhập lựa chọn để sắp xếp: 0 - theo mã, 1 - theo tên, 2 - theo ngày sinh, 3 - theo quên quán:')
                column = int(column)
                self.dssv.sort(column)
                print('Sắp xếp thành công!')
            elif choice =='7':
                self.dssv.saveToFile('students.txt')
                print('Lưu dữ liệu thành công')
            elif choice=='8':
                confirm = input('Bạn muốn đóng chương trình (y/n)? ')
                if confirm=='y' or confirm=='Y':
                    break
            else:
                print('Lựa chọn sai! Bấm 1->7 để lựa chọn các tác vụ.')
            input('Nhấn enter để tiếp tục...')
        print('Chương trình kết thúc...')

