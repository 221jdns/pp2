import datetime
x = datetime.datetime.now()
x = x - datetime.timedelta(days=5)
print(x.strftime("%Y:%m:%d"))