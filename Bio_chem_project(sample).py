import time as t
import matplotlib.pyplot as plt
from os import path#to check that the file doesnt already exist
import numpy as np
from scipy.interpolate import spline
from pylab import *

def createfile(dest):
    """
    The script creates a text file at the passed in location,
    names file based on date
    """

    date_format = t.localtime(t.time())
    today = ' %d_%d_%d'%(date_format[2],date_format[1],date_format[0])
    name_date=' %d_%d_%d.txt'%(date_format[2],date_format[1],date_format[0])#assigning the file name andformat
    ##FileName = name_of_practical + Day_Month_Year


    name_of_practical = raw_input('Enter practical name: ')
       
    if not(path.isfile(dest+name_of_practical + name_date)):#checks if file already exists

        f = open(name_of_practical + name_date,'w')
        print("\nBiochemistry electronic write-up system\n")

        name = raw_input("Enter your name: ")
        f.write("Name: ")
        f.write(name)
        f.write('\n')
        
        Reg_number = raw_input("Enter your registration number: ")
        f.write("Reg_number: ")
        f.write(Reg_number)
        f.write('\n')
        
        program = raw_input("Enter your program name: ")
        f.write("Program: ")
        f.write(program)
        f.write('\n')
        
        f.write("Date: ")
        f.write(today)
        f.write('\n')
        
        coordinator = raw_input("Enter coordinator names: ")
        f.write("Coordinator(s): ")
        f.write(coordinator)
        f.write('\n'*2)
        
        f.write('\t\t\t')
        f.write(name_of_practical)
        f.write('\n'*2)
        
        f.write("Introduction\n")
        f.write(raw_input("\nEnter the introduction of the experiment:\n"))
        f.write('\n'*2)
        
        f.write("Materials and methods\n")
        f.write(raw_input("\nName the materials and methods used in the experiment:\n"))
        f.write('\n'*2)
        
        ##
        f.write("Recording results\n")
        print("Recording results\n")
        ##
        while True:
            try:
                upper_bound=int(raw_input("Enter the total number of recordings: "))
                while upper_bound <=4:#this is to make sure that all values entered are positive and atleast 5
                    print("please try again, you need a minimum of 5 readings")#the error message for negative numbers and values less than 5
                    upper_bound=int(raw_input("Enter the total number of x and y coordinates: "))
                break
            except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
                print("Non-numeric characters are invalid, please enter a positive number for the upper bound of atleast 5")
       
        # 
        x=[]
        x_axis=raw_input("What is the variable for the x-axis: ")       
                 
        for i in range (upper_bound):
            while True:
                try:
                    x.append(float(raw_input("Enter the value for the x-axis: ")))
                    break
                except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
                    print("Non-numeric characters are invalid, please enter numbers")      
            print(x)
            
        list_x = np.array(x)
        f.write('Results for ')
        f.write(x_axis)
        f.write('\n')
        f.write(str(x))
        f.write('\n')
        
        ##
        y = []
        y_axis = raw_input("\nwhat is the the variable for the y-axis: ")
        
        for i in range (upper_bound):
            while True:
                try:
                    y.append(float(raw_input("Enter the value for the y-axis: ")))
                    break
                except ValueError:#this lets the program know what to do with with the errors by entering non-numeric data
                    print("Non-numeric characters are invalid, please enter numbers")      
            print(y)
            
        list_y = np.array(y)
        f.write('\nResults for ')
        f.write(y_axis)
        f.write('\n')
        f.write(str(y))
        f.write('\n'*2)
        ######
        
        # Label the x and y axes and title the graph.
        
        xlabel(x_axis)
        ylabel(y_axis)
        title(name_of_practical)
        
        x_smooth = np.linspace(list_x.min() ,list_x.max(),300)
        y_smooth = spline(list_x, list_y, x_smooth)
        plt.plot(x_smooth,y_smooth)
        plt.show()
                
        f.write("Analysis\n")
        f.write(raw_input("\nEnter the analysis of the experiment:\n"))
        f.write("\n"*2)
        
        f.write("Discussion\n")
        f.write(raw_input("\nEnter the discussion of the experiment:\n"))
        f.write("\n"*2)
        
        f.write("Conclusion\n")
        f.write(raw_input("\nEnter the conclusion of the experiment:\n"))
        f.write("\n"*2)
        
        f.write("References\n")
        f.write(raw_input("\nEnter the refrences of the experiment:\n"))
        f.write("\n"*2)
        
        
        f.close()
    
    
if __name__=='__main__':#if the file is the main file being run then it executes the code below
    destination='C:\\Users\\Default User\\'  #defines the file path
    createfile(destination)
