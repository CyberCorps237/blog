from django.shortcuts import get_object_or_404, render

from blog_cybercorpscm.models import Message, Post

def index(request):
    posts = Post.objects.all()
    
    return render(request, 'pages\index.html',{'posts':posts})
def post(request, post_id):
    posts_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'pages\post.html',{'posts_detail':posts_detail})


def apropos(request):
    
    return render(request, 'pages\propos_about.html')

def contact(request):

    # if request.method=='POST':
    #     f_name= request.POST.get('name')
    #     f_email = request.POST.get('email')
    #     f_tel = request.POST.get('phone')
    #     f_message = request.POST.get('message')
    #     content = "Le message a ete envoyer avec success"
    #     new_message = Message.objects.create(nom=f_name, email=f_email, telephone=f_tel, contenu=f_message)
    #     new_message.save()
    #     return render(request, 'pages\contact.html',{'contain':content})

    return render(request, 'pages\contact.html')


