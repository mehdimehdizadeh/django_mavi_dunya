from django.urls import path
from article import views
from django.conf.urls import url

app_name = "article"
urlpatterns = [
    path('article/<int:id>',views.detail, name="detail"),
    path('category/<int:id>',views.category, name="category"),
    path('comment/<int:id>',views.addComment, name="comment"),
]