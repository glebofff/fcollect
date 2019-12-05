# -*- coding: utf-8 -*-
#
# Author: Stanislav Glebov <glebofff@gmail.com> 
# Created: 05/12/19

from django.urls import path

from . import views

urlpatterns = [
    path('convert', views.ConvertCurrencyView.as_view(), name='convert')
]
