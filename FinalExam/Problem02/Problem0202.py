def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.perf_counter()
        result = fn(*args, **kwargs)
        t2 = time.perf_counter()
        print("@timefn: {} took {} seconds".format(fn.__name__, t2 - t1))
        return result
    return measure_time
    
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
cms = CourseManagementSystem('cms.csv')

# call create_csv()
