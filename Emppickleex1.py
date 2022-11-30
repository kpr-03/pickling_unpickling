#program for accepting employee details and save them in a file
import pickle,sys
with open("Emp.data","ab") as fp: # as pickling concept always takes the file in binary format.
    while(True):
        try:
            print("-"*50)
            #accept employee data from keyboard
            eno=int(input("Enter Employee Number:"))
            ename=input("Enter Employee name:")
            sal=float(input("Enter Employee Salary:"))
            dsg=input("Enter Employee Designation:")
            #add employee values to list
            lst=list()
            lst.append(eno)
            lst.append(ename)
            lst.append(sal)
            lst.append(dsg)
            pickle.dump(lst,fp)
            print("-"*50)
            print("Employee data saved successfully in file")
            print("-"*50)
            ch=input("do you want to enter another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thanks for using this program")
                sys.exit()
        except ValueError:
            print("Don't use strs/symbols/alpha-nums for employee number and salary")