#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
    
    def __init__(self, code, name, dateofbirth, residence):
        self.code = code
        self.name = name
        self.dateofbirth = dateofbirth
        self.residence = residence
    
    def info(self):
        row = self.code.ljust(20, ' ')+self.name.ljust(25, ' ')+self.dateofbirth.ljust(25, ' ')+self.residence
        print(row)
        
    def rowforwriting(self):
        row = f'{self.code}|{self.name}|{self.dateofbirth}|{self.residence}|\n'
        return row

