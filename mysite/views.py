# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from urllib.parse import urlencode
from urllib.request import urlopen
import json

# Create your views here.

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def search(request):
    return render(request, "search.html")

def query(request, query):
    # 외부 API 연동 예제는 아래 블로그를 참조하시면 이해가 좀 더 되실 거 같아요
    # http://blog.naver.com/haru-studio/220990470482

    url = 'https://jsonplaceholder.typicode.com/posts/'
    # API 서버에서 쿼리 옵션 지원할 경우
    # url = url + urlencode(query)

    data = urlopen(url).read()

    if query:
        data = json.loads(data)

        result = []
        for item in data:
            if item['title'].startswith(query):
                result.append(item)
            if len(result) > 5:
                break
        
        result = json.dumps(result)

        return HttpResponse(result, content_type="application/json")
    else:
        return HttpResponse(data, content_type="application/json")