import os


# reading list of dirs in current directory
dirs = os.listdir(path=".");

# convert list to string
dirs = '\n'.join(dirs);


# saving data to file
handler = open("./dirs.txt","w");
handler.write(dirs);
handler.close();
