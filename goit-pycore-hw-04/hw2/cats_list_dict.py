def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding="utf-8") as cats_file:
            for line in cats_file:
                line = line.strip() # remove spaces
                if not line:
                    continue

                parts = line.split(',') # split line
                if len(parts) < 3: # check if line is full
                    print(f"Error: incorrect line -> {line}")
                    continue
                
                try:                    
                    age = int(parts[2].strip())
                    cats.append({"id": parts[0], "name": parts[1], "age": age})
                except ValueError:                    
                    print(f"Error: invalid age value -> {parts[2].strip()} in line -> {line}")


    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []  
    
    if not cats:  # check if there is one cat
        print('File does not contain info about cats')
        return []
    
    return cats


cats_info = get_cats_info('university-python/goit-pycore-hw-04/hw2/cats.txt')
print(cats_info)

cats_info = get_cats_info('university-python/goit-pycore-hw-04/hw2/cats1.txt')
print(cats_info)

cats_info = get_cats_info('university-python/goit-pycore-hw-04/hw2/cats2.txt')
print(cats_info)