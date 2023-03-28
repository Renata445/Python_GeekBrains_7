def print_operation_table(operation, num_rows=6, num_columns=6):
    x = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in x:
        print(*[f"{a:>3}" for a in i])


print_operation_table(lambda x, y: x * y)