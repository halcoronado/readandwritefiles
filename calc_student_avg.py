
import csv
scores = open("Student_Scores.csv","r")

student_file = csv.reader(scores, delimiter=',')

studentaverage = open('student_avg.csv','w')

for student in student_file:
    score_1 = int(student[1])
    score_2 = int(student[2])
    score_3 = int(student[3])
    average = (score_1 + score_2 + score_3)/3
    average = format(average,',.2f')
    studentaverage.write(student[0] + ' ')
    studentaverage.write(average + '\n')
    
student_file.close()
studentaverage.close()



