print("Exam Grade Calculator")
examName = input("What is the name of the exam?: ")
maxScore = int(input("Maximum Possible Score: "))
yourScore = int(input("Your Score: "))
percentScore = float(yourScore/maxScore * 100)
percentScore = round(percentScore, 2)
print("Your Percentage Score is: ", percentScore)
if (percentScore >= 90):
  print("You got ", percentScore, "%", "which is a A+","\N{smiling face with sunglasses}")
elif (percentScore >= 80):
  print("You got ", percentScore, "% which is a A", "\N{face with tears of joy}")
elif (percentScore >= 70):
  print("You got ", percentScore, "%, which is a B", "\N{grinning face}")
elif (percentScore >= 60):
  print("You got ", percentScore, "%, which is a C", "\N{zipper-mouth face}")
elif (percentScore >= 50):
  print("You got ", percentScore, "%, which is a D","\N{unamused face}")
else:
  print("You got ", percentScore, "%, which is a U", "\N{angry face}")