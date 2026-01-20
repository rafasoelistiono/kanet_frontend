# import datetime
# from django.http import HttpResponseRedirect, JsonResponse
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http import HttpResponse
# from django.core import serializers
# from django.shortcuts import render, redirect, get_object_or_404
# from main.forms import NewsForm
# from main.models import News
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# from django.utils.html import strip_tags

# Create your views here.

# @login_required(login_url='/login')
# def show_main(request):
#     filter_type = request.GET.get("filter", "all")  # default 'all'

#     if filter_type == "all":
#         news_list = News.objects.all()
#     else:
#         news_list = News.objects.filter(user=request.user)

#     context = {
#         'npm': '240123456',
#         'name': request.user.username,
#         'class': 'PBP A',
#         'news_list': news_list,
#         'last_login': request.COOKIES.get('last_login', 'Never')
#     }
#     return render(request, "main.html", context)

# def create_news(request):
#     form = NewsForm(request.POST or None)

#     if form.is_valid() and request.method == 'POST':
#         news_entry = form.save(commit = False)
#         news_entry.user = request.user
#         news_entry.save()
#         return redirect('main:show_main')

#     context = {
#         'form': form
#     }

#     return render(request, "create_news.html", context)

# @login_required(login_url='/login')
# def show_news(request, id):
#     news = get_object_or_404(News, pk=id)
#     news.increment_views()

#     context = {
#         'news': news
#     }

#     return render(request, "news_detail.html", context)

# def show_xml(request):
#     news_list = News.objects.all()
#     xml_data = serializers.serialize("xml", news_list)
#     return HttpResponse(xml_data, content_type="application/xml")

# def show_json(request):
#     news_list = News.objects.all()
#     data = [
#         {
#             'id': str(news.id),
#             'title': news.title,
#             'content': news.content,
#             'category': news.category,
#             'thumbnail': news.thumbnail,
#             'news_views': news.news_views,
#             'created_at': news.created_at.isoformat() if news.created_at else None,
#             'is_featured': news.is_featured,
#             'user_id': news.user_id,
#         }
#         for news in news_list
#     ]

#     return JsonResponse(data, safe=False)

# def show_xml_by_id(request, news_id):
#    try:
#        news_item = News.objects.filter(pk=news_id)
#        xml_data = serializers.serialize("xml", news_item)
#        return HttpResponse(xml_data, content_type="application/xml")
#    except News.DoesNotExist:
#        return HttpResponse(status=404)

# def show_json_by_id(request, news_id):
#     try:
#         news = News.objects.select_related('user').get(pk=news_id)
#         data = {
#             'id': str(news.id),
#             'title': news.title,
#             'content': news.content,
#             'category': news.category,
#             'thumbnail': news.thumbnail,
#             'news_views': news.news_views,
#             'created_at': news.created_at.isoformat() if news.created_at else None,
#             'is_featured': news.is_featured,
#             'user_id': news.user_id,
#             'user_username': news.user.username if news.user_id else None,
#         }
#         return JsonResponse(data)
#     except News.DoesNotExist:
#         return JsonResponse({'detail': 'Not found'}, status=404)
   
# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('main:login')
#     context = {'form':form}
#     return render(request, 'register.html', context)

# def login_user(request):
#    if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST)

#       if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         response = HttpResponseRedirect(reverse("main:show_main"))
#         response.set_cookie('last_login', str(datetime.datetime.now()))
#         return response

#    else:
#       form = AuthenticationForm(request)
#    context = {'form': form}
#    return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     return response

# def edit_news(request, id):
#     news = get_object_or_404(News, pk=id)
#     form = NewsForm(request.POST or None, instance=news)
#     if form.is_valid() and request.method == 'POST':
#         form.save()
#         return redirect('main:show_main')

#     context = {
#         'form': form
#     }

#     return render(request, "edit_news.html", context)

