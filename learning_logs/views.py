from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("-date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def check_topic_owner(topic, user):
    """Check if the topic owner is the requested user."""
    if topic.owner != user:
        raise PermissionDenied("You don't have permission to access this topic.")


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request.user)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def new_topic(request):
    """Add a new topic."""
    if request.method == "POST":
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            messages.success(request, "New topic added successfully!")
            return HttpResponseRedirect(reverse("learning_logs:topics"))
    else:
        form = TopicForm()

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def new_entry(request, topic_id):
    """Add new entry to certain topic."""
    topic = get_object_or_404(Topic, pk=topic_id)
    check_topic_owner(topic, request.user)

    if request.method == "POST":
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            messages.success(request, "New entry added successfully!")
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
    else:
        form = EntryForm()

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def edit_entry(request, entry_id):
    """Edit Entry."""
    entry = get_object_or_404(Entry, pk=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request.user)

    if request.method == "POST":
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Entry updated successfully!")
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
    else:
        form = EntryForm(instance=entry)

    context = {"topic": topic, "entry": entry, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


@login_required
@require_http_methods(["POST"])
def delete_entry(request, entry_id):
    """Delete Entry from the learning log."""
    entry = get_object_or_404(Entry, pk=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request.user)
    entry.delete()
    messages.success(request, "Entry deleted successfully!")
    return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))


@login_required
@require_http_methods(["POST"])
def delete_topic(request, topic_id):
    """Delete Topic from the learning log."""
    topic = get_object_or_404(Topic, pk=topic_id)
    check_topic_owner(topic, request.user)
    topic.delete()
    messages.success(request, "Topic and all its entries deleted successfully!")
    return HttpResponseRedirect(reverse("learning_logs:topics"))
