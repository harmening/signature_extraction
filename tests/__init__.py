import sys, os

def get_signature_extractor_folder_path():
	path = os.path.abspath(__file__)
	dir_path = os.path.dirname(path)

	folders = dir_path.split('/')
	folders.remove('tests')
	folders.append('signature_extractor')
	return os.path.join('/', *folders)

sys.path.append(get_signature_extractor_folder_path())