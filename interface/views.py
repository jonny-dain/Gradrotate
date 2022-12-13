from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from accounts.permissions import allowed_users
from interface.forms import AdminForm
from interface.gale_shapely import *
from interface.preferences import *
from users.forms import ManagerCreateOffice, ManagerCreateSkills
from users.models import *
from django.contrib import messages
from geopy.geocoders import Nominatim

# Create your views here.
import openpyxl


#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def admin_interface(request):

    #admin = request.user.admin
    admin = Admin.objects.all().first()
    jobs = Job.objects.all()
    users = User.objects.all().count()
    
    form = AdminForm(instance= admin)
    form2 = ManagerCreateOffice()
    additional_skills = ManagerCreateSkills()

    
    interns = Intern.objects.all()
    locations = JobLocation.objects.all()
    computing_skills = ComputingSkills.objects.all()
    analytic_skills = AnalyticSkills.objects.all()
    marketing_skills = MarketingSkills.objects.all()
    management_skills = ManagementSkills.objects.all()
    leadership_skills = LeadershipSkills.objects.all()
    business_skills = BusinessSkills.objects.all()
    admin_skills = AdminSkills.objects.all()
    

    if request.method == 'POST':
        form = AdminForm(request.POST, instance= admin)  
        form2 =ManagerCreateOffice(request.POST)
        additional_skills =ManagerCreateSkills(request.POST)

        if 'Submit_office' in request.POST:
            if form2.is_valid():
                office_name = form.data['location']
                address = form.data['address']
                try:
                    geolocator = Nominatim(user_agent="interface")
                    location = geolocator.geocode(address)
                    offices = JobLocation.objects.filter()
                    offices.create(location = office_name, address = location.address, latitude=location.latitude, longitude= location.longitude)
                except:
                    messages.error(request, 'Incorrect location! Please copy the google maps address')
                    return redirect('../../../admin_interface')
                return redirect('../../../admin_interface')               
        elif 'Submit_skills' in request.POST:

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
            
            return redirect('../../../admin_interface')
       
       
        else:   
            if form.is_valid():
                form.save()
                return redirect('../../../admin_interface')


    context = { 'form': form, 
    'users':users,
    'jobs' :jobs , 
    'interns' : interns, 
    'locations' :locations, 
    'computing_skills' : computing_skills,
    'analytic_skills'  :analytic_skills,
    'marketing_skills' : marketing_skills,
    'management_skills' : management_skills,
    'leadership_skills' : leadership_skills,
    'business_skills' : business_skills,
    'admin_skills' : admin_skills,
    'additional_office':form2,
    'additional_skills': additional_skills
    }
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

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteJob(request, pk):

    job = Job.objects.get(id=pk)
    InternPreference.objects.filter(job = job).delete()
    User.objects.get(job = job).delete()
    job.delete()
    return redirect('../../../admin_interface/jobs/')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteOffice(request, pk):
    office = JobLocation.objects.get(id=pk)
    office.delete()
    return redirect('../../../admin_interface')


#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillComputing(request, pk):
    skill = ComputingSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillAnalytic(request, pk):
    skill = AnalyticSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillMarketing(request, pk):
    skill = MarketingSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillManagement(request, pk):
    skill = ManagementSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillLeadership(request, pk):
    skill = LeadershipSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillBusiness(request, pk):
    skill = BusinessSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteSkillAdmin(request, pk):
    skill = AdminSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')





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
        try:
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
        except:

            messages.info(request, 'Error - Make sure all Intern preferences are filled in')
            return redirect('../../../admin_interface')

    else:
        messages.info(request, 'You must be in the allocate phase to allocate positions')

        return redirect('../../../admin_interface')




#This allocates excel files 

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def allocate_excel(request):


    if "GET" == request.method:
        context = {}
        return render(request, 'interface/allocate_excel.html', context)
    else:
        excel_file = request.FILES["excel_file"]

        #Validation of excel file needs to be complete...

        workbook = openpyxl.load_workbook(excel_file)
        try:
            intern_excel = workbook["Sheet1"]
            job_excel = workbook["Sheet2"] 
            intern_preference = excel_preferences(preferences = intern_excel)
            job_preference = excel_preferences(preferences = job_excel)
            intern_set = excel_set(model = intern_excel)
            job_set = excel_set(model = job_excel)
            preference_number = intern_excel.max_row - 1
            allocated_pairs = gale_allocation(
                intern_set=intern_set,
                job_set=job_set,
                intern_preference=intern_preference,
                job_preference=job_preference,
            )  
        except:
            messages.error(request, 'Wrong format! Please edit and try again')
            return redirect('../../../admin_interface/allocate/excel')


        context = {'allocated_pairs':allocated_pairs, 'intern_preference':intern_preference, 'job_preference': job_preference, 'preference_number' : range(1,preference_number + 1)}
        return render(request, 'interface/allocate_excel.html', context)






