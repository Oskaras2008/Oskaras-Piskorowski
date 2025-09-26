#Author Oskaras Piskorowski
#Date 2nd September 2025
#Programme Write a programme that marks in 5 subjects and outputs the average marks

subjectone = int(input('What percentage did you get in subject one? '))
subjecttwo = int(input('What percentage did you get in subject two? '))
subjectthree = int(input('What percentage did you get in subject three? '))
subjectfour = int(input('What percentage did you get in subject four? '))
subjectfive = int(input('What percentage did you get in subject five? '))

total= subjectone + subjecttwo + subjectthree + subjectfour + subjectfive
total= int(total)

average= total/5
average= int(average)

print('The average percentage between all five subects was',average,'%')
