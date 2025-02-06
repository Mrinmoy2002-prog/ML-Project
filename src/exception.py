import sys   
from src.logger import logging

def error_message_detail(error,error_detail:sys):  #error_detail is present inside the sys
    _,_,exc_tb = error_detail.exc_info()   # The .exc_info() returns a tuple and the first two values are not taken so _,_,exc_tb and this exc_tb stores the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename # This gives the name of the file
    error_message = "Error Occured in python script name [{0}] line number[{1}] error message[{2}]".format(  # 0 , 1 and 2 are the placeholder text and instead of those the values inside the format will get printed

        file_name,exc_tb.tb_lineno,str(error)  #error contains the error message 

        
    )
    return error_message
    

# Whenever error is raised the above function will get called by the below class
class CustomException(Exception):        # The Exception class is being inherited by the CustomException class 
    def __init__(self,error_message,error_detail:sys):   # self is a object for this class
        super().__init__(error_message)     # __init__ is a attribute of the base class i.e Exception so call using super()
        self.error_message = error_message_detail(error_message,error_detail)   #here the calling occurs

    def __str__(self):
        return self.error_message
    
#Whenever a error occurs that will call this CustomException class and that will call the error_message_detail function 

if __name__ =="__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero error")  #This is basically the error message
        raise CustomException(e,sys)
        