from django.shortcuts import render,redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, AddJobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.
########################################################################

def job_list(request):
    job_list = Job.objects.all()
    llist = Job.objects.all()
    jfilter = JobFilter(request.GET,queryset=job_list)
    job_list = jfilter.qs
    paginator = Paginator(job_list, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs' : page_obj,
        'llist' : llist,
        'jfilter': jfilter,
    }
    return render(request,'job/job_list.html',context)

########################################################################

def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()


    context = {
        'job' : job_detail,
        'form1' : form,
    }
    return render(request,'job/job_detail.html',context)

#########################################################################
@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('jobs:job_list')
    else:
        form = AddJobForm()

    context = {
        'form': form,
    }
    return render(request,'job/add_job.html',context)