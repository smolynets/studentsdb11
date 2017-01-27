from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _



def paginate(objects, size, request, context, var_name='object_list'):
    """Paginate objects provided by view.
    This function takes:
    * list of elements;
    * number of objects per page;
    * request object to get url parameters from;
    * context to set new variables into;
    * var_name - variable name for list of objects.
    It returns updated context object.
    """
    # apply pagination
    paginator = Paginator(objects, size)
    # try to get page number from request
    page = request.GET.get('page', '1')
    try:
       object_list = paginator.page(page)
    except PageNotAnInteger:
       # if page is not an integer, deliver first page
       object_list = paginator.page(1)
    except EmptyPage:
       # if page is out of range (e.g. 9999),
       # deliver last page of results
       object_list = paginator.page(paginator.num_pages)
    # set variables into context
    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator
    return context



def get_groups(request):
  from models.group import Group
  cur_group = get_current_group(request)

  groups = []
  for group in Group.objects.all().order_by('title'):
    groups.append({
      'id': group.id,
      'title': group.title,
      'leader': group.leader and (u'%s %s' %(group.leader.first_name, group.leader.last_name)) or None,
      'selected': cur_group and cur_group.id == group.id and True or False 
      })
  return groups



def get_current_group(request):
  pk = request.COOKIES.get('current_group')

  if pk:
    from models.group import Group
    try:
      group = Group.objects.get(pk=int(pk))
    except Group.DoesNotExist:
      return None
    else:
      return group
  else:
    return None





def get_lang(request):
  if request.COOKIES.get('django_language') == 'en':
     pk = 'english'
     return pk
  elif request.COOKIES.get('django_language') == 'uk':
     pk = _(u'ukrainian')
     return pk
  else:
     return None

  