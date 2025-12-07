from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description_bullets = models.JSONField(help_text="List of bullet points describing the role")

    def __str__(self):
        return f"{self.role} at {self.company}"

class Project(models.Model):
    name = models.CharField(max_length=200)
    tech_stack = models.JSONField(help_text="List of technologies used", default=list)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
