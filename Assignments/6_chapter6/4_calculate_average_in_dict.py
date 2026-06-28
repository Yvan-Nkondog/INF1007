
# Write a script that calculate the averages of students. Names = dict keys and 
# result = dict values. Also return the name of the student with the highest mark.

def compute_average_and_best_result(names_and_marks: dict) -> tuple:
    average = sum(names_and_marks.values()) / len(names_and_marks)
    highest_mark = max(names_and_marks.values())
    result_dict = {}
    for name, mark in names_and_marks.items():
        if mark == highest_mark:
            result_dict[name] = mark
    return average, result_dict


if __name__ == "__main__":
    names_and_marks = {"John": 13, "Paul": 12, "Martin": 19, "Benjamin": 20, "FRB": 20}
    print(compute_average_and_best_result(names_and_marks))