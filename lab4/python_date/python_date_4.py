import datetime 
x = input("Enter the first date (YYYY-MM-DD HH:MM:SS)")
y = input("Enter the first date (YYYY-MM-DD HH:MM:SS)")
date_1= datetime.srpttime(x,"%Y-%m-%d %H:%M:%S")
date_2= datetime.srpttime(y,"%Y-%m-%d %H:%M:%S")
date =  date_2 - date_1
date = date.total_seconds()
print(date)

