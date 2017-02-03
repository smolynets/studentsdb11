from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.monthjournal import logentry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required




@login_required
def logs(request):
   logs = logentry.objects.order_by('asctime').reverse()
   # paginate logs
   paginator = Paginator(logs, 5)
   page = request.GET.get('page')
   try:
     logs = paginator.page(page)
   except PageNotAnInteger:
   # If page is not an integer, deliver first page.
     logs = paginator.page(1)
   except EmptyPage:
     # If page is out of range (e.g. 9999), deliver
     # last page of results.
     logs = paginator.page(paginator.num_pages)
   return render(request, 'students/logs.html',
     {'logs': logs})