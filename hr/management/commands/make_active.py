from django.core.management.base import BaseCommand

from hr.models import Employee


#Створіть нову management команду для моделі Employee. Команда повинна робити всіх Employee активними (is_active=True).

class Command(BaseCommand):
    help = "Change status for employees to is_active"

    def handle(self, *args, **kwargs):

        employees = Employee.objects.all()

        for employee in employees:
            if not employee.is_active:
                employee.is_active = True
                employee.save()

        self.stdout.write(
            self.style.SUCCESS('All employees is active now')
        )



