# from django import forms
# from .models import Club, Hall_of_Fame, Event, Resources

# class ClubForm(forms.ModelForm):
#     class Meta:
#         model = Club
#         fields = ['name', 'description']

# class HallOfFameForm(forms.ModelForm):
#     class Meta:
#         model = Hall_of_Fame
#         fields = ['name', 'year']

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'date', 'venue']

# class ResourcesForm(forms.ModelForm):
#     class Meta:
#         model = Resources
#         fields = ['name', 'file', 'description']
from django import forms
from .forms import *
from .models import Club, Hall_of_Fame, Event, Resources,Job

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description','head']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClubForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['added_by'].initial = self.user

class HallOfFameForm(forms.ModelForm):
    class Meta:
        model = Hall_of_Fame
        fields = ['name', 'year','designation','company','contact','pic']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HallOfFameForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['added_by'].initial = self.user

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue','desc']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['added_by'].initial = self.user

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'date','venue']
#         widgets = {
#             'date': forms.DateInput(attrs={'class': 'datepicker'}),
#         }

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super(EventForm, self).__init__(*args, **kwargs)
#         if self.user:
#             self.fields['added_by'].initial = self.user

class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ['name', 'file', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ResourcesForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['added_by'].initial = self.user

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company','location','experience','date_added']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(JobForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['added_by'].initial = self.user