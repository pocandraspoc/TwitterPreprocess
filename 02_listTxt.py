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

def list_tweet_text_files(input_dir='/home/my/Downloads/'):
	list_= []
	os.chdir(input_dir)
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
		os.chdir(input_dir)
	return list_

def main(output_dir='/home/my/Dow_tw/'):
	os.chdir(output_dir)
	for elem in list_tweet_text_files():
		#print(elem)
		os.chdir(output_dir)
		concatenate_file_lines(elem, "conc.txt")
		os.remove(elem)

main()