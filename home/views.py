from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class Base(View):
    views = {}
class HomeView(Base):
    def get(self,request):
        self.views['categories'] = category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['reviews'] = CustomerReview.objects.all()
        return render(request,'index.html',self.views)