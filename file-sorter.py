# importing the required modules
import os
import shutil
import glob

# change your directory to the one you want sorted
os.chdir('Directory You want sorted')

curr = os.getcwd()

doc = 'Documents'
img = 'Images'
vid = 'Videos'
code = 'Coding'
text = 'Text'
audio = 'Audio'

# making all the folders
os.mkdir('Documents')
os.mkdir('Images')
os.mkdir('Videos')
os.mkdir('Coding')
os.mkdir('Text')
os.mkdir('Audio')

docs = str(os.path.join(curr, doc))
imgs = str(os.path.join(curr, img))
vids = str(os.path.join(curr, vid))
codes = str(os.path.join(curr, code))
texts = str(os.path.join(curr, text))
audios = str(os.path.join(curr, audio))


Directories= {
	docs:[".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
            ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
            ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
            "pptx", ".pdf"],
	imgs:[".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
	audio:[".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
	vids:[".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
	codes:[".py", ".html", ".html5", ".xml",],
	texts:[".txt", ".in", ".out"]
}

for destination, extensions in Directories:
	for ext in extensions:
		for file in glob.glob(curr + '*.' + ext):
			shutil.move(file, destination)

