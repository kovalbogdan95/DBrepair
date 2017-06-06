import os

handler = open('dirs.txt');

counter = 0;

for line in handler:
	counter += 1;

print(counter);