from django.urls import path
from .views import NewsList, NewDetail, NewsCreate, NewsUpdate, PostDelete, SearchList

# from django.contrib.auth.decorators import login_required

urlpatterns = [

   path('', NewsList.as_view(), name='post_list'),

   path('<int:pk>', NewDetail.as_view(), name='post_detail'),
   
   path('search/', SearchList.as_view(), name='post_search'),
   

   path('create/', NewsCreate.as_view(), name='create_news'),
   # path('create/', login_required(NewsCreate.as_view()), name='create_news'),

   path('<int:pk>/update/', NewsUpdate.as_view(), name='update_news'),
   # path('<int:pk>/update/', login_required(NewsUpdate.as_view()), name='update_news'),

   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   # path('<int:pk>/delete/', login_required(PostDelete.as_view()), name='post_delete'),

]