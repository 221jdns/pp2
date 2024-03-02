import datetime
x = datetime.datetime.now()
y = x + datetime.timedelta(days=1)
z = x - datetime.timedelta(days=1)
print(z.strftime("%Y:%m:%d"))
print(x.strftime("%Y:%m:%d"))
print(y.strftime("%Y:%m:%d"))