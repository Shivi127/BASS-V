from django import forms
from .models import CourseReview
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.


class CourseReviewCreateForm(forms.Model Form):
    class Meta:
        model = CourseReview
        fields=[
            'comment',
        ]
    # validating data
    def clean_comment(self):
        data = self.cleaned_data.get['comments']
        return data

 # comment = models.CharField(blank=True, null=True)
 #    user = models.ForeignKey(User, default=1)
 #    date = models.DateField(default=date.today)