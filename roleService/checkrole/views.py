# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import requests
import json
from django.shortcuts import render

# Create your views here.

def getRole(request):
    user = json.loads(json.loads(request.body))
    accessToken = user["extra_data"]['access_token']
    url = "https://isis2503-arquimedevs.us.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['isis2503-arquimedevs.us.auth0.com/role']
    return HttpResponse(role)