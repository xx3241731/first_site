from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post #把在models.py中自定義的Class引入Post資料表
import random
from datetime import datetime
from mysite.models import AccessInfo, Branch, StoreIncome

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all() #取得所有Post 並放入變數posts
    now = datetime.now()       #index.html即可使用datetime
    return render(request,'index.html',locals())#最後需要return

def lotto(request):
    now = datetime.now()
    lucky = random.randint(1,42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1,42))
    return render(request,'lotto.html',locals())

def showpost(request, slug):
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        return render(request,'post.html',locals())
    except:
        return redirect('/')

def mychart(request,bid=0):
    branchs = Branch.objects.all()

    now = datetime.now()
    if bid == 0:
        data = StoreIncome.objects.filter(income_month='11')
    else:
        data = StoreIncome.objects.filter(branch=bid)
    return render(request, 'mychart.html',locals())

def mychart2(request,bid=0):
    branchs = Branch.objects.all()

    now = datetime.now()
    if bid == 0:
        data = StoreIncome.objects.filter(income_month='11')
    else:
        data = StoreIncome.objects.filter(branch=bid)
    return render(request, 'mychart2.html',locals())

def chart(request,year=0,month=0):
    branchs = Branch.objects.all()

    now = datetime.now()
    if year == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(income_year=year)
        if month>0:
            data = data.filter(income_month=month)
    if year>0 and month>0:
        title ='{}年{}月各分店營收情形'.format(year,month)
    elif year>0:
        title = '{}年各分店營收情形'.format(year)
    else:
        title = '各分店營收情形'
    return render(request, 'mychart.html',locals())




   