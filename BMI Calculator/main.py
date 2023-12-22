height = input("enter height in meters: ")
weight = input("enter weight in kilograms: ")

int_weight = int(weight)
# print(type(int_weight))
float_height = float(height)
# print(type(float_height))

BMI = (int_weight/float_height**2)
print(int(BMI))