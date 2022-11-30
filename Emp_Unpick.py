#program for reading employee details from file
import pickle
with open("Emp.data","rb") as fp:
    print("-"*50)
    print("Empno\tName\tSalary\tDesignation")
    print("-"*50)
    while(True):
        try:
            empobj=pickle.load(fp)
            for empval in empobj:
                print("{}".format(empval),end="\t")
            print()
        except EOFError:
            print("-"*50)
            break