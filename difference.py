import os

dirs = open('dirs.txt');

records = open('records.txt');

same = open('same.txt', 'w');

for line in dirs:
	print(line);
	for string in records:
		print(string);
		if str(string) == str(line):
			same.write(line + '\n');
			print(line);


dirs.close();
records.close();
same.close();