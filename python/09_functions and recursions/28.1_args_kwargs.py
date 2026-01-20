# *Args
# def fun_args(*args):
#     for item in args:
#         print(item)


# fun_args("vijay","bhaskar","Raju","Bhupathiraju")



#--------------------------------------------------
# **Kwargs
def fun_kwargs(**kwargs):
    for key,val in kwargs.items():
        print(key,val)

dict1 = {"name":"Vijay", "Age":19}
fun_kwargs(name="Vijay", Age=19)    #use "=" when assigning key words in function not ":" 
fun_kwargs(**dict1)