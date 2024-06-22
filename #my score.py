#my score
import math
print("Enter 10 test scores:")
lst = []
n = 10
for i in range(n):
    lst.append(float(input()))
lst.sort()

# Tính giá trị nhỏ nhất
min_value = lst[0]
print("Min =", min_value)

# Tìm giá trị lớn nhất
max_value = lst[-1]
print("Max =", max_value)

# Tính giá trị trung bình
def average(scores):
    return sum(scores) / len(scores)

avg = average(lst)
print("Average =", avg)

# Tìm giá trị lớn thứ 2
second_large = lst[-2]
print("Second largest =", second_large)

# Nhắc nhở giá trị vượt quá 100
for score in lst:
    if score > 100:
        print("Warning: A value over 100 has been entered.")
        break

# Xóa 2 số thấp nhất và tính trung bình phần còn lại
if len(lst) > 2:
    average_after_dropping = average(lst[2:])
    print("Average after dropping the 2 lowest numbers =", average_after_dropping)
else:
    print("Not enough numbers to drop 2 lowest values.")


