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

    def __repr__(self):
        return f'Board(name={self.name})'


class Todo(ModelBaseUUID):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Todo(title={self.title}, board={self.board.id})'