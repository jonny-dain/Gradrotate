import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from accounts.permissions import allowed_users, update_phase
from interface.forms import AdminForm, AdminForm2, AdminToggleAlgorithm, AdminToggleAutomaticPhase, AdminToggleNotify
from interface.gale_shapely import *
from interface.preferences import *
from users.forms import ManagerCreateOffice, ManagerCreateSkills
from users.models import *
from django.contrib import messages
from geopy.geocoders import Nominatim

# Create your views here.
import openpyxl


#Admin internface
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
@update_phase
def admin_interface(request):

    #admin = request.user.admin
    admin = Admin.objects.all().first()
    jobs = Job.objects.all()
    users = User.objects.all().count()
    
    form = AdminForm(instance= admin)
    form2 = ManagerCreateOffice()
    additional_skills = ManagerCreateSkills()
    automatic_phase = AdminForm2(instance = admin)
    toggle_automatic_phase = AdminToggleAutomaticPhase(instance = admin)
    toggle_algorithm = AdminToggleAlgorithm(instance = admin)

    
    interns = Intern.objects.all()
    locations = JobLocation.objects.all()
    computing_skills = ComputingSkills.objects.all()
    analytic_skills = AnalyticSkills.objects.all()
    marketing_skills = MarketingSkills.objects.all()
    management_skills = ManagementSkills.objects.all()
    leadership_skills = LeadershipSkills.objects.all()
    business_skills = BusinessSkills.objects.all()
    admin_skills = AdminSkills.objects.all()
  
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
    'additional_skills': additional_skills,
    'automatic_phase':automatic_phase,
    'toggle_automatic_phase':toggle_automatic_phase,
    'toggle_algorithm':toggle_algorithm,
    'admin':admin
    }

    if request.method == 'POST':
        form = AdminForm(request.POST, instance= admin)  
        form2 =ManagerCreateOffice(request.POST)
        additional_skills =ManagerCreateSkills(request.POST)
        automatic_phase = AdminForm2(request.POST, instance = admin)
        toggle_automatic_phase = AdminToggleAutomaticPhase(request.POST, instance = admin)

        toggle_algorithm = AdminToggleAlgorithm(request.POST, instance= admin)

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
                    messages.error(request, 'Incorrect Address - Please submit a valid postcode for this address')
                    return redirect('../../../admin_interface')
                return redirect('../../../admin_interface')

        elif 'Submit_toggle_automated' in request.POST:
            if toggle_automatic_phase.is_valid():
                toggle_automatic_phase.save()
                return redirect('../../../admin_interface')



        elif 'Submit_phase' in request.POST:
            if automatic_phase.is_valid():
                #Changes the phases on the admin panel 

                allocation_creation_date = form.data['allocation_creation_date']
                intern_creation_date = form.data['intern_creation_date']
                job_creation_date = form.data['job_creation_date']
                if (job_creation_date >= intern_creation_date) or (intern_creation_date >= allocation_creation_date) or (job_creation_date >= allocation_creation_date):
    
                    messages.error(request, 'Incorrect Date Change Order - Please refer to the info button for more information')
                    return render(request, 'interface/interface.html', context)
                    
                else:
                    automatic_phase.save()
                    return redirect('../../../admin_interface')


                       
        elif 'Submit_skills' in request.POST:

            if additional_skills.is_valid():
                skill_category = form.data['skill_category']
                skill_name = form.data['name']

                if ComputingSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under computing skills!')
                elif AnalyticSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under analtyic skills!')
                elif ManagementSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under management skills!')
                elif MarketingSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under marketing skills!')
                elif LeadershipSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under leadership skills!')
                elif BusinessSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under business skills!')
                elif AdminSkills.objects.filter(name = skill_name):
                        messages.info(request, str(skill_name) + ' already exists under admin skills!')
                else:
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
        
        elif 'Submit_algorithm' in request.POST:
            if toggle_algorithm.is_valid():
                toggle_algorithm.save()
                return redirect('../../../admin_interface')

       
       
        else:   
            if form.is_valid():
                form.save()

                
                
                return redirect('../../../admin_interface')


    
    return render(request, 'interface/interface.html', context)











#Admin Intern interface
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def intern_interface(request):
    
    
    interns = Intern.objects.all()
    jobs = Job.objects.all()

    intern_preference = intern_preference_dictionary()

    context = {'interns' : interns, 'jobs' :jobs , 'intern_preference' : intern_preference}
    return render(request, 'interface/interns.html', context)


#Admin Job interface
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def job_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    job_preference = job_preference_dictionary()

    context = {'jobs' :jobs , 'interns' : interns, 'job_preference' : job_preference}
    return render(request, 'interface/jobs.html', context)

