import os
import re
import ujson

def replace_links(tweet_string):
	try:
		links = re.findall("(?P<url>https?://[^\s]+)", tweet_string)
		for link in links:
			tweet_string = tweet_string.replace(link, "")
		return tweet_string
	except AttributeError:
		pass

def strip(input_file, output_file):
	with open(input_file) as infile, open(output_file, 'a+') as outfile:
		for line in infile:
			if not line.strip():
				continue
			try:
				tweet = ujson.loads(str(line), )
			except ValueError:
				continue
			try:
				tweet = tweet["text"]
				if (tweet[0:3]) != "RT ": 
					tweet = re.sub(r'\n', ' ', tweet)
					tweet = re.sub(r'  ', ' ', tweet)
					tweet = replace_links(tweet)
					tweet = tweet.encode('utf-8')
					outfile.write(str(tweet) +"\n")
			except KeyError:
				continue
			continue
	infile.close()
	outfile.close()
	return

def only_files(path):
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			yield file
#DATA IDR:
#
input_dir='/home/my/Desktop/B'
def main():
	os.chdir(input_dir)
	for counter, dirname in enumerate(os.listdir('.')):
		print(counter)
		subdir = os.getcwd()+'/'+dirname
		os.chdir(subdir)
		for file in only_files(subdir):
			strip(file, 'stripped_' + str(dirname) + '.txt')
		os.chdir(input_dir)
		
main()