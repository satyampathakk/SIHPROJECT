from .models import *

def Predict():
    students = Student.objects.all()

    for student in students:
        quiz1 = student.quiz1
        quiz2 = student.quiz2
        quiz3 = student.quiz3
        pre_end = student.preend
        ment=student.mentor

        total_marks = 0
        total_quizzes = 0

        if quiz1 is not None:
            total_marks += quiz1
            total_quizzes += 1

        if quiz2 is not None:
            total_marks += quiz2
            total_quizzes += 1

        if quiz3 is not None:
            total_marks += quiz3
            total_quizzes += 1

        

        quiz_percent = (total_marks / (30 * total_quizzes)) * 100



        if pre_end is not None:
            total_percentage = ((quiz_percent) + (pre_end * 1.5) + (ment * 10 * 1.5)) / 4
        else:
            total_percentage = ((quiz_percent) + (ment * 10 * 1.5)) / 2.5

        predict = total_percentage * 0.7
        student.predict=predict
        if predict>=35:
            student.slow_learner='slow learner'


        student.save()