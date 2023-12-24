student_heights = input().split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])

height_sum = 0
student_count = 0
for height in student_heights:
  height_sum += height
  student_count +=1
print(f"total height = {height_sum}")
print(f"number of students = {student_count}")
average_height = round(height_sum/student_count)
print(f"average height = {average_height}")
