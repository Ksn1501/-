string = input()
strip_string = string.strip()
number_list = [int(num) for num in strip_string.split()]
even_list = [num for num in number_list if num % 2 == 0]
print(even_list)