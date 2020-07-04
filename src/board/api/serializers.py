from rest_framework import serializers
from ..models import Todo, Board


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(required=False)
    class Meta:
        fields = (
            'id',
            'url',
            'title',
            'created',
            'updated',
            'done'
        )
        model = Todo


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    todo_count = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'url',
            'name',
            'todo_count'
        )
        model = Board

    def get_todo_count(self, obj):
        return obj.todos.count()


class BoardDetailSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'todos'
        )
        model = Board

    def create(self, validated_data):
        """
        Create and return an existing `Board` instance, given the validated data.
        """
        todos_data = validated_data.pop('todos')
        board = Board.objects.create(**validated_data)
        for todo_data in todos_data:
            Todo.objects.create(board=board, **todo_data)
        return board
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Board` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        todos_data = validated_data.pop('todos', [])
        for todo_data in todos_data:
            if 'id' in todo_data:
                Todo.objects.filter(id=todo_data['id']).update(**todo_data)
            else:
                todo_data['board'] = instance
                Todo.objects.create(**todo_data)
        return instance