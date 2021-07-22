from django import forms
from cofe.models import Category

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': "Название", 'required': "required"}))

    cat_order = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': "Порядок категории в меню",
                                                                          'required': "required"}))


    is_visible = forms.BooleanField(initial=True, required=False)


    class Meta:
        model = Category
        fields = ('title', 'is_visible', 'cat_order')