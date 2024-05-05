from django.contrib import admin
from .models import DefinedFile, Challenge, Level
from .forms import DefinedFileAdminForm


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_filter = ('published',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'challenge_name')
    list_filter = ('challenge__name',)

    def challenge_name(self, obj):
        return obj.challenge.name

class DefinedFileAdmin(admin.ModelAdmin):
    form = DefinedFileAdminForm
    list_display = ('name', 'level_name', 'challenge_name')
    list_filter = ('level__name', 'level__challenge__name')

    def level_name(self, obj):
        return obj.level.name

    def challenge_name(self, obj):
        return obj.level.challenge.name
    
    # Optionally, add short descriptions for these methods
    level_name.short_description = 'Level Name'
    challenge_name.short_description = 'Challenge Name'

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(DefinedFile, DefinedFileAdmin)
