from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from trafficelearner import settings
from wsite import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('trial-starter/', views.trial_exam_starter, name="trial_exam_starter"),
    path('trial-exam/', views.trial_exam, name="trial_exam"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('website-information/', views.site_info, name="site_info"),

    path('packages/', views.packages, name="packages"),
    path('package/<int:package_id>/update/', views.update_package, name="update_package"),

    path('questions/part-1/', views.add_question_part_1, name="questions_part_1"),
    path('edit/question/<int:q_id>/part-1/', views.update_question_part_1, name="edit_questions_part_1"),

    path('questions/part-2/', views.add_question_part_2, name="questions_part_2"),
    path('edit/question/<int:q_id>/part-2/', views.update_question_part_2, name="edit_questions_part_2"),

    path('questions/part-3/', views.add_question_part_3, name="questions_part_3"),
    path('edit/question/<int:q_id>/part-3/', views.update_question_part_3, name="edit_questions_part_3"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)