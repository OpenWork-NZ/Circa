from django import forms

class UploadPhotoForm(forms.Form):
    username = forms.CharField(max_length = 400,
                                help_text = "Log in to upload photo.")
    password = forms.CharField(max_length = 400, widget = forms.PasswordInput)
    title = forms.CharField(max_length = 400)
    link = forms.URLField()
    description = forms.CharField(widget = forms.Textarea)

class NewGroupForm(forms.Form):
    name = forms.CharField(max_length = 400, required = True)
    description = forms.CharField(widget = forms.Textarea, required = True)
    start_date = forms.DateField(required = False)
    end_date = forms.DateField(required = False)
    reference = forms.URLField(help_text = "Link to justify your dates?", required = False)
    source_rect = forms.CharField(required = False, help_text="Select by dragging over the image on the left.")
