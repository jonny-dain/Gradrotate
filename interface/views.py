from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from interface.forms import AdminForm
from interface.gale_shapely import *
from interface.preferences import *
from users.models import *
from django.contrib import messages

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def admin_interface(request):

    #admin = request.user.admin
    admin = Admin.objects.all().first()
    form = AdminForm(instance= admin)

    jobs = Job.objects.all()
    interns = Intern.objects.all()

    #Want to make a settings dashboard to allocate jobs



    # tests
    #print(job_preference)


    if request.method == 'POST':
        form = AdminForm(request.POST, instance= admin)   
   
        if form.is_valid():
            #gathers all the skills
            form.save()
            return redirect('../../../admin_interface')

    context = {'jobs' :jobs , 'interns' : interns, 'form': form}
    return render(request, 'interface/interface.html', context)










#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def intern_interface(request):
    
    
    interns = Intern.objects.all()
    jobs = Job.objects.all()

    intern_preference = intern_preference_dictionary()

    context = {'interns' : interns, 'jobs' :jobs , 'intern_preference' : intern_preference}
    return render(request, 'interface/interns.html', context)

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def job_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    job_preference = job_preference_dictionary()

    context = {'jobs' :jobs , 'interns' : interns, 'job_preference' : job_preference}
    return render(request, 'interface/jobs.html', context)

#This is to delete Interns from the system
#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteIntern(request, pk):

    
    intern = Intern.objects.get(id=pk)
    InternPreference.objects.filter(intern = intern).delete()
    User.objects.get(intern = intern).delete()
    intern.delete()
    #need to delete all interns items
    return redirect('../../../admin_interface/interns/')

def deleteJob(request, pk):

    job = Job.objects.get(id=pk)
    InternPreference.objects.filter(job = job).delete()
    User.objects.get(job = job).delete()
    job.delete()
    return redirect('../../../admin_interface/jobs/')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def allocate_interface(request):
    admin = Admin.objects.all().first()

    if (admin.phase == 'Allocation'):
        jobs = Job.objects.all()
        interns = Intern.objects.all()

            #if jobs.count() != interns.count():
            #Add error messages here.. 
        #    return redirect('../../../admin_interface')

        intern_preference = intern_preference_dictionary()
        job_preference = job_preference_dictionary()



        job_set = set(jobs)
        intern_set = set(interns)


        allocated_pairs = gale_allocation(
            intern_set=intern_set,
            job_set=job_set,
            intern_preference=intern_preference,
            job_preference=job_preference,
        )  


        

        print(allocated_pairs)

        first_preference = 0
        second_preference = 0
        third_preference = 0



        #works out how many interns got their first,second and third choices
        for pair in allocated_pairs:
            for intern, jobs in intern_preference.items():
                if pair[0] == intern:
                    if pair[1] == jobs[0]:
                        first_preference += 1
                    elif pair[1] == jobs[1]:
                        second_preference += 1
                    elif pair[1] == jobs[2]:
                        third_preference += 1


            




        context = {'jobs' :jobs , 'interns' : interns, 'allocated_pairs': allocated_pairs, 'first_preference' : first_preference, 'second_preference' : second_preference, 'third_preference' : third_preference}
        return render(request, 'interface/allocate.html', context)

    else:
        messages.info(request, 'You must be in the allocate phase to allocate positions')

        return redirect('../../../admin_interface')






