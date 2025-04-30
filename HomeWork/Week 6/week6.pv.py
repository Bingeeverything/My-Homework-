start = int(input('Start: '))
stop = int(input('Stop: '))

file = open('table.txt', 'w')
for i in range(start, stop):
    file.write(f'{i:08b} is {i}\n')

file.close()

# Read and display the contents of the file.
table_file_readonly = open('table.txt', 'r')
print(table_file_readonly.read(), end='')
