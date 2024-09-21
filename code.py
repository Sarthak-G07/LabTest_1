import numpy as np
import matplotlib.pyplot as plt

def operations(salary):
    salary.sort()
    print("Max Salary = ", salary[salary.size()-1])
    print("Min Salary = ",  min_salary = salary[0])
    sum =0 
    for i in salary:
        sum = sum + salary[i]
    print("Avg Salary = ", sum/i)


def change_performance(performance):
    
    while(c==True)
    
    

b = True
while(b==True):
    emp_name = input("input name = ")
    p = np.array(emp_name)
    salary = int(input("enter salary = ")) 
    q = np.array(salary)
    desig = input("enter designaton = ")
    r = np.array(desig)
    address = input("enter address = ")
    s = np.array(address)
    performance = input("enter performance = ")
    t = np.array(performance)
    a = int(input("do you want to continue, 1 for yes 0 for no = "))
    if(a==1):
        b=True
    else:
        b=False


#  u = np.array(attendence)

print(p)
print(q)
print(r)
print(s)
print(t)

operations(salary)

plt.scatter(emp_name, performance)
