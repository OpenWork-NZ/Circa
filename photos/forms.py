from django import forms

class UploadPhotoForm(forms.Form):
    username = forms.CharField(max_length = 400,
                                help_text = "Log in to upload photo.")
    password = forms.CharField(max_length = 400, widget = forms.PasswordInput)
    title = forms.CharField(max_length = 400)
    link = forms.URLField()
    description = forms.CharField(widget = forms.Textarea)
