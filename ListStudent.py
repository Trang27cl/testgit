#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Student import Student
class ListStudent:
    
    def __init__(self):
        self.L = []
        
    def load(self):
        stud1 = Student('20225115', 'Lê Chí Bách', '22/6/2000', 'Hà Nội')
        stud2 = Student('20225116', 'Võ Thị Phượng', '12/7/2002', 'Hà Nam')
        stud3 = Student('20225117', 'Đặng Quang Sáng', '05/12/1999', 'Bắc Ninh')
        self.L = [stud1, stud2, stud3]
        
    def loadFromFile(self, path):
        f = open(path, "r", encoding='utf8')
        for x in f:
            if not x.__contains__('|'):
                continue
            info = x.split('|')
            st = Student(info[0], info[1],info[2],info[3])
            self.L.append(st)
        f.close()
        
    def saveToFile(self, path):
        # Lưu dữ liệu
        f = open(path, "w", encoding='utf8')
        for st in self.L:
            f.write(st.rowforwriting())
        f.close()
    def info(self):
        header = 'Mã sinh viên'.ljust(20, ' ')+'Họ tên'.ljust(25, ' ')+'Ngày sinh'.ljust(25, ' ')+'Quê quán'
        print(header)
        print(''.ljust(80, '='))
        for stud in self.L:
            stud.info()
            
    def update(self, code_updating, new_info):
        succeded = False
        for st in self.L:
            if st.code == code_updating:
                # update
                if new_info.name!='':
                    st.name = new_info.name
                if new_info.dateofbirth!='':
                    st.dateofbirth = new_info.dateofbirth
                if new_info.residence!='':
                    st.residence = new_info.residence
                succeded = True
                break
        return succeded
    
    def search(self, keyword):
        '''Search by code and by name and by residence'''
        found = []
        for st in self.L:
            if st.code.startswith(keyword) or +            st.name.lower().startswith(keyword.lower()) or +            st.residence.lower().startswith(keyword.lower()):
                found.append(st)                
        return ListStudent(found)
    
    def sort(self, column):
        if column==0:
            # sắp xếp theo mã
            self.L = sorted(self.L, key=lambda x:x.code)
        elif column==1:
            self.L = sorted(self.L, key=lambda x:x.name)
        elif column==2:
            self.L = sorted(self.L, key=lambda x:x.dateofbirth)
        else:
            self.L = sorted(self.L, key=lambda x:x.residence)
    
    def add(self, st):
        self.L.append(st)
        
    def delete(self, deleting_code):
        succeded = False
        for st in self.L:
            if st.code == deleting_code:
                confirm = input(f'Bạn chắc chắn muốn xoá sinh viên có mã {deleting_code}? ')
                if confirm == 'y' or confirm =='Y':
                    self.L.remove(st)
                    succeded = True
                break
        return succeded

