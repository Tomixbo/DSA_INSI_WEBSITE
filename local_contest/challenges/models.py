from django.db import models
from django.utils.text import slugify
import os

class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('Alpha', 'Alpha'),
        ('Beta', 'Beta'),
        ('Gamma', 'Gamma'),
        ('Omega', 'Omega'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Alpha')
    difficulty = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])  # Level field with choices 1 to 5
    published = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    # Add any other fields for levels as needed
    def upload_to_description_file(instance, filename):
        challenge_slug = instance.challenge.slug
        return f'{challenge_slug}/level_descriptions/{filename}'

    def upload_to_input_file(instance, filename):
        challenge_slug = instance.challenge.slug
        return f'{challenge_slug}/level_input_files/{filename}'
    
    
    description_file = models.FileField(upload_to=upload_to_description_file, null=True, blank=True)
    input_file = models.FileField(upload_to=upload_to_input_file, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='levels')

    

    def __str__(self):
        return self.name


class DefinedFile(models.Model):
    name = models.CharField(max_length=100)

    def upload_to_input_file(instance, filename):
        if instance.level:
            return f"{instance.level.challenge.slug}/level_input_files/{instance.level.name}/{filename}"
        else:
            return "level_input_files/" + filename
    
    def upload_to_output_file(instance, filename):
        if instance.level:
            return f"{instance.level.challenge.slug}/level_output_files/{instance.level.name}/{filename}"
        else:
            return "level_output_files/" + filename

    input_file = models.FileField(upload_to=upload_to_input_file, null=True, blank=True)
    output_file = models.FileField(upload_to=upload_to_output_file, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='defined_files') 
    
    def __str__(self):
        return self.name
    
    def filename(self):
        return os.path.basename(self.input_file.name)