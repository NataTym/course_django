from modeltranslation.translator import TranslationOptions, register

from hr.models import Position, Department, Company


@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('title', 'job_description')

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'parent_department')

