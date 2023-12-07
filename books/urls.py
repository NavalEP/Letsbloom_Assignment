# Book/urls.py


from django.urls import include, path
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'books', views.BookViewSet)

urlpatterns = [
    # path('Book', get_all_books, name='get_all_books'),
    # path('Book/', add_new_books, name='add_new_books'),
    # path('Book/<int:id>', update_books, name='update_books'),
    path('books/', views.booksAPI.as_view()),
    path('books/<int:pk>/', views.booksPUT.as_view())
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns+=router.urls