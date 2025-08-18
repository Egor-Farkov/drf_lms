import django_filters

from lms.models import Lessons, Courses
from users.models import Pay


class PayFilter(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(
        field_name='lessons',
        queryset=Lessons.objects.all(), label='урок'
    )
    lesson = django_filters.ModelChoiceFilter(
        field_name='Course',
        queryset=Courses.objects.all(), label='курс'
    )
    choose_pay = django_filters.ChoiceFilter(field_name='choose_pay', choices=Pay.TYPE_PAY, label='вид оплаты')

    class Meta:
        model = Pay
        fields = ['course', 'lesson', 'choose_pay']
