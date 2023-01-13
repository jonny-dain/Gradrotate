from email.policy import HTTP
from unicodedata import name
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.permissions import allowed_users, required_phase, update_progress
from users.models import InternPreference
from .forms import *
from django.contrib import messages
import json 
from geopy.geocoders import Nominatim



# Create your views here.

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@update_progress(1)
@required_phase(phase=['Intern collection'])
def student_form(request):
    intern = request.user.intern
    form = StudentForm(instance= intern)
    

    if request.method == 'POST':
        form = StudentForm(request.POST, instance= intern)        
        if form.is_valid():
            

            form.save()
            return redirect('../../form/student_form/requirements')


    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form.html', context)
    


@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@update_progress(2)
@required_phase(phase=['Intern collection'])
def student_form_requirements(request):
    intern = request.user.intern
    form = StudentForm2(instance= intern)
    
    location_list = list(JobLocation.objects.all().values()) 
    location_json = json.dumps(location_list)
    
    if request.method == "POST":
        form = StudentForm2(request.POST, instance= intern) 
        if form.is_valid():
            #intern.location = request.POST['pref_location']
            #intern.remote = request.POST['remote_option']
            form.save()
            return redirect('../../form/student_form/skills')

    context = {'form': form, 'intern': intern, 'locations': location_json}
    return render(request, 'users/student_form2.html', context)



@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@update_progress(3)
@required_phase(phase=['Intern collection'])
def student_form_skills(request):
    intern = request.user.intern
    form = StudentForm3(instance= intern)

    computing_skills = ComputingSkills.objects.all()

    if request.method == "POST":
        form = StudentForm3(request.POST, instance= intern) 
        if form.is_valid() and 'Submit' in request.POST:
            #gathers all the skills

            computing_skills = form.cleaned_data['computing_skills']
            analytic_skills = form.cleaned_data['analytic_skills']
            marketing_skills = form.cleaned_data['marketing_skills']
            management_skills = form.cleaned_data['management_skills']
            leadership_skills = form.cleaned_data['leadership_skills']
            business_skills = form.cleaned_data['business_skills']
            admin_skills = form.cleaned_data['admin_skills']

            

            if (len(computing_skills) + len(analytic_skills) + len(marketing_skills) + len(management_skills) + len(leadership_skills) +len(business_skills)+len(admin_skills)) > 5:
                messages.info(request, '5 Skill maximum')
                context = {'form': form, 'intern': intern}
                return render(request, 'users/student_form3.html', context)
            else:
                
                form.save()
                return redirect('../../dashboard')

        else:
            messages.info(request, 'Error completing form')
            context = {'form': form, 'intern': intern}
            return render(request, 'users/student_form3.html', context)


    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form3.html', context)





    
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_form(request, pk):
    #job = request.user.job
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')

    
    

    if job.progress < 1:
        job.progress = 1
        job.save()

    #.job
    form = ManagerForm(instance= job)


    if request.method == 'POST':
        
        form = ManagerForm(request.POST, instance= job)     
 

        if form.is_valid() and 'Submit_form' in request.POST:
            
            form.save()
            return redirect('../../../form/'+str(job.id)+'/manager_form/information')


    context = {'form': form, 'job': job}
    return render(request, 'users/manager_form.html', context)





@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_form_requirements(request, pk):
    #job = request.user.job
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')

    if job.progress < 2:
        job.progress = 2
        job.save()

    form = ManagerForm2(instance= job)

    location_list = list(JobLocation.objects.all().values()) 
    location_json = json.dumps(location_list)

    if request.method == 'POST':
        form = ManagerForm2(request.POST, instance= job)        
        if form.is_valid():
            #gathers all the skills
            form.save()
            return redirect('../../../form/'+str(job.id)+'/manager_form/information_2')

    context = {'form': form, 'job': job, 'locations': location_json}
    return render(request, 'users/manager_form2.html', context)



    
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_form_additional_requirements(request, pk):
    #job = request.user.job
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')

    if job.progress < 3:
        job.progress = 3
        job.save()

    form = ManagerForm4(instance= job)
    form2 = ManagerCreateOffice()

    location_list = list(JobLocation.objects.all().values()) 
    location_json = json.dumps(location_list)




    if request.method == 'POST':

        form = ManagerForm4(request.POST, instance= job)   
        form2 =ManagerCreateOffice(request.POST)  
        if 'Submit_office' in request.POST:
            if form2.is_valid():
                office_name = form.data['location']
                address = form.data['address']
                try:
                    geolocator = Nominatim(user_agent="users")
                    location = geolocator.geocode(address)
                    offices = JobLocation.objects.filter()
                    offices.create(location = office_name, address = location.address, latitude=location.latitude, longitude= location.longitude)
                except:
                    messages.info(request, 'Incorrect address')
                    context = {'form': form, 'additional_office': form2, 'job': job, 'locations': location_json}
                    return render(request, 'users/manager_form4.html', context)

                return redirect('../../../form/'+str(job.id)+'/manager_form/information_2')

        elif 'Submit_form' in request.POST:   
            if form.is_valid():
                #gathers all the skills
                job.wage = form.data['wage_value']
                form.save()
                return redirect('../../../form/'+str(job.id)+'/manager_form/skills')

        


                

    context = {'form': form, 'additional_office': form2, 'job': job, 'locations': location_json}
    return render(request, 'users/manager_form4.html', context)






