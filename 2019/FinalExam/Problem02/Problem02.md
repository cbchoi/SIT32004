Problem02: Course Management Program
=============
## 2.1 Following program load three raw data and creates CSV file. 
## Complete the code.

* Assumptions
  * Each file contains the information of a student. 
  * Each line of the file is the students
* Note that the raw data is corrupted. Therefore, you should cleanse the data. 
  * To cleanse data, you should remove the incomplete data. 

```python

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

```

## 2.2 Use 'time_fn' decorator to measure the time consumption of each methods.

```python
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.perf_counter()
        result = fn(*args, **kwargs)
        t2 = time.perf_counter()
        print("@timefn: {} took {} seconds".format(fn.__name__, t2 - t1))
        return result
    return measure_time
```