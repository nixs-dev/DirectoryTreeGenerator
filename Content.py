import os

class Content:
	separator = "__"
	
	def __init__(self, path, name, parent_level, level, type):
		self.path = path
		self.name = name
		self.level = level
		self.parent_level = parent_level
		self.type = type
		self.contents = []
	
	def get_name(self):
		return self.name
	
	def get_parent_level(self):
		return self.parent_level
		
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
	
	def get_tree_repr(self):
		levels_difference = self.get_level() - self.get_parent_level()
		parents_parent = "  " * self.get_parent_level()
		line_start = "|_" if levels_difference > 0 else ""
		line_body =  (Content.separator * (levels_difference-2))
		content_name = self.get_name()
		
		return parents_parent + line_start + line_body + content_name + "\n"
	
	def build(self):
		folders = []
		files = []
		
		try:
			for content in os.listdir(self.path):
				content_path = self.path + "/" + content
				
				if os.path.isdir(content_path):
					new_content = Content(content_path, content, self.get_level(), self.get_level() + 1, "Folder")
					new_content.build()
					print(new_content)
					folders.append(new_content)
				else:
					files.append(Content(content_path, content, self.get_level(), self.get_level() + 1, "File"))
		
			self.set_contents(folders + files)
		except PermissionError:
			pass #IF DIRECTORY ACCESS IS DENIED, JUST IGNORE IT

	def __str__(self):
		tree_str = self.get_tree_repr()
		contents = self.get_contents()
		
		for c in contents:
			if c.get_type() == "Folder":
				tree_str += c.__str__()
			else:
				tree_str += c.get_tree_repr()
		
		return tree_str