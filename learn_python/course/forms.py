import django.forms
import course.models


class CourseAdminForm(django.forms.ModelForm):
    introduction = django.forms.CharField(
        widget=django.forms.Textarea(attrs={'id': 'richtext_field'}),
    )
    
    class Meta:
        model = course.models.Course
        fields = '__all__'


class LessonAdminForm(django.forms.ModelForm):
    theory = django.forms.CharField(
        widget=django.forms.Textarea(attrs={'id': 'richtext_field'}),
    )
    
    class Meta:
        model = course.models.Lesson
        fields = '__all__'


class TaskAdminForm(django.forms.ModelForm):
    text = django.forms.CharField(
        widget=django.forms.Textarea(attrs={'id': 'richtext_field'}),
    )
    
    class Meta:
        model = course.models.Task
        fields = '__all__'