#This is to delete Interns from the system
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteIntern(request, pk):

    
    intern = Intern.objects.get(id=pk)
    InternPreference.objects.filter(intern = intern).delete()
    User.objects.get(intern = intern).delete()
    intern.delete()
    #need to delete all interns items
    return redirect('../../../admin_interface/interns/')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteJob(request, pk):

    job = Job.objects.get(id=pk)
    InternPreference.objects.filter(job = job).delete()
    job.delete()
    return redirect('../../../admin_interface/jobs/')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteOffice(request, pk):
    office = JobLocation.objects.get(id=pk)
    office.delete()
    return redirect('../../../admin_interface')


@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillComputing(request, pk):
    skill = ComputingSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillAnalytic(request, pk):
    skill = AnalyticSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillMarketing(request, pk):
    skill = MarketingSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillManagement(request, pk):
    skill = ManagementSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillLeadership(request, pk):
    skill = LeadershipSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillBusiness(request, pk):
    skill = BusinessSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')

@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def deleteSkillAdmin(request, pk):
    skill = AdminSkills.objects.get(id=pk)
    skill.delete()
    return redirect('../../../admin_interface')


@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def allocate_interface(request):
    admin = Admin.objects.all().first()

    if (admin.phase == 'Allocation'):
        jobs = Job.objects.all()
        interns = Intern.objects.all()


        try:
            intern_preference = intern_preference_dictionary()
            job_preference = job_preference_dictionary()



            if admin.allocation_algorithm == 'Gale Shapely':
            
                allocated_pairs = gale_allocation(
                    intern_preference=intern_preference,
                    job_preference=job_preference,
                )  

                algorithm_context = 'The Gale-Shapley algorithm is a method for pairing interns with their preferred jobs, utilizing both intern and job preferences. The algorithm iteratively matches each intern with their most preferred job whilst considering the preferences of the jobs. This ensures interns are matched with their best possible job in a stable configuration. <a href="https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm" target="_blank">Learn more</a>'

                

            elif admin.allocation_algorithm == 'Hungarian':

                allocated_pairs = hungarian_algorithm(preference=intern_preference)

                algorithm_context = 'The Hungarian algorithm is a technique for pairing interns with their preferred jobs, only using the intern’s preferences. The algorithm optimizes the matching by finding the minimum cost of assigning interns to jobs. It achieves this by iteratively selecting the lowest cost assignment and updates the matching until the optimal is found. <a href=" https://en.wikipedia.org/wiki/Hungarian_algorithm " target="_blank">Learn more</a>'
        
            elif admin.allocation_algorithm == 'Pareto':
    
                allocated_pairs = pareto_optimal(intern_preferences=intern_preference, job_preferences=job_preference)
                
                algorithm_context = 'The Pareto algorithm finds the optimal pairing that satisfies the preferences of both interns and jobs. The algorithm iteratively evaluates the potential intern-job matches and identifying a match where a pairing cannot be improved without worsening any other interns preference. <a href=" https://en.wikipedia.org/wiki/Multi-objective_optimization" target="_blank">Learn more</a>'

            elif admin.allocation_algorithm == 'Random Serial Dictatorship':
                allocated_pairs = random_serial_dictatorship_matching(intern_preference=intern_preference, job_preference=job_preference)

                algorithm_context = 'The Random Serial Dictatorship is an optimal method for pairing interns with jobs, only considering the intern’s preferences. The algorithm randomly selects an intern allowing them to choose their most preferred job. If the job is available, the intern is assigned to the job. If not, the job is removed from consideration and the intern moves on to their next preferred job. <a href=" https://en.wikipedia.org/wiki/Random_priority_item_allocation" target="_blank">Learn more</a>'

         
           
            
            
            #Saves the allocated interns and jobs to the profiles
            
            for pair in allocated_pairs:
                pair[0].allocated_job = pair[1]
                pair[1].allocated_intern = pair[0]
                pair[0].save()
                pair[1].save()
                

            


            data = spread_of_preference(allocated_pairs = allocated_pairs, intern_preference = intern_preference, job_preference = job_preference)
         
            
            rank_pairs = spread_of_preference_pairs(allocated_pairs = allocated_pairs, intern_preference = intern_preference, job_preference = job_preference)


            data_intern_match = percentage_match(1,data)
            data_job_match = percentage_match(2,data)
            data_overall_match = int(((data_intern_match + data_job_match)/2))
            

            form = AdminToggleNotify(instance= admin)
            if request.method == 'POST':
                form = AdminToggleNotify(request.POST, instance= admin)  
                form.save()
           
                return redirect('../../../admin_interface/allocate/')

            allocated_pairs_rank = zip(allocated_pairs,rank_pairs)

            context = {'data': json.dumps(data), 'form':form, 'jobs' :jobs , 'interns' : interns, 'allocated_pairs': allocated_pairs,'allocated_pairs_rank':allocated_pairs_rank,'data_intern_match':data_intern_match, 'data_job_match':data_job_match,'data_overall_match':data_overall_match, 'algorithm_context':algorithm_context,'admin':admin }
            return render(request, 'interface/allocate.html', context)

        except:

            messages.info(request, 'Error - Make sure all Intern preferences are filled in and there are enough Jobs for each Intern')
            return redirect('../../../admin_interface')

    else:
        messages.info(request, 'You must be in the allocate phase to allocate positions')

        return redirect('../../../admin_interface')



