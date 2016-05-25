from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param, None)
        if page_size == '0':
            return None
        else:
            return PageNumberPagination.get_page_size(self, request)
