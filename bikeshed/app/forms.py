# coding=utf-8
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Field
from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import Bike


class BikeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BikeForm, self).__init__(*args, **kwargs)

        # add image to the model
        if 'image' in self.files:
            self.instance.setImage(self.files['image'])

        image_preview_path = static('images/no-preview-available.png')

        self.fields['image'].label = 'Upload an image'

        # create layout of the form
        self.helper = FormHelper(self)
        self.helper.form_id = 'add-bike-form'
        self.form_tag = False
        self.helper.form_class = 'form-horizontal'

        self.helper.layout = Layout(
            Div(
                Div(
                    Field('brand'),
                    Field('model'),
                    Div(
                        Div(
                            Field('price'),
                            css_class='col-md-6'
                        ),
                        Div(
                            Field('size'),
                            css_class='col-md-6'
                        ),
                        css_class='row'
                    ),
                    Field('type'),
                    Field('headline'),
                    Field('description')
                    , css_class='col-md-8'),
                Div(
                    HTML(
                        '<img id="preview_image" src="%s" class="img-responsive" alt="your image" />' % (
                            image_preview_path)
                    ),
                    Div(Field('image', help_text="Upload an image"), css_class='fileUpload btn btn-primary'),
                    css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                css_class="error-messages"
            ),
            Div(
                Submit('Submit', 'Submit')
            )

        )

    class Meta:
        model = Bike
        fields = ['brand', 'model', 'price', 'size', 'type', 'headline', 'description', 'image']
