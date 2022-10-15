from django import forms
from .models import Memo,Comment
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }

CHOICE_FIELD_RECODE_NUMBERS = (
('10', '10件'),
('15', '15件'),
('30', '30件'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}),
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

CHOICE_FIELD_ORDER_NUMBERS = (
('new', '新着順'),
('old', '古い順'),
)

class OrederNumberForm(forms.Form):
    order_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}),
        choices=CHOICE_FIELD_ORDER_NUMBERS
    )

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea
        }
