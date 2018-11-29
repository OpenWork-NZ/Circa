from django import forms

class UploadPhotoForm(forms.Form):
    username = forms.CharField(max_length = 400,
                                help_text = "Log in to upload photo.")
    password = forms.CharField(max_length = 400, widget = forms.PasswordInput)
    title = forms.CharField(max_length = 400)
    link = forms.URLField()
    description = forms.CharField(widget = forms.Textarea)

class ImageRect(forms.HiddenInput):
    """
    Add JavaScript for drawing a div.annotation over an image based on mouse drags,
    and uploading the bounding coordinates.
    Output the image wrapped in a div.annotated-image in order to correctly
    position it.

    Parse the uploaded rect.
    """

class NewGroupForm(forms.Form):
    name = forms.CharField(max_length = 400, required = True)
    description = forms.CharField(widget = forms.Textarea, required = True)
    start_date = forms.DateField(required = False)
    end_date = forms.DateField(required = False)
    reference = forms.URLField(help_text = "Link to justify your dates?", required = False)
    # crop area
