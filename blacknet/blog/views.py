from django.shortcuts import render, redirect
from .models import Blogpost
from  django.http import HttpResponse



def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request,"blog/index.html",
                  {'myposts':myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,"blog/blogpost.html",
                  {'post':post})
def post(request):
    if request.method == "POST":
        post=Blogpost()
        post.title = request.POST.get('title', '')
        post.head0 = request.POST.get('head0', '')
        post.chead0 = request.POST.get('chead0', '')
        post.head1 = request.POST.get('head1', '')
        post.chead1 = request.POST.get('chead1', '')
        post.head2 = request.POST.get('head2', '')
        post.chead2 = request.POST.get('chead2', '')
        post.pub_date = request.POST.get('pub_date', '')

        if len(request.FILES) !=0:
            post.thumbnail = request.FILES['thumbnail']
        post.save()
        print(post.title, post.head0, post.chead0, post.head1, post.chead1, post.head2, post.chead2, post.pub_date, post.thumbnail)
        return redirect('/blog/')
    return render(request, 'blog/post.html')











    # thank = False
    # if request.method == "POST":
    #     print(request)
    #     title = request.POST.get('title', '')
    #     head0 = request.POST.get('head0', '')
    #     chead0 = request.POST.get('chead0', '')
    #     head1 = request.POST.get('head1', '')
    #     chead1 = request.POST.get('chead1', '')
    #     head2 = request.POST.get('head2', '')
    #     chead2 = request.POST.get('chead2', '')
    #     pub_date = request.POST.get('pub_date', '')
    #     thumbnail = request.POST.get('thumbnail','')
    #     print(title, head0, chead0, head1, chead1, head2, chead2, pub_date, thumbnail)
    #     post = Blogpost(title=title, head0=head0, chead0=chead0, head1=head1, chead1=chead1, head2=head2,
    #                     chead2=chead2, pub_date=pub_date, thumbnail=thumbnail)
    #     post.save()
    #     thank = True
    # return render(request, 'blog/post.html', {'thank': thank})

