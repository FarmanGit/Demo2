'''
Created on 05-Apr-2018

@author: viky
'''

if __name__ == '__main__':
    pass
def largest(num1, num2, num3):
        if (num1 > num2) and (num1 > num3):
            largest_num = num1
        elif (num2 > num1) and (num2 > num3):
            largest_num = num2
        else:
            largest_num = num3
        print("The largest of the 3 numbers is : ", largest_num)