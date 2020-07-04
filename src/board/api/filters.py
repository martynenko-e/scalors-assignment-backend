from rest_framework import filters


class DoneFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.GET.get('done'):
            is_done = request.GET.get('done') not in ['false', 'False', 'no', '0']
            return queryset.filter(done=is_done)
        return queryset