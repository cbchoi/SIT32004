
class CourseManagementSystem(object):
	def __init__(self, _text, _names, _ids, _departs):
		self.student_list = []
		self.csv_name = _text
		self.name_list = []
		self.id_list = []
		self.depart_list = []
		
		'''
		Initalization	
		
		'''

		pass
	
	def load_names(self, _names):
		pass
	
	def load_ids(self, _ids):
		pass
	
	def load_depart(self, _departs):
		pass
	
	def create_csv(self):
		pass

# Instantiate the CourseManagementSystem class
# When you instantiate the CourseManagementSystem class, 
# the instance must hold the contents
cms = CourseManagementSystem('cms.csv', 'names.txt', 'ids.txt', 'departs.txt')

# call create_csv()
