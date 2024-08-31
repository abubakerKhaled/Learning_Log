"""Define URL patterns for learning_logs app."""

from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    
    # Detail view for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Add a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Add a new entry to a topic.
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    
    # Edit an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    # Delete an entry.
    # path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    
    # Delete a topic.
    # path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]
