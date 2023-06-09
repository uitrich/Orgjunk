import os
import sys
import time
import random
import shutil

from difflib import SequenceMatcher
from pathlib import Path

os.chdir(sys.argv[1])

DIRECTORIES = {
	"HTML": [".html5", ".html", ".htm", ".xhtml"],
	"Javascript": [".js"],
	"Css": [".css"],

	"Pictures": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
				 ".heif", ".psd", ".ico", ".webp", ".avif", ".apng"],
	"Text": [".txt"],
	"Simulated Enviroments": [".ova"],
	"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
	"Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
				  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
				  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
				  ".pptx", ".onepgk", ".csv"],
	"PDF": [".pdf"],

	"Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				 ".dmg", ".rar", ".xar", ".zip"],

	"Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],

	"UML": [".drawio", ".umlet", ".uxf", ".xml"],

	"SQL": [".sql", ".backup"],

	"Java executable": [".jar"],

	"Applications": [".exe", ".msi"],

	"Shell": [".sh", ".bat"],

	"Rainmeterskins": [".rmskin"],

	"Calendar": [".ics"],

	"Final Fantasy": [".ttmp", ".ttmp2", ".pmp", ".dds"],

	"Cheat Engine": [".ct"],

	"Folders": [".unobtainable"]
}

CONSOLE_LOG = {
	"Cheat Engine": 0,
	"Final Fantasy": 0,
	"Text": 0,
	"Simulated Enviroments": 0,
	"java exec": 0,
	"SQL": 0,
	"PDF": 0,
	"UML": 0,
	"HTML": 0,
	"Javascript": 0,
	"Css": 0,
	"Pictures": 0,
	"Videos": 0,
	"Documents": 0,
	"Archives": 0,
	"Audio": 0,
	"Applications": 0,
	"Shell": 0,
	"Rainmeterskins": 0,
	"Calendar": 0,
	"Folders": 0
}

FILE_FORMATS = {file_format: directory
				for directory, file_formats in DIRECTORIES.items()
				for file_format in file_formats}


def recursive_rename(file_pathy, directory_pathy, i):
	try:
		file_pathy.rename(directory_pathy.joinpath(file_pathy))
	except:
		filepaths = file_pathy.suffix
		filepathr = str(file_pathy).replace(filepaths, "")
		filepathr = filepathr + "(" + str(i) + ")" + filepaths
		os.rename(file_pathy, filepathr)
		file_pathy = Path(filepathr)
		recursive_rename(file_pathy, directory_pathy, i + 1)


def organize_junk():
	for entry in os.scandir():

		if entry.is_dir():
			if entry.name in DIRECTORIES.keys():
				continue
			if sys.argv[2] == "foldersort":
				folder_dir = Path("Folders")
				folder_dir.mkdir(exist_ok=True)
				try:
					shutil.move(entry.name, "Folders")
					CONSOLE_LOG["Folders"] = CONSOLE_LOG["Folders"] + 1
					os.rmdir(entry.name)
					print("Folder Found")
				except:
					pass
		file_path = Path(entry)
		file_format = file_path.suffix.lower()
		if file_format in FILE_FORMATS:
			directory_path = Path(FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok=True)
			recursive_rename(file_path, directory_path, 0)
			CONSOLE_LOG[str(directory_path)] = CONSOLE_LOG[str(directory_path)] + 1
		for dir in os.scandir():
			try:
				if dir.name in DIRECTORIES.keys():
					os.rmdir(dir)
			except:
				pass
	for t_type in CONSOLE_LOG:
		if CONSOLE_LOG[t_type] > 0: print(t_type, CONSOLE_LOG[t_type])
	return CONSOLE_LOG

if __name__ == "__main__":
	organize_junk()