@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_form_skills(request, pk):
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')

    if job.progress < 4:
        job.progress = 4
        job.save()

    form = ManagerForm3(instance= job)
    additional_skills = ManagerCreateSkills()

    if request.method == 'POST':
        form = ManagerForm3(request.POST, instance= job)      

        additional_skills =ManagerCreateSkills(request.POST)
        if 'Submit_skills' in request.POST:

            if additional_skills.is_valid():
                skill_category = form.data['skill_category']
                skill_name = form.data['name']


                if skill_category == 'Computing':
                    skills = ComputingSkills.objects.filter()
                elif skill_category == 'Analytic':
                    skills = AnalyticSkills.objects.filter()
                elif skill_category == 'Marketing':
                    skills = MarketingSkills.objects.filter()
                elif skill_category == 'Management':
                    skills = ManagementSkills.objects.filter()
                elif skill_category == 'Leadership':
                    skills = LeadershipSkills.objects.filter()
                elif skill_category == 'Business':
                    skills = BusinessSkills.objects.filter()
                elif skill_category == 'Admin':
                    skills = AdminSkills.objects.filter()
                
                skills.create(name = skill_name)
            
            return redirect('../../../form/'+str(job.id)+'manager_form/skills')

        elif form.is_valid() and 'Submit_form' in request.POST:
            #gathers all the skills

            computing_skills = form.cleaned_data['computing_skills']
            analytic_skills = form.cleaned_data['analytic_skills']
            marketing_skills = form.cleaned_data['marketing_skills']
            management_skills = form.cleaned_data['management_skills']
            leadership_skills = form.cleaned_data['leadership_skills']
            business_skills = form.cleaned_data['business_skills']
            admin_skills = form.cleaned_data['admin_skills']

            if (len(computing_skills) + len(analytic_skills) + len(marketing_skills) + len(management_skills) + len(leadership_skills) +len(business_skills)+len(admin_skills)) > 5:
                messages.info(request, '5 Skill maximum')
                context = {'form': form, 'job': job, 'additional_skills' : additional_skills}
                return render(request, 'users/manager_form3.html', context)
            else:

                form.save()

                #redirect to done... 
                return redirect('../../../form/'+str(job.id)+'/manager_form/complete')


    context = {'form': form, 'job': job, 'additional_skills' : additional_skills}
    return render(request, 'users/manager_form3.html', context)



@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@update_progress(5)
@required_phase(phase=['Intern collection'])
def student_complete(request):
    #Top choices
    intern = request.user.intern
    
    intern.save()

    preferences = intern.internpreference_set.all()
    intern_dictionary = {}

    for preference in preferences:
        intern_dictionary[preference.job] = preference.preference

    intern_dictionary = sorted(intern_dictionary.items(), key=lambda x:x[1])
    intern_dictionary = dict(intern_dictionary)
    preference_list = list(intern_dictionary.keys())




    context = {'preference_list' : preference_list}
    return render(request, 'users/student_complete.html', context)




@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_complete(request, pk):
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')



    if job.progress < 5:
        job.progress = 5
        job.save()






    
    skills = []
    skills += job.computing_skills.all()
    skills += job.analytic_skills.all()
    skills += job.marketing_skills.all()
    skills += job.management_skills.all()
    skills += job.leadership_skills.all()
    skills += job.business_skills.all()
    skills += job.admin_skills.all()
  


    context = {'job' : job, 'skills' : skills }
    return render(request, 'users/manager_complete.html', context)


@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Intern'])
@required_phase(phase=['Allocation'])
def student_allocation_complete(request):
    intern = request.user.intern
    job = intern.allocated_job
    admin = Admin.objects.all().first()

    context = {'job':job, 'admin':admin}

    

    

    return render(request, 'users/student_allocate_complete.html', context)



@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Allocation'])
def manager_allocation_complete(request):
    
    admin = Admin.objects.all().first()
    manager_jobs = Job.objects.filter(manager = request.user.manager)


    context = {'manager_jobs':manager_jobs, 'admin':admin}
    return render(request, 'users/manager_allocate_complete.html', context)









@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_dashboard(request):
    
    manager_jobs = Job.objects.filter(manager = request.user.manager)

    context = {'manager_jobs':manager_jobs}
    return render(request, 'users/manager_dashboard.html', context)


@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_create_job(request):
    admin = Admin.objects.all().first()
    user = request.user
    manager = request.user.manager

    job = Job.objects.create(
        manager = manager,
        email = user.email,
        
    )
    job.save()

    admin.total_jobs += 1
    admin.save()


    return redirect('../../../form/'+str(job.id)+'/manager_form')




@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Manager'])
@required_phase(phase=['Job creation'])
def manager_delete_job(request, pk):
    
    job = Job.objects.get(id=pk)
    manager = request.user.manager

    if job.manager != manager:
        return redirect('../../../../../form/manager_dashboard')



    job.delete()
    InternPreference.objects.filter(job = job).delete()
    return redirect('../../../../../../form/manager_dashboard/')