# def func(*args):
#     list = func[2,3,4,5,6,8,9,5,2,5,8]
#     pil = 0
#     for i in list:
#     # print(i)
#     # if i / 2 == 1:
#         pil += i
#     func(pil)
# def narcissistic( value ):



# def narcissistic(value):
#     amoun_numbers = len(str(value))
#     amoun_number = 0 
#     m = 0
#     l = 0 
#     number = str(value)
#     for i in number:
#         amoun_number += len(i)
#         m = (int(number[amoun_number-1]))  
#         l += m **  amoun_numbers
#     number = int(number) 
#     if l == number:
#         return True
#     else:
#         return False
# narcissistic(153)




# def solution(string, ending):
#     print(string[2])

# solution('abc', 'bc')  
    

 

 

 

# def digitize(n):              
#     s = []
#     for  i in str(n):
#       s.append(int(i))
#     l = []
#     # s = reversed(s)
#     for i in s:
#     #    i = int(i)
#        l.append(i)
#     print(l)
# digitize(348597)



# def get_planet_name(id):
#     # This doesn't work; Fix it!
#     name=""
#     case = id
#     if  id == 1:
#         name = "Mercury"
#     if id ==  2: name = "Venus"
#     if id == 3: name = "Earth"
#     if case == 4: name = "Mars"
#     if case == 5: name = "Jupiter"
#     if case == 6: name = "Saturn"
#     if case == 7: name = "Uranus"  
#     if case == 8: name = "Neptune"
#     return name
# get_planet_name(1)
 

# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)
 
 
# def bool_to_word(boolean):
# #     boolean = str(boolean)
#     if boolean == 'Yes':
#         print(True)
#     elif boolean == 'No':
#         return False
# bool_to_word('Yes')

# def are_you_playing_banjo(name):
#     # Implement me!
     
#     if name[0] == "R" or name[0] == 'r':
#        name += "plays banjo"
#     else:
#        name += 'does not plase banjo'
    
    
    
    
    
#     print(name)
# are_you_playing_banjo('lianna')




# def sum_array(a):
 
#     a =  float(sum(a))
#     if a == None:
#         return 0
#     else:
#         if a - int(a) != 0:
#             print(a)
#         else: 
#             print(int(a))
     
# sum_array([1.1, 2.2, 3.3])
# sum_array([6,7,7,6,54])



# def sum_array(a):
#     a = sum(a)
#     print(a)
# sum_array([])





# def count_sheeps(sheep):
#    n = []
#    for i in sheep:
#     if i == True:
#         n.append(i)
#    return len(n) 

# sheep = [True,  True,  True,  False,
#           True,  True,  True,  True ,
#           True,  False, True,  False,
#           True,  False, False, True ,
#           True,  True,  True,  True ,
#           False, False, True,  True ]


           
     
# count_sheeps(sheep)
   


# def get_status(is_busy):
#     status = "busy" if is_busy == True else "available"
#     statuss = ["status"]
#     # return status
    
#     print(f"{statuss},", status)
# get_status(False)



# import re
# from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


# def digitize(n):
#     '''
#     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
#     ⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
#     ⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
#     ⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀
#     ⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀
#     ⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀
#     ⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
#     ⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
#     ⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁
#     ⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
#     ⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀
#     ⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾⠀⠀
#     ⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇⠀⠀
#     ⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⠀⡇⠀⠀
#     ⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣧⠀⠀
#     ⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀⢸⠀⠀
#     ⣿⠀⡇⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇⠀
#     ⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀⠀⠀⢹⡀
#     ⡇⠀⠇⠀⠀⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂⠀⠀⠀⠀⠀⠀⢧
#     ⣇⠀⢠⠀⠀⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
#     ⢻⠀⠈⠰⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀⠀⠀⠀⠀
#     ⠸⡆⠀⠀⠇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⡀
#     '''
#     return list(map(int, str(n)))[::-1]



# class Solution(object):
#     def reorderedPowerOf2(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
    
#         if 1 <= n <= 109:
#             print(True)
#         else:
#             print(False)
#         return  self.n  
    
# Solution.reorderedPowerOf2(n=1)
   
 