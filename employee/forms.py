from django import forms 
from .models  import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_id', 'employee_name', 'employee_email', 'employee_contact')
        # widgets = {
            
        #     'employee_id': forms.TextInput(attrs={
        #          'class': 'form-control',
        #          'placeholder':'Employee ID'

        #     }),
        #      'employee_name': forms.TextInput(attrs={
        #          'class': 'form-control',
        #          'placeholder': 'Employee Name'

        #     } ),
        #     'employee_email': forms.EmailInput(attrs={
        #          'class': 'form-control',
        #          'placeholder': 'Employee Email'

        #     } ),
        #      'employee_contact': forms.TextInput(attrs={
        #          'class': 'form-control',
        #          'placeholder': 'Employee Contact'

        #     } ),
        