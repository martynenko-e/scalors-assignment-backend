import uuid
from django.db import models

# Create your models here.
class ModelBaseUUID(models.Model):
    """
    This is a BaseModel to store any model that uses a UUID as a primary key.
    """
    class Meta:
        abstract = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)



class Board(ModelBaseUUID):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Todo(ModelBaseUUID):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title