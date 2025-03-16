def total_salary(path):
    salaries = []
    try:
        with open(path, 'r', encoding="utf-8") as salary_file:
            for line in salary_file:
                line = line.strip() # remove spaces
                if not line:
                    continue

                parts = line.split(',') # split line
                if len(parts) < 2: # check if line contains something after ,
                    print(f"Error: incorrect line -> {line}")
                    continue

                try:
                    salary = float(parts[1].strip())
                    salaries.append(salary)
                except ValueError: # check if second could be convert into int 
                    print(f"Error: Cannot convert to int -> {parts[1].strip()}")
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    
    if not salaries:  # check if there is one salary
        print(f"File does not contain info about salaries")
        return 0, 0 

    total = sum(salaries)
    average = total / len(salaries)

    return total, average


total, average = total_salary('university-python/goit-pycore-hw-04/hw1/salary.txt')
print(f'Total salary: {total}, Average salary: {average}')


total, average = total_salary('university-python/goit-pycore-hw-04/hw1/salary1.txt')
print(f'Total salary: {total}, Average salary: {average}')

total, average = total_salary('university-python/goit-pycore-hw-04/hw1/salary2.txt')
print(f'Total salary: {total}, Average salary: {average}')