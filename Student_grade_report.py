students=[("Alice",85),("Bob",72),("Charlie",38),("David",90),("Eva",35)]
score_total=0
counter=0
for name,score in students:
    if score>75:
        print("The name of the student is : " ,  name)
    #    To find the avg score
    score_total=score_total+score
    if score<40:
        counter=counter+1
print("The average of the score is: " , score_total/len(students))
print("The no. of students who scored less than 40 is:", counter)