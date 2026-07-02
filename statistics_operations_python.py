numbers = [1,2,3,1,2]

def maximum(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num

def minimum(numbers):
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num

def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def average(numbers):
    avg = sum_list(numbers) / len(numbers)
    return avg 

def find_mode(numbers):
    mode = []
    max_count = 0

    for i in numbers:
        count = 0

        for j in numbers:
            if i == j:
                count += 1

        if count > max_count:
            max_count = count
            mode = [i]
        elif count == max_count:
            already_exists = False

            for x in mode:
                if x == i:
                    already_exists = True

            if not already_exists:
                mode.append(i)
    return mode

def median(numbers):
    median = 0
    numbers = sorted(numbers)
    l = numbers[len(numbers) // 2]
    if len(numbers) % 2 == 1:
        median = l
    else:
        m = l - 1
        median = (m + l) / 2
    print(numbers)
    return median

print("Min: ", minimum(numbers))
print("Max: ", maximum(numbers))
print("Sum: ", sum_list(numbers))
print("Avg: ", average(numbers))
print("Mode: ", find_mode(numbers))
print("Median: ", median(numbers))