import random

#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

# n=int(input("Enter the number you want to sum upto:"))
# total=0
# for i in range(0,n+1):
#     total=total+i
# print(total)

#**************************************
#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

# n=int(input("Enter the number you want to sum upto:"))
# total=0
# for i in range(1,n+1):
#     if i%3==0 or i%5 == 0:
#
#         print(i)
#         total=total+i
# print(total)

# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

#**************************************


#Write a program that prints a multiplication table for numbers up to 12
# n=2
# q=1
# for i in range (1,11):
#     table = i *n
#     print(q ,'x' , n ,'=',table)
#     q=q+1
#**************************************
# Write a guessing game where the user has to guess a secret number.

# rannum=random.randint(1,8)
# print(rannum)
#
#
# count = 0
# while count<=3 :
#     n= int(input("Enter your guessed Number"))
#     count+=1
#     if n > rannum:
#         print("You have entered a Greater Number")
#     if n< rannum:
#         print("You have entered a Lesser Number")
#     if n == rannum:
#         print(" You have guessed Correct Number")
#         break
#********************************************************************
#Write a program that prints the next 20 leap years.

# for i in range (2020,2060):
#     if (i%4 == 0)and (i%100 !=0):
#         print(i)

#**************************************
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# def integraldic(n):
#     intdic={}
#
#     for i in range (1,n+1):
#         sqint=i*i
#         intdic.update({i:sqint})
#
#     print (intdic)
#
# integraldic(8)
#
#**************************************
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# def seq():
#     seqin=input("Enter a seq of comma sep numbers:")
#
#     spilitseq=seqin.split()
#
#     print(spilitseq)
#     tupseq=eval(seqin)
#     print (str(tupseq))
# seq()


# ****************************************

# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

# def sum_double(a, b):
#     if a==b:
#         double=a**2
#         return double
#     else:
#         sum=a+b
#         return sum
#
# sum_double(4,4)

# **********************************************************************
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#
#
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0
#
# def diff21(n):
#     diff= 21-n
#     if n>=21:
#         print (diff**2)
#     else:
#         print (diff)
#
# diff21(19)

# ***********************************************************************************

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10

# def makes10(a, b):
#
#     c = a+b
#     if (a ==10) or (b==10) or (c==10):
#         return True
#     else:
#         return False
#
# total =makes10(0,10)
# print (total)
#*****************************************************************************************************

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

# def findhund(n):
#     diff=100-abs(n)
#     if diff >=11:
#         return False
#     else:
#         return True
# nearhun=findhund(-93)
# print (nearhun)


#**********************************************************
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


#***********************************************************************************************************
# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

# def not_string(st):
#
#     splittext=st.split()
#     if splittext[0] == 'not':
#         return st
#     else:
#         return 'not'+st
#
#
# finaltext =not_string('spicy')
#
# print(finaltext)
#***********************************************************************************************************************

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#
#
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'


# def missing_char(word, n):
#
#     newstr=word[n-1:n]+word[n+1:]
#
#     print(newstr)
#
# missing_char('kitten',2)

# **************************************************************************

# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'
#
# def string_times(str, n):
#     final = str
#
#     for i in range(1,n):
#         final = str + final
#
#     print (final)
#
# string_times('hi',4)
#********************************************************************************

# def front_times(str, n):
#     spilstr=str[:n]
#     timesstr =  spilstr*n
#
#     print (spilstr)
#     print (timesstr)
#
# front_times('abc',3)

# ***********************************************************************************
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'
#
# def string_bits(str):
#
#     result =''
#     for i in  range(0,len(str),2):
#
#         loopresult=str[i]
#         result=result+loopresult
#     print (result)

# string_bits('Heeololeo')
# *********************************************************************************************
# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
#
# def string_splosion(str):
#     result =''
#
#     for i in range(0,len(str)+1):
#         result = result+str[:i]
#     print(result)

# string_splosion('Code')
# # *********************************************************************************************
# Given an array of ints, return the number of 9's in the array.
#
#
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3
#
# def array_count9(nums):
#
#     findnumber=9
#     count = 0
#     for i in nums:
#         if i==9:
#             count =count+1
#     print (count)
#
#
# array_count9([1, 9, 9,3,9])

# **********************************************************************************

# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
#
#
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False
#
# def array_front9(nums):
#
#     if len(nums)>4:
#         end =4
#     for i in range(0,4):
#         if nums[i]==9:
#             return True
#
#     return False
#
# final=array_front9([1, 2, 8, 3, 4])
# print(final)

# *****************************************************************************



# def string_splosion(str):













# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2


#************************
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
#
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
#
#

# arr=[1, 1, 2, 3, 2]
#
# flag=False
# for i in range(len(arr)-1):
#
#     if arr[i]==1:
#         if arr[i+1:i+3]==[2,3]:
#             print(arr[i],arr[i+1:i+3])
#
#             flag=True
#             break
#
#
# print (flag)
#solution 2:
# for i in range(len(arr)-2):
#     if arr[i]==1 and arr[i+1]and arr[i+2]==3:
#         print("True")
# else:
#      print("False")
#

#********************************************************************************
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0


match=['abc', 'aba']

findstring='ab'

for i in match:

    index=i.index('ab')
    print(index)