from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import Category, Course, LikeCourse, video, Comment


# Create your views here.

def home(request):
    title = "Home"
    print('hello world')
    courses = Course.objects.all().order_by('-likes')
    recently_added_courses = Course.objects.all().order_by('-date_created')[:4]
    print(recently_added_courses.count())
    return render(request, 'app1/index.html', {'courses': courses, 'title': title, 'recentcourses': recently_added_courses})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'app1/category.html', {'categories': categories, 'title': "Categories"})


def categoryview(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    courses = Course.objects.filter(category=category)
    return render(request, 'app1/catview.html', {'courses': courses, 'title': "Categories"})


@login_required(login_url='login')
def courseview(request, slug):
    like_status = "Like"
    course = Course.objects.get(slug=slug)
    print("likes", course.likes.all().count())
    likes = course.likes.all().count()
    if request.user in course.likes.all():
        print('user present')
        like_status = "Liked"
    else:
        print('user not present')
    num = course.num_of_vids
    print('num', num)
    vids_list = []

    for i in range(num):
        print('i', i)
        print('num', num)
        try:
            vid = video.objects.get(course=course, num=i)
            print(vid.title)
            vids_list.append(vid)
        except Exception as e:
            print(e)
    comment_form = CommentForm()
    return render(request, 'app1/course.html',
                  {'course': course, 'likes': likes, 'like_status': like_status, 'vids': vids_list,
                   'comment_form': comment_form, 'title': course.name})

@login_required(login_url='login')
def likecourse(request, slug):
    course = Course.objects.get(slug=slug)
    user = User.objects.get(id=request.user.id)
    status = ""
    try:
        print('try block')
        obj = LikeCourse.objects.get(course=course, user=user)
        if obj:
            print(obj.value)
            if obj.value == 0:
                print('Currently not liked')
                obj.value = 1
                obj.save()
                print('now liked')
                course.likes.add(user)
                status = "liked"
            else:
                obj.value = 0
                print(obj.value)
                obj.save()
                print('Unliked')
                course.likes.remove(user)
                status = "unliked"
    except Exception as e:
        print(e)
        obj = LikeCourse.objects.create(course=course, user=user, value=1)
        print('added to table')
        print('liked')
    data = {'status': status}
    return redirect('courseview', slug=slug)
