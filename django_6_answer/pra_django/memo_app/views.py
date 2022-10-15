from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .forms import PostForm, RecordNumberForm,OrederNumberForm,UpdateForm,CommentForm
from django.contrib.auth import get_user_model




def index(request, now_page=1,*args, **kwargs):
        # レコード件数
    if 'record_number' in request.session:
        record_number = request.session['record_number']
    else:
        record_number = 10

    if 'order_number' in request.session:
        order_number = request.session['order_number']
    else:
        order_number = 'new'


    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    order_number_form = OrederNumberForm()
    order_number_form.initial = {'order_number': str(order_number)}


    if order_number == "new":
        memos = Memo.objects.filter(user=request.user).order_by('update_datetime').reverse()
    else:
        memos = Memo.objects.filter(user=request.user).order_by('update_datetime')
    page = Paginator(memos, record_number)
    cm = Comment.objects.all().order_by('update_datetime')
    params = {
        'page': page.get_page(now_page),
        'memo':memos,
        'comment':cm,
        'form': PostForm(),
        'record_number_form': record_number_form,
        'order_number_form': order_number_form,
        }
    return render(request, 'index.html', params)


def post(request,*args, **kwargs):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        user = get_user_model().objects.get(id=request.user.id)
        memo = Memo(content=request.POST.get('content'), user=user)
        memo.save()
    else:
        print(form.errors)

    return redirect(to='/')

def update(request,num):
    memo = Memo.objects.get(id=num)
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=memo)
        form.save()
        return redirect(to='/')
    else:
        params = {
        'id':num,
        'form':UpdateForm(instance=memo)
    }

    return render(request, 'update.html',params)



def comment(request,memo,**kwargs):
    cm = Comment.objects.filter(memo=memo)
    params = {
        'form': CommentForm(),
        'comment':cm,
        'memo':memo,
        }

    return render(request, 'comment.html', params)



def post_comment(request,memo,*args, **kwargs):
    form = CommentForm(request.POST,instance=Comment())
    if form.is_valid():
        memo = Memo.objects.get(content=memo)
        cm = Comment(comment=request.POST.get('comment') ,memo=memo)
        cm.save()
    else:
        print(form.errors)

    return redirect(to='/')

def delete(request,num):
    memo = Memo.objects.get(id=num)
    if (request.method == 'POST'):
        memo.delete()
        return redirect(to='/')
    params = {
        'id':num,
        'content':memo}
    return render(request, 'delete.html',params)

def set_record_number(request,*args, **kwargs):
        request.session['record_number'] = request.POST['record_number']
        return redirect(to='/')

def set_order_number(request,*args, **kwargs):
    request.session['order_number'] = request.POST['order_number']
    return redirect(to='/')
