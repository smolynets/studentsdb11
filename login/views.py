from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.models import User




class logForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(logForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

            # return HttpResponseRedirect(
            #     u'%s?status_message=5' %  reverse('exam'))


        # set form tag attributes
        self.helper.form_action = reverse('users:auth_login')
        # self.helper.form_action = u'%s?status_message=5' % reverse('exam_add')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-12 form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8 input-group'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('send_button', _(u'go')))
       