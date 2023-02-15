# Fruits=['apple','banana', 'pear']
# for fruit in Fruits:
# 	print(fruit)
# 	print(fruit + ' mango smoothie')


# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# total_height = 0
# for height in student_heights:
# 	total_height+=height
# print(total_height)

# number_of_student=0
# for number in student_heights:
# 	number > student_heights
# print(number)

# average = round(total_height/number_of_student)
# print(average)

#Write your code below this row 👇


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f'The highest score is {highest_score}')




	