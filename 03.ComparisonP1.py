
import os

startTime = os.times()

for i in range(1000000):

    result = i*i

for j in range(1000000):

    result = j*j

endTime = os.times()

print(f"User CPU Start Time: {startTime.user}")
# print(f"System CPU Start Time: {startTime.system}")

print(f"User CPU End Time: {endTime.user}")
# print(f"System CPU End Time: {endTime.system}")

totalUserTime = endTime.user - startTime.user
totalSystemTime = endTime.system - startTime.system

print(f"User CPU Time: {totalUserTime}")
print(f"System CPU Time: {totalSystemTime}")