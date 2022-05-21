import os
import sys
from Content import Content


def setup_tree(path):
	if os.path.isdir(path) and not os.path.isfile(path):
		path_splitted = path.split("/")
		dir_name = path_splitted[-1] if path_splitted[-1] != "" else path_splitted[-2]
		
		return Content(path, dir_name, 0, "Folder")
	else:
		return "Diretório não encontrado!"
		

path = input("Diretório: ")
ROOT = setup_tree(path)

if isinstance(ROOT, str):
	print(ROOT)
	sys.exit()
	
ROOT.build()
print(ROOT)