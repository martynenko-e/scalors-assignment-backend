from django.contrib import admin
from .models import Board, Todo

class TodoInline(admin.TabularInline):
    model = Todo

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    inlines = [
        TodoInline,
    ]

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'done', 'created', 'updated')