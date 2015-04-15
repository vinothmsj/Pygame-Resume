"""
page 0 :intro
page 1: name and personal details
page 2 : Objective
page 3: current
pgae 4: skills
page 5: projects and internships
page 6: cert and courses
page 7: edu back
page 8 : thank you

"""
import json


# The program starts from here by extracting the data from the json file.
class ReadData:
	def read_file(self):
		json_file = open("Raw_data.txt")
		json_object = json.load(json_file)
		self.name_personal = json_object.get('name','')
		self.objective = json_object.get('objective', '')
		self.GitHub=json_object.get('GitHub','')
		self.current_data = json_object.get('current', '')
		self.skills = json_object.get('skills', '')
		self.cert_cour = json_object.get('cert_cour', '')
		self.edu_back = json_object.get('edu_back', '')

		return self


class GetData:
	def __init__(self):
		self.data = ReadData().read_file()
		

	def __call__(self, page_no):
		if page_no == 1:
			return self.data.name_personal
		elif page_no == 2:
			return self.data.objective
		elif page_no==3:
			return self.data.GitHub
		elif page_no == 4:
			return self.data.current_data
		elif page_no == 5:
			return self.data.skills
		elif page_no == 6:
			return self.data.cert_cour
		elif page_no == 7:
			return self.data.edu_back
		else:
			return None
