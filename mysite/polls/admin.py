from django.contrib import admin

from .models import Choice, Question

# Register your models here.


class ChoiceInline(admin.TabularInline):
    # model to inline
    model = Choice
    # initial slots for choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # set order for question fields
    # fields = [
    #     'pub_date',
    #     'question_text'
    # ]

    # By default, Django displays the __str__() of each object.
    # Can set labels, by model fields, for displaying Quesiton objects
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Add field filter options for admins
    list_filter = ['pub_date']

    # Add search options for admins
    """
    You can use as many fields as you’d like – although because it uses a LIKE query behind the scenes,
    limiting the number of search fields to a reasonable number will make it easier for your database to do the search.
    """
    search_fields = ['question_text']

    # limit pagination
    list_per_page = 20

    # set titles, fields, and order for editing Question objects
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # let Question admin pg. edit Choice objects
    inlines = [ChoiceInline]


# tell the admin that Question objects have a specific admin interface.
admin.site.register(Question, QuestionAdmin)
