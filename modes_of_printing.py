'''Name:Goutham
date=19-05-2022
file name= modes of printing
'''
name=input('name')
empid=int(input('empid'))
salary=float(input('salary'))
contact_no=int(input('phone no'))
system_no=input('system no')

# print('my name is',name,'and employid is',empid)
# print('my salary in the month march',salary)
# print('my contact no is',contact_no, 'my system number is',system_no)
'''using format specifier'''
# print('my name is %s and employid is %d'%(name,empid))
# print('my salary in the month march %.3f'%salary)
# print('my contact no is %i and my system is %s'%(contact_no,system_no))
'''f--->fast string '''
# print(f'my name is{name} and employid is {empid}')
# print(f'my salary in the month march {salary}')
# print(f'my contact no is {contact_no} and my system no is{system_no}')


# print('my name is '+name+' and my employee id is '+str(empid))
# print('my salary for the month of may is '+str(salary))

# print('my name is '+name+' and my employee id is'+str(empid)+'\nmy salary for the month of may is '+str(salary))

# print('my name is {0} and my employee id is {1} and contact number is {2}'.format(name,empid,contact_no))
# print('my salary in the month of may is {0} and my system number is {1}'.format(salary,system_no))

# print('my name is {2} and my employee id is {0} and contact number is {1}'.format(name,empid,contact_no))
# print('my salary in the month of may is {0} and my system number is {1}'.format(salary,system_no))

