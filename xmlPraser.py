# -*- coding: utf-8 -*- 
import os
import re

count = 0;
# open xml file
handler = open('mytetra.xml', 'r', encoding='UTF8');

# open output file
output = open('out.txt', 'w');

for line in handler:
	lst = re.findall('dir="\S+"', line);
	lst = "".join(lst);
	if len(lst) > 0:
		output.write(lst);
		output.write("\n");
		count += 1;

# write number of records
output.write(str(count)+ ' records');

output.close();
handler.close();
