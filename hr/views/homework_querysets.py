# Створіть новий Django view під назвою homework_querysets. В цьому view, вам потрібно виконати наступні комбіновані запити:
# Запит 1: Знайдіть усі відділи (Department), у яких є позиції менеджерів, та впорядкуйте їх за назвою відділу в алфавітному порядку.
# Використовуйте filter() і order_by().
# Запит 2: Знайдіть загальну кількість активних позицій (Position). Використовуйте filter() та count().
# Запит 3: Виберіть усі позиції, які є активними або які належать до відділу з назвою "HR". Використовуйте filter() і OR (|).
# Запит 4: Виберіть назви всіх відділів (Department), в яких є менеджери. Використовуйте filter() та values().
# Запит 5: Виберіть усі позиції, відсортовані за назвою, але виводьте лише назву та інформацію про активність.
# Використовуйте order_by() і values().


from django.db.models import Count
from django.http import HttpResponse
from hr.models import Department, Position, Employee


def homework_querysets(request):
    manager_dep = Department.objects.filter(position__is_manager=True).order_by('name')

    active_count3 = Position.objects.filter(employee__is_active=True).count()

    positions_select = Position.objects.filter(is_active=True) | Position.objects.filter(department__name='HR')

    manager_value = Department.objects.filter(position__is_manager=True).values('name')

    soreted = Position.objects.order_by('title').values('title', 'is_active')

    text = "1. Departments with managers:\n"
    text += "\n".join([f"{e.name}" for e in manager_dep])

    text += "\n\n 2. Overall q-ty of active positions:"
    text += f"{active_count3}"

    text += "\n\n 3. All active or HR positions:\n"
    text += "\n".join([f"{e.title}" for e in positions_select])

    text += "\n\n 4. All departments with managers:\n"
    text += f"{manager_value}"

    text += "\n\n 5. All positions:\n"
    text += f"{soreted}"

    return HttpResponse(text, content_type="text/plain")


# Питання, в чому різниця:
    # active_count = Employee.objects.filter(is_active=True).aggregate(num_active=Count('position'))
    # active_count2 = Position.objects.filter(employee__is_active=True).aggregate(num_active=Count('title'))





