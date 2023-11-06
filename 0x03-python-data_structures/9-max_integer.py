#!/usr/bin/python3
def max_integer(my_list=[]):
   if my_list == "":
       return None
   else:
       m_int = my_list[0]
       for i in my_list:
           if i > m_int:
               m_int = i
               return m_int
