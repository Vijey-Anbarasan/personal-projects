print("The Love Calculator is calculating your score...")
name1 = input("What is your name?" )
name2 = input("What is their name?" )


combined_names = name1 + name2
# print(combined_names.replace(" ","").lower())
lowered_combined_names = combined_names.lower()

t_count = lowered_combined_names.count('t')
r_count = lowered_combined_names.count('r')
u_count = lowered_combined_names.count('u')
e_count = lowered_combined_names.count('e')

l_count = lowered_combined_names.count('l')
o_count = lowered_combined_names.count('o')
v_count = lowered_combined_names.count('v')

true_check = t_count + r_count + u_count + e_count
love_check = l_count + o_count + v_count + e_count

combined_love_score = int(str(true_check) + str(love_check))
# combined_love_score = int(love_score)

if combined_love_score < 10 or combined_love_score > 90:
  print(f"Your score is {combined_love_score}, you go together like coke and mentos.")
elif combined_love_score > 40 and combined_love_score < 50:
  print(f"Your score is {combined_love_score}, you are alright together.")
else:
  print(f"Your score is {combined_love_score}.")