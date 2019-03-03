from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory

from blog.forms import TestForm, PostModelForm
from blog.models import Post


def home(request):
    intial_text = { # this overrides the intial form data
        "q": "Text",
        "q2": True
    }
    form = TestForm(request.POST or None, initial=intial_text)
    if form.is_valid():
        print(form)
        print(form.cleaned_data)

    return render(request, 'test_form.html', {'form': form})


def blog_post(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'test_form.html', {'form': form})


def formset_view(request):
    TestFormSet = formset_factory(PostModelForm, extra=2)
    formset = TestFormSet(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    context = {
        "formset": formset
    }
    return render(request, "formset.html", context)


def model_formset_view(request):
    fields = ['user', 'title', 'slug', 'image']
    TestFormSet = modelformset_factory(Post, fields=fields, extra=2)  # we use the model here not a form
    formset = TestFormSet(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    context = {
        "formset": formset
    }
    return render(request, "formset.html", context)
