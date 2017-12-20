from django import forms
from django.utils.translation import ugettext as _

from meupet import models


# def _build_choice_field(label, choices=None, required=False):
#     empty_choice = (('', '------------'),)
#     field = forms.ChoiceField(
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         choices=empty_choice,
#         label=label,
#         required=required
#     )
#     if choices:
#         field.choices += choices
#     return field


class SongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        kwargs['initial'] = initial
        super(SongForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Song
        fields = ('name', 'group', 'description',
                  'owner',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Выхода нет')}),
            'group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Сплин')}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': _(
                                                     "Скоро рассвет, "
                                                     "Выхода нет. "
                                                     "Ключ поверни...")}),
        }


    def clean_name(self):
        return self.cleaned_data['name'].title()


class SearchForm(forms.Form):
    # name = _build_choice_field(_('Name'), models.Song.name)
    # group = _build_choice_field(_('Group'), models.Song.group)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(SearchForm, self).clean()

        if not any([cleaned_data['name'],\
                    cleaned_data['group']]):
            raise forms.ValidationError(_('You must select at least one filter'))
