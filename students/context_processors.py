from .util import get_groups, get_lang, stud
#group select
def groups_processor(request):
	return {'GROUPS': get_groups(request)}



#select language
def lang_processor(request):
	return {'PK': get_lang(request)}


def stud_c(request):
	return {'stud': stud(request)}






	