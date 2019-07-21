from datetime import datetime
import time

curTime = datetime.now()

# print out with no format
print("This output is without format{0}".format(curTime))


# print out with different format
print("This output is with different formats of {0}".format(curTime))

# 2019-07-14 01:43:12
print (curTime.strftime("%Y-%m-%d %H:%M:%S"))
# 2019/07/14
print (curTime.strftime("%Y/%m/%d"))
# 01:43:12
print (curTime.strftime("%H:%M:%S"))
# 01:43:12 AM
print (curTime.strftime("%I:%M:%S %p"))
# Sun, Jul 14, 2019
print (curTime.strftime("%a, %b %d, %Y"))


print("The timezone of this machine is {0}".format(time.tzname))



