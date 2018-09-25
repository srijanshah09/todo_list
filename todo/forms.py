from django import forms
from .models import Todo

# Creating Forms Without Using Models

#class  TodoForm(forms.Form):
#	text = forms.CharField(max_length=40, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter todo e.g. Delete junk files', 'aria-label':'Todo', 'aria-describedby':'add-btn'}))

# Creating Forms Using Models

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo	
		fields = ['text']
		widgets = {
			'text': forms.TextInput(attrs={
				'class':'form-control', 
				'placeholder':'Enter todo e.g. Delete junk files', 
				'aria-label':'Todo', 
				'aria-describedby':'add-btn'		
			})
		}	