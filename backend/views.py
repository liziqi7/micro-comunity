from django.http import HttpResponse
from django.shortcuts import render
from backend.models import *
from django.core import serializers
from django.db.models import F
from threading import Lock
import re, json

# Create your views here.
def community(request):
	resp = list(Community.objects.all().values())
	return HttpResponse(json.dumps(resp), content_type="application/json")


def gift(request):
	resp = {}
	if request.method == 'GET':
		community = request.GET.get('community','')
		try:
			community = Community.objects.get(id=community)
		except Exception, e:
			resp['error'] = 'no_such_community'
			return HttpResponse(json.dumps(resp), content_type="application/json")

		items = [item['gift'] for item in StoreItem.objects.filter(community=community).values('gift')]
		gifts = list(Gift.objects.filter(id__in=items).values())
		return HttpResponse(json.dumps(gifts), content_type="application/json")

	resp['error'] = 'unsupported_method'
	return HttpResponse(json.dumps(resp), content_type="application/json")


def order(request):
	resp = {}
	if request.method == 'GET':
		community = request.GET.get('community', '')
		username = request.GET.get('username', '')
		mobile = request.GET.get('mobile', '')
		count = request.GET.get('count', '')
		gifts = request.GET.get('gifts', '')

		try:
			community = Community.objects.get(id=community)
			gifts = json.loads(gifts)
			assert len(gifts) > 0
			assert len(username) > 0
			assert re.match(r'^\d{11}$', mobile)
			assert re.match(r'^[1-9]\d*$', count)
		except Exception, e:
			resp['error'] = 'parameter_error'
			return HttpResponse(json.dumps(resp), content_type="application/json")

		lock = Lock()
		lock.acquire()
		try:
			total = 0
			for gift, number in gifts.iteritems():
				gift = int(gift)
				number = int(number)
				item = StoreItem.objects.get(gift_id=gift,community=community)
				total += number

			order = Order.objects.create(community=community,username=username,mobile=mobile,count=total)
			for gift, number in gifts.iteritems():
				gift = int(gift)
				number = int(number)
				OrderItem.objects.create(order=order,gift_id=gift,number=number)
			resp['status'] = 'ok'
			return HttpResponse(json.dumps(resp), content_type="application/json")
		except Exception, e:
			resp['error'] = 'cannot_get_gifts'
			return HttpResponse(json.dumps(resp), content_type="application/json")
		finally:
			lock.release()

	resp['error'] = 'unsupported_method'
	return HttpResponse(json.dumps(resp), content_type="application/json")