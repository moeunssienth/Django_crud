from django import forms
from .models import Test



class Employeeform(forms.ModelForm):
  

    class Meta:
     model=Test
     fields = ['fullname', 'emp_code', 'mobile', 'position']
     labels = {
         'fullname': 'Full Name',
         'emp_code': 'Employee Code',
         'mobile': 'Mobile Number',
         'position': 'Position'
     }

     def __init__(self, *args, **kwargs):
            super(Employeeform, self).__init__(*args, **kwargs)
          
            self.fields['emp_code'].emty_label = 'Select Employee Code'
            self.fields['position'].required = False