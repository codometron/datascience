
#Temp converter function 
def celsius_converter(in_temp):
    new_list=[]
    for temp in in_temp:
           if type(temp)==float or type(temp)==int:
                new_list=[]
                for temp in in_temp:
                    out_temp=(9.0/5)*temp +32.0
                    new_list.append(out_temp)
        else:
            print" The number is not int or float type"
                       return new_list
