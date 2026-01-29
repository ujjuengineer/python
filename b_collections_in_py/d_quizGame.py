# quiz game, where we will store the questions, options, answers and guesses by the user

# question stored in tuples as we will not change it in future

questions = ("national bird of india ?", "national flag of india", "national fruit of india", "king of vegitables ?")

options = (("A. peacock", "B. kalu", "C. dogesh", "D. gandesh"), ("A. xyz", "B. zyx", "C. trianga", "D. kalu ki chaddi"), ("A. apple", "B. bnana", "C. grapes", "D. mango"), ("A. baigan", "B. aalu", "C. bhindi", "D. loki"))

answer = ("a", "c", "d", "b")

guess = [] # store the guess by the user

question_number = 0

score = 0


for idx, ques in enumerate(questions) :
    print(ques)

    for opt in options[idx] : 
        print(opt)

    print("choose option : A, B, C, D : ", end = " ")

    correctAns = answer[idx]

    ans = input()
    
    guess.append(ans)

    if ans.lower() == correctAns : 
        score += 1
        print("correct answer")
    else: 
        print("wrong answer")
    print(); 

print(f"your score is {score}/4")
print()