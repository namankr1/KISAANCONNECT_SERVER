from . import models
import requests,urllib

def translate(strtobetranslated):
	if strtobetranslated is None:
		return None
	if isinstance(strtobetranslated,unicode):
		strtobetranslated = strtobetranslated.encode('utf8')
	lang = ['en','hi','bn','te','mr','ta','ur','gu','kn','ml','pa','ne','sd']
	f={'q':strtobetranslated}
	p = urllib.urlencode(f)
	val = ""
	for x in lang:
		url = "https://translate.googleapis.com/translate_a/single?client=gtx&ie=UTF-8&sl=auto&tl="+x+"&dt=t&"+p
		y = urlhit(url)
		val = val + ';' + y
	translatedstr = val[1:]
	return translatedstr

def urlhit(url):
	r = requests.get(url)
	p1 = r.text
	p2 = p1.split('"')
	return p2[1]

def getCategories():
    categories = models.Category.objects.all()
    jsonout = []
    for c in categories:
        d={}
        d['id']=c.id
        d['name']=c.name
        d['description']=c.description
        d['picture'] = "pict/" + c.picture.url
        jsonout.append(d)
    return jsonout

def getSubcategories(categoryid):
    categories = models.Category.objects.filter(id=categoryid)
    if len(categories)==0:
        return -1
    subcategories = models.Subcategory.objects.filter(category = categories[0])
    if len(subcategories)==0:
        return -2
    jsonout = []
    for c in subcategories:
        d={}
        d['id']=c.id
        d['name']=c.name
        d['description']=c.description
        d['picture'] = "pict/" + c.picture.url
        jsonout.append(d)
    return jsonout

def addCategories(name,description):
    x = translate(name)
    y = translate(description)
    category = models.Category(name = x, description = y)
    category.save()
    return 1;
def addSubCategories(name,description,categoryid):
	category = models.Category.objects.filter(id=categoryid)
	if len(category)==0:
		return -1
	x = translate (name)
	y = translate (description)
	subcategory = models.Subcategory(name = x, description = y, category = category[0])
	subcategory.save()
	return 1
