import web
import db

urls = (
#things for display
'/','Index',
'/vulnerability/','Vulnerability',
'/protocol/','Protocol',
'/malware/','Malware',
'/search/','Search',
'/about/','About',
#things for user
'/user/login','User_Login',
'/user/view','User_View',
'/user/edit','User_Edit',
'/user/submit','User_Submit',
'/user/add','User_Add',
'/user/delete','User_Delete',
'/user/post_new','User_Post',
#things for admin
'/admin/login','Admin_Login',
'/admin/manage','Admin_Manage'
)

app = web.application(urls,globals())
render = web.template.render('templates/')

class Index:
	def GET(self):
		profile=['admin','haha']
		#v_data = db.get_v_title(2,1)
		v_data = db.get_title('v',2,1)
		p_data = db.get_title('p',2,1)
		m_data = db.get_title('m',2,1)
		#p_data = db.get_p_title(2,1)
		#m_data = db.get_m_title(2,1)	
		header = render.header()
		return render.index(header,profile,v_data,p_data,m_data)

class About:
	def GET(self):
		name='123'
		header = render.header()
		return render.about(header,name)
		
class Vulnerability:
	def GET(self):
		name='Vulnerability Analysis Reports'
		type = 'vulnerability'
		get_data = web.input(pageid=None)
		if get_data.pageid == None:
			page_id = 0
		else:
			page_id = int(get_data.pageid.encode("ascii"))
		v_data = db.get_title('v',2,page_id)
		header = render.header()
		return render.view(header,name,type,v_data,page_id)
		
class Protocol:
	def GET(self):
		pageid = web.input(pageid=None)
		name='Protocol Analysis Reports'
		type = 'protocol'
		get_data = web.input(pageid=None)
		if get_data.pageid == None:
			page_id = 0
		else:
			page_id = int(get_data.pageid.encode("ascii"))
		p_data  = db.get_title('p',2,page_id)
		header = render.header()
		return render.view(header,name,type,p_data,page_id)
		
class Malware:
	def GET(self):
		name = 'Malware Analysis Reports'
		type = 'malware'
		get_data = web.input(pageid=None)
		if get_data.pageid == None:
			page_id = 0
		else:
			page_id = int(get_data.pageid.encode("ascii"))
		m_data = db.get_title('m',2,page_id)
		header = render.header()
		return render.view(header,name,type,m_data,page_id)
		
class Search:
	def GET(self):
		name=None
		header = render.header()
		return render.search(header,name)

class User_Post:
	def GET(self):
		name=None		
		return render.user_post_new(name)


if __name__ == "__main__": 
	app.run()
