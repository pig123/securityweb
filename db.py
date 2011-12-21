import web

#create a connector with mysql
db = web.database(dbn='mysql',db='security_analysis',user='root',pw='')

def get_title(post_type,n,p):
	numberpage = n
	pageid = p
	limit_ = numberpage
	if pageid>=1:
		offset_ = (pageid-1)*numberpage
	else:
		offset_ = 0
	results = db.query('select post_date,post_title,user_nicename from posts left join users on posts.post_author = users.ID where post_type=\''+post_type+'\' limit '+str(limit_)+' offset '+str(offset_) )
	return results

def get_v_title(n,p):
	numberpage = n
	pageid = p
	limit_ = numberpage
	if pageid>=1:
		offset_ = (pageid-1)*numberpage
	else:
		offset_ = 0

	results = db.select('posts',what='post_date,post_title,post_author',where='post_type=\'v\'',limit=limit_,offset=offset_)
	return results

def get_p_title(n,p):
	numberpage = n
	pageid = p
	limit_ = numberpage
	if pageid>=1:
		offset_ = (pageid-1)*numberpage
	else:
		offset_ = 0
	results = db.select('posts',what='post_date,post_title,post_author',where='post_type=\'p\'',limit=limit_,offset=offset_)
	return results

def get_m_title(n,p):
	numberpage = n
	pageid = p
	limit_ = numberpage
	if pageid>=1:
		offset_ = (pageid-1)*numberpage
	else:
		offset_ = 0
	results = db.select('posts',what='post_date,post_title,post_author',where='post_type=\'m\'',limit=limit_,offset=offset_)
	return results


