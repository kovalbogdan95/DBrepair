import os

handler = open('out.txt');

records = open('records.txt', 'w');


for line in handler:
	lst = line[5:25];
	records.write(lst + '\n');

handler.close();
records.close();