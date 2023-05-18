import csv
def write_into_csv(info_list):
  with open('student_info.csv','a','newline='')as csv_file:
            if csv_file.tell()==0:
            write.writerow(['Name','Age','Contact Number','Email Id'])
            write.writerow(info_list)
if __name__ == '__main__':
            condition==True
            student_num=1
while(condition): 
            student_info=input("Enter student information for student #{} in the following format (Name Age ContactName EmailID):".format(student.num))
#split
student_info_list=student_info.split('')
            
 print("\nThe entered information is-\nNamw:{}\nAge:{}\nContact Number:{}\nEmailID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
 choice_check=input("Is the entered information correct?(yes/no):")
 if choice_check=="yes":
      write_into_csv(student_info_list)
      condition_check=input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check=="yes":
                condtion=True
                student_num=student_num+1
            elif condition_check =="no":
                condition=False
elif choice_check =="no":
            print("\nPlease re-enter the value")
            
                   
            
         
            
            
          
