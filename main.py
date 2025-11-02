from student_utils.marks import calculate_total, calculate_average
from student_utils.grades import get_grade
from student_utils.remarks import get_remark

def main(): 
    print("Smart Student Analyzer")
    name=input("Enter name:")
    marks = list(map(int, input("Enter 5 subject marks (separated by space): ").split()))

    total=calculate_total(marks)
    avg=calculate_average(marks)
    grade=get_grade(avg)
    remark=get_remark(grade)

    print("Result Summary")
    print(f"Name:{name}")
    print(f"Total marks:{total}")
    print(f"Average:{avg}")
    print(f"Grade:{grade}")
    print(f"Remark:{remark}")
if __name__=="__main__":
    main()