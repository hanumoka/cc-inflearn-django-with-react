from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from instagram.forms import PostForm
from .models import Tag


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list()) # 순서 중요, 모체인 post가 먼저저장 되어야 한다.
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect("/")  # TODO: get_absolute_url 활용
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form": form,
    })