# def delete_news(request, id):
#     news = get_object_or_404(News, pk=id)
#     news.delete()
#     return HttpResponseRedirect(reverse('main:show_main'))

# @csrf_exempt
# @require_POST
# def add_news_entry_ajax(request):
#     title = request.POST.get("title")
#     content = request.POST.get("content")
#     category = request.POST.get("category")
#     thumbnail = request.POST.get("thumbnail")
#     is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
#     user = request.user

#     new_news = News(
#         title=title, 
#         content=content,
#         category=category,
#         thumbnail=thumbnail,
#         is_featured=is_featured,
#         user=user
#     )
#     new_news.save()

#     return HttpResponse(b"CREATED", status=201)


# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat! Silakan login.')
            return redirect('main:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:show_main')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:login')

@login_required
def show_main(request):
    return render(request, "main_menu.html")

@login_required
def halte_sekitar_view(request):
    # Dummy halte list
    dummy_halte = [
        {'id': 1, 'nama': 'Halte Blok M', 'jarak': '100 m', 'fasilitas': ['Toilet', 'Musolla', 'Gate A']},
        {'id': 2, 'nama': 'Halte Blok A', 'jarak': '400 m', 'fasilitas': ['Toilet', 'Musolla', 'Gate B']},
        {'id': 3, 'nama': 'Halte Blok C', 'jarak': '600 m', 'fasilitas': ['Toilet', 'Musolla', 'Gate C']},
    ]
    context = {'halte_list': dummy_halte}
    return render(request, "halte_sekitar.html", context)

@login_required
def navigasi_halte_view(request, halte_id):
    # Dummy list for lookup
    dummy_halte_list = [
        {'id': 1, 'nama': 'Halte Blok M', 'jarak': '100 m', 'fasilitas': ['Toilet', 'Musolla', 'Koridor 1']},
        {'id': 2, 'nama': 'Halte Blok A', 'jarak': '400 m', 'fasilitas': ['Toilet', 'Musolla', 'Gate B']},
        {'id': 3, 'nama': 'Halte Blok C', 'jarak': '600 m', 'fasilitas': ['Toilet', 'Musolla', 'Gate C']},
    ]
    # Pick by ID
    halte_terpilih = next((halte for halte in dummy_halte_list if halte['id'] == halte_id), None)
    
    context = {'halte': halte_terpilih}
    return render(request, "navigasi.html", context)

@login_required
def jadwal_halte_list_view(request):
    # Dummy stop list
    dummy_halte = [
        {'id': 1, 'nama': 'Halte Blok M', 'jarak': '100 m'},
        {'id': 2, 'nama': 'Halte Blok A', 'jarak': '200 m'},
        {'id': 3, 'nama': 'Halte Blok C', 'jarak': '350 m'},
    ]
    context = {'halte_list': dummy_halte}
    return render(request, "jadwal_halte_list.html", context)

@login_required
def jadwal_halte_detail_view(request, halte_id):
    # Dummy schedule
    dummy_jadwal = [
        {'tujuan': 'Kota', 'gate': 'Gate A', 'waktu': '5 Menit'},
        {'tujuan': 'Blok M', 'gate': 'Gate B', 'waktu': '6 Menit'},
    ]
    context = {
        'halte_nama': 'Halte Blok M', # Fixed halte name for now
        'jadwal_list': dummy_jadwal,
    }
    return render(request, "jadwal_halte_detail.html", context)

@login_required
def lokasi_sekarang_view(request):
    # Dummy location info
    context = {
        'info_lokasi': 'Sekarang Anda berada 200m dari Halte Blok M'
    }
    return render(request, "lokasi_sekarang.html", context)

@login_required
def feedback_view(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text')
        # Placeholder until storage is added
        print(f"Feedback diterima: {feedback_text}")
        messages.success(request, 'Terima kasih atas feedback Anda!')
        return redirect('main:show_main')
        
    return render(request, "feedback.html")
