# from socket import fromshare
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.forms import ModelForm

# from catalog.models import BookInstance
from catalog.models import BookInstance  # все работает


# class RenewBookModelForm(ModelForm):
#     def clean_due_back(self):
#         data = self.cleaned_data['due_back']
#
#         # Check if a date is not in the past.
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         # Remember to always return the cleaned data.
#         return data
#
#     class Meta:
#         model = BookInstance
#         fields = ['due_back']
#         labels = {'due_back': _('Renewal date')}
#         help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')
    # required=False    labeal=...
    # initial   widget  help_text   error_messages
    # validators    localize    disabled

    def clean_renewal_date(self):
        # очищенные от потенциально небезопасного ввода с использованием
        #  средств проверки по умолчанию, и преобразуем их в правильный
        # стандартный тип для данных (в данном случае
        # datetime.datetime объект Python).
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
# Приведенный выше пример также переносит этот текст в одну из функций
# перевода Django gettext_lazy()(импортируется как_()), что является
# хорошей практикой, если вы хотите перевести свой сайт позже.
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
