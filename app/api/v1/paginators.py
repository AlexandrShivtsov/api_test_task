from rest_framework.pagination import PageNumberPagination


class TeammatesPaginations(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
    
    
class TeamsPaginations(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
