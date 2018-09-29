import os
from os import walk

def list_files_with_extension(directory, extension):
    for (dirpath, dirnames, filenames) in walk(directory):
        return (f for f in filenames if f.endswith('.' + extension))

def concatenate_file_lines(input_file, output_file):
	with open(input_file) as infile, open(output_file, 'a+') as outfile:
		for line in infile:
			outfile.write(line)
	infile.close()
	outfile.close()

def list_tweet_text_files():
	list_= []
	os.chdir('/home/my/Downloads/')
	for dirname in os.listdir('.'):
		subdir = os.getcwd()+'/'+dirname
		os.chdir(subdir)
		directory = subdir
		#print(directory)
		files = list_files_with_extension(directory, "txt")
		for filename in files:
			full_path = os.path.join(os.getcwd(), filename)
			#print (full_path)
			list_.append(full_path)
		os.chdir('/home/my/Downloads/')
	return list_

def main():
	os.chdir('/home/my/Dow_tw/')
	for elem in list_tweet_text_files():
		#print(elem)
		os.chdir('/home/my/Dow_tw/')
		concatenate_file_lines(elem, "conc.txt")
		os.remove(elem)

main()