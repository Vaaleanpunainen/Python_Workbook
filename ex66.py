# program computes a grade point average


flag = True
sm = 0
av = 0

while flag:
    letter = (input("Enter a letter grade: ")).upper()

    if letter == "":
        flag = False
    else:
        av += 1
        if letter == "A-":
            gp = 3.7
        elif letter[0] == "A":
            gp = 4.0
        elif letter == "B+":
            gp = 3.3
        elif letter == "B":
            gp = 3.0
        elif letter == "B-":
            gp = 2.7
        elif letter == "C+":
            gp = 2.3
        elif letter == "C":
            gp = 2.0
        elif letter == "C-":
            gp = 1.7
        elif letter == "D+":
            gp = 1.3
        elif letter == "D":
            gp = 1.0
        elif letter == "F":
            gp = 0
        sm = sm + gp




print("The average grade points: %s" %(sm/av))
