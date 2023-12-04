# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.shortcuts import render

# Create your views here.

def getRole(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "https://isis2503-arquimedevs.us.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['isis2503-arquimedevs.us.auth0.com/role']
    return (role)