from django import forms

from blog.models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'slug', 'content', 'image']
        exclude = []

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be 3 characters or more')

        return title  # if you forget this you will get no title back and the form will error

    def save(self, commit=True, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.save()

        return obj


class TestForm(forms.Form):
    SOME_CHOICES = (
        ('db-value', 'display value'),
        ('db-value', 'display value 2'),
    )

    YEARS = [x for x in range(1980, 2021)]
    text_widget = forms.Textarea(attrs={"rows": 4, "cols": 10})
    select_widget = forms.Select(choices=SOME_CHOICES)

    date_field = forms.DateField(initial="2010-01-01", widget=forms.SelectDateWidget(years=YEARS))
    q = forms.CharField(label='search text', widget=text_widget)
    choices = forms.CharField(label='Text', widget=select_widget)
    q2 = forms.BooleanField(label='bool')
    q3 = forms.IntegerField(label='number', initial=10)
    q4 = forms.EmailField(label='email', min_length=5)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

    def clean_q(self, *args, **kwargs):
        text = self.cleaned_data.get("q")
        if len(text) < 10:
            raise forms.ValidationError('Needs more text')

        return text

    def clean_q3(self, *args, **kwargs):
        integer = self.cleaned_data.get("q3")
        if integer < 10:
            raise forms.ValidationError('The integer must be greater than 10')

        return integer


