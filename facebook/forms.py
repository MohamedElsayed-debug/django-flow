from django import forms

class FacebookPostForm(forms.Form):
    token = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Access Token'})
    )
    img = forms.ImageField(label='' ,required=False)
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Post message'})
    )
