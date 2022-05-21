import os

class Content:
	separator = "__"
	
	def __init__(self, path, name, level, type):
		self.path = path
		self.name = name
		self.level = level
		self.type = type
		self.contents = []
	
	def get_name(self):
		return self.name
		
	def get_level(self):
		return self.level
	
	def get_type(self):
		return self.type
	
	def get_contents(self):
		return self.contents
	
	def set_contents(self, contents):
		self.contents = contents
	
	def add_content(self, content):
		self.contents.append(content)
	
	def build(self):
		folders = []
		files = []
		
		for content in os.listdir(self.path):
			content_path = self.path + "/" + content
			
			if os.path.isdir(content_path):
				new_content = Content(content_path, content, self.get_level() + 1, "Folder")
				new_content.build()
				folders.append(new_content)
			else:
				files.append(Content(content_path, content, self.get_level() + 1, "File"))
		
		self.set_contents(folders + files)
	
	def __str__(self):
		tree_str = (Content.separator * (self.get_level())) + self.get_name() + "\n"
		contents = self.get_contents()
		
		for c in contents:
			if c.get_type() == "Folder":
				tree_str += c.__str__()
			else:
				tree_str += (Content.separator * (c.get_level())) + c.get_name() + "\n"
		
		return tree_str