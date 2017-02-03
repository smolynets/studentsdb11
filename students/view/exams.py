from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.exam import Exam
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.student import Student
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from ..util import paginate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




#########################################################################
#exam_list
class ExamList(ListView):
  model = Exam
  context_object_name = 'exams'
  template_name = 'students/exams.html'
  def get_context_data(self, **kwargs):
    """This method adds extra variables to template"""
    # get original context data from parent class
    context = super(ExamList, self).get_context_data(**kwargs)
    # tell template not to show logo on a page
    context['show_logo'] = False
    queryset = Exam.objects.all().order_by('group')
    context = paginate(queryset, 2, self.request, context, var_name='exams')
    # return context mapping
    return context
  def get_queryset(self):
    """Order exams by title."""
    # get original query set
    qs = super(ExamList, self).get_queryset()
    # order by title
    return qs.order_by('title')



##########################################################################

#exam_add
 
#crispy

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(ExamCreateForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

            # return HttpResponseRedirect(
            #     u'%s?status_message=5' %  reverse('exam'))


        # set form tag attributes
        self.helper.form_action = reverse('exam_add')
        # self.helper.form_action = u'%s?status_message=5' % reverse('exam_add')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-12 form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8 input-group'
        self.helper.attrs = {'novalidate': ''}

        # add buttons
        # self.helper.layout.fields.append(self)
        self.helper.layout.fields.append(FormActions(
            Submit('add_button', _(u'save'), css_class="btn btn-primary"),
            Submit('cancel_button', _(u'cancel'), css_class="btn btn-link"),
)) 


class ExamCreate(CreateView):

  model = Exam
  template_name = 'students/exam_add.html'
  form_class = ExamCreateForm
  def get_success_url(self):
    return u'%s?status_message=%s' % (reverse('exams', _(u'Exam created sucefully')))
  def post(self, request, *args, **kwargs):
    if request.POST.get('cancel_button'):
      return HttpResponseRedirect(u'%s?status_message=%s'% (reverse('exams'), _(u'Creation of exam canceled')))
    else:
      return super(ExamCreate, self).post(request, *args, **kwargs)
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(ExamCreate, self).dispatch(*args, **kwargs)
      
         





##################################################################################

#exam_edit

   #crispy
class ExamUpdateForm(ModelForm):
  class Meta:
    model = Exam
  def __init__(self, *args, **kwargs):
      super(ExamUpdateForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper(self)
      # set form tag attributes
      self.helper.form_action = reverse('exam_edit',kwargs={'pk': kwargs['instance'].id})
      self.helper.form_method = 'POST'
      self.helper.form_class = 'form-horizontal'
      # set form field properties
      self.helper.help_text_inline = True
      self.helper.html5_required = True
      self.helper.label_class = 'col-sm-2 control-label'
      self.helper.field_class = 'col-sm-10'
      self.helper.attrs = {'novalidate': ''}
      # add buttons
      self.helper.layout.fields.append(FormActions(
        Submit('add_button', _(u'save'), css_class="btn btn-primary"),
        Submit('cancel_button', _(u'cancel'), css_class="btn btn-primary"),
      ))



class ExamUpdate(UpdateView):
  model = Exam
  template_name = 'students/exam_edit.html'
  form_class = ExamUpdateForm
  def get_success_url(self):
    return u'%s?status_message=%s' % (reverse('exams'), _(u'Exam sucefully edited!'))
  def post(self, request, *args, **kwargs):
    if request.POST.get('cancel_button'):
      return HttpResponseRedirect(u'%s?status_message=%s'% (reverse('exams'), _(u'Editing of exam canceled')))
    else:
      return super(ExamUpdate, self).post(request, *args, **kwargs)
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(ExamUpdate, self).dispatch(*args, **kwargs)



####################################################################################

#exam delete

class ExamDelete(DeleteView):
  model = Exam
  template_name = 'students/exam_delete.html'
  def get_success_url(self):
    return u'%s?status_message=%s' % (reverse('exams'), _(u'Exam deleted sucefully'))
  def post(self, request, *args, **kwargs):
    if request.POST.get('no_delete_button'):
      return HttpResponseRedirect(u'%s?status_message=%s'% (reverse('exams'), _(u'Deleting of exam canceled')))
    else:
      return super(ExamDelete, self).post(request, *args, **kwargs)
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(ExamDelete, self).dispatch(*args, **kwargs)
    
          
      
        
    