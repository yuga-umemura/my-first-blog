from django import forms

from .models impotr Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)
		