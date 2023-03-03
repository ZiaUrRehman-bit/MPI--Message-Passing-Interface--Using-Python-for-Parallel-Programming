
import os

startTime = os.times()

for i in range(1000000):

    result = i*i

for j in range(1000000):

    result = j*j

endTime = os.times()

totalUserTime = endTime.user - startTime.user
totalSystemTime = endTime.system - startTime.system

print(f"User Time: {totalUserTime}")
print(f"System Time: {totalSystemTime}")