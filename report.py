import web

urls = (
#things for display
'/','Index',
'/vulnerability','Vulnerab ility',
'/protocol','Protocol',
'/malware','Malware',
'/search','Search',
'/about','About',
#things for user
'/user/login','User_Login',
'/user/view','User_View',
'/user/edit','User_Edit',
'/user/submit','User_Submit',
'/user/add','User_Add',
'/user/delete','User_Delete',
#things for admin
'/admin/login','Admin_Login',
'/admin/manage','Admin_Manage'
)

app = web.application(urls,globals())
render = web.template.render('templates/')

class Index:
	def GET(self):
		name="123"
		return render.index(name)

class About:
	def GET(self):
		name='123'
		return render.about(name)
		
class Vulnerability:
	def GET(self):
		name='Vulnerability Analysis Reports'
		return render.view(name)
		
class Protocol:
	def GET(self):
		name='Protocol Analysis Reports'
		return render.view(name)
		
class Malware:
	def GET(self):
		name = 'Malware Analysis Reports'
		return render.view(name)
		
class Search:
	def GET(self):
		name=None
		return render.search(name)

if __name__ == "__main__": 
	app.run()