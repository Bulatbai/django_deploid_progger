
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, HttpResponse,  get_object_or_404
     
from .forms import   Postforms,  Coment_Form, LetRegisterform, CartAddProductForm
from .import models 
from django.contrib.auth.mixins import    LoginRequiredMixin
from .models import   Post, Comments, User  
from django.views import View
from django.views.generic import TemplateView, FormView, DeleteView, CreateView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.decorators.http import require_POST

 
# # class Homeview(View):
# #     def get(self, request, *args, **kwargs):
# #         return render(request, 'index.html')

# # class Homeview(TemplateView):
# #     template_name = 'places/index.html'







def autenticate(request):
    return render(request, 'registr.html')


def kontact(request):
    
    return render(request, 'kontact.html' )



 
def PLaces(request):
    user_don = Post.objects.all()
    return render(request, 'main.html', {'post': user_don})


 



def Create_plase(request):
    if request.method == "POST":
        form_place = Postforms(request.POST)
        if form_place.is_valid():
            form_place.save()
            return redirect(PLaces)
    form = Postforms()
    return render(request, 'places/form.html', {'place_form': form})





# class FeedbackDetailview(DeleteView):
#     queryset = Feedback.objects.all()
#     template_name = 'plase.html'
    
def detail_post(request, id):
    user_ob = Post.objects.all()

    if request.method == "POST":
        comment_person = Coment_Form(request.POST)
        if comment_person.is_valid():
            comment_person.save()
            return redirect(detail_post, id)
    commet = Coment_Form() 
    
    try:
        post = models.Post.objects.get(id=id)
        try:
            comment = models.Comments.objects.filter(post_id=id).order_by('created_date')
             
        except models.Model_Register.DoesNotExist:
            return HttpResponse('No Comments')
    except models.Post.DoesNotExist:
        raise Http404('Post does not exixst, baby')

    return render(request, 'places/plase.html', {'postingo': post, 'com': comment, 'coment': commet, 'post': user_ob})



class Feedbackcreate(FormView):
        template_name = 'feedback.html'
        form_class =  Postforms
        success_url = '/'
         

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)



def edit_place(request, id):
    place_edit = Post.objects.get(id=id)
    if request.method == 'POST':
        place_form = Postforms(data=request.POST, instance=place_edit)
        if place_form.is_valid():
            place_form.save()
            return redirect(detail_post, id=id)
    place_forms = Postforms(instance=place_edit)
    return  render(request, 'places/form.html', {'place_form': place_forms})






def delete_place(request, id):
    place_delete = Post.objects.get(id=id)
    place_delete.delete()
    return redirect(PLaces)






 

 



    








def regist(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        user_form = LetRegisterform(request.POST)
        # Валидация данных из формы
        if user_form.is_valid():
            # Сохраняем пользователя
            new_user = user_form.save(commit=False)
            # Передача формы к рендару
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse('<h1> registr_successful</h2><a href="/"><h3>Home</h3></a></h1>')
    else: # Иначе
        # Создаём форму
        user_form = LetRegisterform()
     
    return render(request, 'registr.html', {'form': user_form})


 