# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import json
from django.views.generic import View, ListView
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from .models import Header, Detail
from django.views.decorators.csrf import ensure_csrf_cookie

NEW_PAGE_ID = 0

class HandsonTableView(View):

    def get(self, request, *args, **kwargs):
        details = Detail.objects.filter(header_pk=self.kwargs.get('pk')).select_related().all()
        return HttpResponse(
            serializers.serialize('handsontablejson', details),
            content_type='application/json'
        )

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.load(body_unicode)
        header = self.update_header(self.kwagrs.get('pk'))
        Detail.objects.filter(header=header).delete()

        for b in body:
            Detail(
                header=header,
                purchase_date = b.get('purchase_date'),
                customer_name = b.get('customer_name'),
                price = b.get('price'),
            ).save()

        return HttpResponse('OK')

    def update_header(self, pk):
        if int(pk)==NEW_PAGE_ID:
            new_header = Header(update_at = timezone.now())
            new_header.save()
            print (Header.objects.latest('id').id)
            return new_header
        header = Header.object.filter(pk=pk).first()
        header.update_at = timezone.now()
        header.save()
        return header
