
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Station, Guestbook  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import translation  
from django.contrib.auth import authenticate, login


# 1. (Home)
def home(request):
    return render(request, 'stations/home.html')

# 2. (About)
def about(request):
    return render(request, 'stations/about.html')

# 3.(Tour) 
@login_required
def tour(request):
    return render(request, 'stations/tour.html')

# 4. AJAX
def get_station_api(request, order):
    try:
        st = Station.objects.get(order=order)
        

        lang = translation.get_language() 
        
        return JsonResponse({
            'title': st.title_ar if lang == 'ar' else st.title_en,
            'desc': st.desc_ar if lang == 'ar' else st.desc_en,
            'video': st.video.url,
            'audio': st.audio.url,
            'order': st.order
        })
    except Station.DoesNotExist:
        return JsonResponse({'error': 'end'}, status=404)

# 5. Guestbook save
def save_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        
        if name and message: 
            Guestbook.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=name,
                message=message
            )
            return JsonResponse({'status': 'ok'})
            
    return JsonResponse({'status': 'failed'}, status=400)

def guestbook_view(request):
    return render(request, 'stations/guestbook.html')

# 6. Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        user = authenticate(username=user_id, password=user_pass)
        
        if user is not None:
            login(request, user)
            return redirect('/admin/') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'login.html')