"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
Ex -: Www.HackerRank.com → wWW.hACKERrANK.COM
Ex -: Pythonist 2 → pYTHONIST 2  

"""

def swap_case (s):
    return s.swapcase()
    
s = '''HackerRank.com presents "Pythonist 2".'''
swap_case(s)