#This allocates excel files 
@login_required(login_url='../../../../login')
@allowed_users(allowed_roles=['Admin'])
def allocate_excel(request):
    admin = Admin.objects.all().first()

    


    if "GET" == request.method:
        context = {}
        return render(request, 'interface/allocate_excel.html', context)
    

    else:
        excel_file = request.FILES["excel_file"]

        #Validation of excel file needs to be complete...
        
        
        try:
            workbook = openpyxl.load_workbook(excel_file)
            intern_excel = workbook["intern_preference"]
            job_excel = workbook["job_preference"] 
            intern_preference = excel_preferences(preferences = intern_excel)
            job_preference = excel_preferences(preferences = job_excel)
            preference_number = intern_excel.max_row - 1

            if admin.allocation_algorithm == 'Gale Shapely':
            
                allocated_pairs = gale_allocation(
                    intern_preference=intern_preference,
                    job_preference=job_preference,
                )  

                algorithm_context = 'The Gale-Shapley algorithm is a method for pairing interns with their preferred jobs, utilizing both intern and job preferences. The algorithm iteratively matches each intern with their most preferred job whilst considering the preferences of the jobs. This ensures interns are matched with their best possible job in a stable configuration. <a href="https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm" target="_blank">Learn more</a>'

            elif admin.allocation_algorithm == 'Hungarian':

                allocated_pairs = hungarian_algorithm(preference=intern_preference)

                algorithm_context = 'The Hungarian algorithm is a technique for pairing interns with their preferred jobs, only using the intern’s preferences. The algorithm optimizes the matching by finding the minimum cost of assigning interns to jobs. It achieves this by iteratively selecting the lowest cost assignment and updates the matching until the optimal is found. <a href=" https://en.wikipedia.org/wiki/Hungarian_algorithm " target="_blank">Learn more</a>'
        
            elif admin.allocation_algorithm == 'Pareto':
    
                allocated_pairs = pareto_optimal(intern_preferences=intern_preference, job_preferences=job_preference)
                
                algorithm_context = 'The Pareto algorithm finds the optimal pairing that satisfies the preferences of both interns and jobs. The algorithm iteratively evaluates the potential intern-job matches and identifying a match where a pairing cannot be improved without worsening any other interns preference. <a href=" https://en.wikipedia.org/wiki/Multi-objective_optimization" target="_blank">Learn more</a>'

            elif admin.allocation_algorithm == 'Random Serial Dictatorship':
                allocated_pairs = random_serial_dictatorship_matching(intern_preference=intern_preference, job_preference=job_preference)

                algorithm_context = 'The Random Serial Dictatorship is an optimal method for pairing interns with jobs, only considering the intern’s preferences. The algorithm randomly selects an intern allowing them to choose their most preferred job. If the job is available, the intern is assigned to the job. If not, the job is removed from consideration and the intern moves on to their next preferred job. <a href=" https://en.wikipedia.org/wiki/Random_priority_item_allocation" target="_blank">Learn more</a>'


            
            data = spread_of_preference(allocated_pairs = allocated_pairs, intern_preference = intern_preference, job_preference = job_preference)
            
            data_intern_match = percentage_match(1,data)
            data_job_match = percentage_match(2,data)

            data_overall_match = int(((data_intern_match + data_job_match)/2))



        except:
            messages.error(request, 'Incorrect Format! Please edit and try again')
            return redirect('../../../admin_interface/allocate/excel')

        
        

        context = {'data': json.dumps(data),'allocated_pairs':allocated_pairs, 'intern_preference':intern_preference, 'job_preference': job_preference, 'preference_number' : range(1,preference_number + 1),'data_intern_match':data_intern_match, 'data_job_match':data_job_match,'data_overall_match':data_overall_match, 'algorithm_context':algorithm_context,'admin':admin  }
        return render(request, 'interface/allocate_excel.html', context)
