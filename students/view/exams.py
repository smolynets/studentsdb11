from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.student import Student
from ..models.group import Group
from ..models.exam import Exam
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from datetime import datetime
def exams_list(request):
   exams = Exam.objects.all()
   # try to order students list
   order_by = request.GET.get('order_by', '')
   if order_by in ('title', 'group', 'date', '#'):
     exams = exams.order_by(order_by)
     if request.GET.get('reverse', '') == '1':
       exams = exams.reverse()
   # paginate students
   paginator = Paginator(exams, 10)
   page = request.GET.get('page')
   try:
     exams = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     exams = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     exams = paginator.page(paginator.num_pages)
   return render(request, 'students/exams.html',
     {'exams': exams})



def exam_add(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for student object
      data = {}
      # validate user input
      title = request.POST.get('title', '').strip()
      if not title:
        errors['title'] = _(u"Name is mandatory")
      else:
        data['title'] = title
      group = request.POST.get('group', '').strip()
      if not group:
        errors['group'] = _(u"Group is mandatory!")
      else:
        data['group'] = Group.objects.get(pk=group)
      date = request.POST.get('date', '').strip()
      if not date:
        errors['date'] = u"Date is mandatory"
      else:
        try:
          datetime.strptime(date, '%Y-%m-%d')
        except Exception:
          errors['date'] = _(u"Enter the correct date format (eg. 1986-03-23)")
        else:
          data['date'] = date
      
           
      # save exam
      if not errors:
        exam = Exam(**data)
        exam.save()
        # redirect to students list
        return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('exams'), _(u"Exam successfully added")))
      else:
        # render form with errors and previous user input
        return render(request, 'students/exam_add.html',
        {'groups': Group.objects.all().order_by('title'),'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=%s' % (reverse('exams'), _(u"Adding Students canceled")))
  else:
   # initial form render
   return render(request, 'students/exam_add.html',
   {'groups': Group.objects.all().order_by('title')})





  







def exam_edit(request, pk):
    exams = Exam.objects.filter(pk=pk)
    groups = Group.objects.all()

    
    if request.method == "POST":
        data = Exam.objects.get(pk=pk)
        if request.POST.get('add_button') is not None:
            
            errors = {}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = _(u"Name is mandatory.")
            else:
                data.title = title

            group = request.POST.get('group', '').strip()
            if not group:
                errors['group'] = _(u"Group is mandatory!")
            else:
                data.group = Group.objects.get(pk=group)

            date = request.POST.get('date', '').strip()
            if not date:
                errors['date'] = _(u"Birthday is mandatory.")
            else:
                
                data.date = date
           
            
            if errors:
                return render(request, 'students/exam_edit.html', {'pk': pk, 'exam': data, 'errors': errors, 'groups': groups})
            else:
                data.save()
                return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('exams'), _(u'editing of exam finished')))
        elif request.POST.get('cancel_button') is not None:

            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('main'), _(u'editing of exam canceled')))
        
    else:
        return render(request,
                      'students/exam_edit.html',
                      {'pk': pk, 'exam': exams[0], 'groups': groups})
                      
                      
                      
def exam_delete(request, pk):
    exams = Exam.objects.filter(pk=pk)
    
    if request.method == "POST":
        if request.POST.get('yes') is not None:
          exams.delete()
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('exams'), _(u'Exam deleted succefully')))
        elif request.POST.get('cancel_button') is not None:
          return HttpResponseRedirect( u'%s?status_message=%s'  % (reverse('exams'), _(u'Deleting of exam canceled')))
      
    else:
        return render(request,
                      'students/exam_delete.html',
                      {'pk': pk, 'exam': exams[0]})

