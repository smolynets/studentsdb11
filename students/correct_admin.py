from django.utils.translation import ugettext as _
from .models.group import Group
from .models.exam import Exam
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.core.urlresolvers import reverse


#student
class StudentFormAdmin(ModelForm):

    def clean_student_group_id(self):
        """Check if student is leader in any group.

        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group_id'] != groups[0].id:
            raise ValidationError(_(u'Student is leader of other group.'),
                code='invalid')

        return self.cleaned_data['student_group_id']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group_id']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group_id']
    ordering = ['last_name']
    list_filter = ['student_group_id']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket',
        'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})



#group
class GroupAdmin(admin.ModelAdmin):
  list_display = ['title', 'leader']
  list_display_links = ['title', 'leader']
  ordering = ['title']
  list_filter = ['title']
  list_per_page = 5
  search_fields = ['title', 'leader']
  def view_on_site(self, obj):
    return reverse('groups_edit', kwargs={'pk': obj.id})




#exam
class ExamAdmin(admin.ModelAdmin):
  list_display = ['title', 'group']
  list_display_links = ['title', 'group']
  ordering = ['title']
  list_filter = ['title']
  list_per_page = 5
  search_fields = ['title', 'leader']
  def view_on_site(self, obj):
    return reverse('exam_edit', kwargs={'pk': obj.id})
