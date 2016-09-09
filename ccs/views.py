from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import CounselCenter
from .models import UnivCounselingCenter

# Create your views here.
def ccs_list(request):
	centers = CounselCenter.objects.all()
	return render(request, 'ccs/ccs_list.html', {'centers': centers})


def center_detail(request, pk):
	center = get_object_or_404(CounselCenter, pk=pk)
	return render(request, 'ccs/center_detail.html', {'center':center})

def univCounselingCenterList(request):
	univCounselingCenters = UnivCounselingCenter.objects.all()
	return render(request, 'ccs/ccs_list.html', {'univCounselingCenters', univCounselingCenters})


def search_action(request):
	center = get_object_or_400(CounselCenter.objects.all())
	return render(request, 'ccs/search_result.html', {'center':center})