from django import forms
from list.models import Item

# class ItemForm(forms.Form):
# 	#Example of a custom form using widgets
# 	# item_text = forms.CharField(
# 	# 	widget=forms.fields.TextInput(attrs={
# 	# 		'placeholder': 'Enter a to-do item',
# 	# 		'class':'form-control input-lg',
# 	# 		}))
EMPTY_LIST_ERROR = "You can't have an empty list item"

	
class ItemForm(forms.models.ModelForm):

	class Meta:
		model = Item
		fields = ('text',)
		widgets = {
			'text':forms.fields.TextInput(attrs={
				'placeholder': 'Enter a to-do item',
				'class': 'form-control input-lg',
				}),
		}
		error_messages = {
			'text': {'required': EMPTY_LIST_ERROR}
		}