from django.shortcuts import render, redirect
from django.contrib.auth import login
# Access content authorized - redirect login
from django.contrib.auth.mixins import LoginRequiredMixin
# Redirect
from django.urls import reverse_lazy
# import models, DB
# from .models import *

# Create views here.
