from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *



#This function creates job preferences for interns based off skills
def job_preference_dictionary():
    #create a preference dictionary "job": ["intern","intern","intern"]
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    jobs_dictionary = {}

    for job in jobs:
        job_dictionary = {}
        computing_skills_job = job.computing_skills.all()
        analytic_skills_job = job.analytic_skills.all()
        marketing_skills_job = job.marketing_skills.all()
        management_skills_job = job.management_skills.all()
        leadership_skills_job = job.leadership_skills.all()
        business_skills_job = job.business_skills.all()
        admin_skills_job = job.admin_skills.all()


        #print("Job: "+ str(job.name))

        for intern in interns:
            computing_skills_intern = intern.computing_skills.all()
            analytic_skills_intern = intern.analytic_skills.all()
            marketing_skills_intern = intern.marketing_skills.all()
            management_skills_intern = intern.management_skills.all()
            leadership_skills_intern = intern.leadership_skills.all()
            business_skills_intern = intern.business_skills.all()
            admin_skills_intern = intern.admin_skills.all()

            #skill_difference1 = abs(job.coding - intern.coding) + abs(job.project_management - intern.project_management) + abs(job.marketing1_skills - intern.marketing1_skills) + abs(job.web_skills - intern.web_skills)
            # save the skill difference with each of the jobs. if a job has a higher skill difference add to the end 
            #

            #Similarites in skill 
            skill_difference = len(list(set(computing_skills_job).intersection(computing_skills_intern)))
            skill_difference += len(list(set(analytic_skills_job).intersection(analytic_skills_intern)))
            skill_difference += len(list(set(marketing_skills_job).intersection(marketing_skills_intern)))
            skill_difference += len(list(set(management_skills_job).intersection(management_skills_intern)))
            skill_difference += len(list(set(leadership_skills_job).intersection(leadership_skills_intern)))
            skill_difference += len(list(set(business_skills_job).intersection(business_skills_intern)))
            skill_difference += len(list(set(admin_skills_job).intersection(admin_skills_intern)))

            #print(" intern: " + str(intern.name))

            #print("     similarities: " + str(skill_difference))
            

            #Take the 

            #print("job skills : " + str(computing_skills_job) + " intern skills: " + str(computing_skills_intern))


            job_dictionary[intern] = skill_difference
            #print(" The intern: " + str(intern.name))
            #print(" Skill difference: " + str(skill_difference))
        
        


        #{<Intern: Intern2>: 6, <Intern: Intern1>: 6, <Intern: Intern7>: 10, <Intern: Test5>: 3, <Intern: Test3>: 18} sorts that into higher and lower
        
        #job_dictionary = sorted(job_dictionary.items(), key=lambda x:x[1])

        #Now reverses the list to get the intern with the most similar skills
        
        job_dictionary = sorted(job_dictionary.items(), key=lambda x:x[1], reverse=True)
        


        job_dictionary = dict(job_dictionary)
        intern_list = list(job_dictionary.keys())

        job_dictionary.clear()

        jobs_dictionary[job] = intern_list
    
        

    return jobs_dictionary








#This function creates a dictionary for the interns
def intern_preference_dictionary():
     #create a preference dictionary "intern": ["job","job","job"]

    jobs = Job.objects.all()
    interns = Intern.objects.all()

    interns_dictionary = {}
    for intern in interns:
        intern_dictionary = {}
        preferences = intern.internpreference_set.all()
        for preference in preferences:

            
            intern_dictionary[preference.job] = preference.preference

        intern_dictionary = sorted(intern_dictionary.items(), key=lambda x:x[1])
        intern_dictionary = dict(intern_dictionary)
        job_list = list(intern_dictionary.keys())

        interns_dictionary[intern] = job_list

    #print(interns_dictionary)

    return interns_dictionary




def excel_preferences(preferences):

        preferences_dictionary = {}
        for j in range(2, preferences.max_column + 1):
            row_data = list()
            for number, i in enumerate(range(1, preferences.max_row + 1)):
                
                cell_obj = preferences.cell(row = i, column = j)
                if number == 0:
                    #If first row forget... this will be added later as the primary key
                    continue
                else:
                    row_data.append(str(cell_obj.value))
                
            cell_obj = preferences.cell(row = 1, column = j)
            preferences_dictionary[cell_obj.value] = row_data

        return preferences_dictionary

def excel_set(model):
    model_list = list()
    for j in range(2, model.max_column + 1):
        cell_obj = model.cell(row = 1, column = j)
        model_list.append(str(cell_obj.value))
    return model_list
   
    

def spread_of_preference(allocated_pairs, intern_preference, job_preference):
    
    all_jobs_count = Job.objects.all()
    all_intern_count = Intern.objects.all()

    pref_ranking = []
    i = 0
    if (all_intern_count.count() < all_jobs_count.count()):

        while i < all_jobs_count.count():
            i += 1
            list = [i,0,0]
            pref_ranking.append(list)

    else:
        
        while i < all_intern_count.count():
            i += 1
            list = [i,0,0]
            pref_ranking.append(list)





    #[(<Intern: Intern1>, <Job: Digital degree>), (<Intern: Test>, <Job: TPO>), (<Intern: Test1>, <Job: Manager Testing Job>)]
    for pair in allocated_pairs:
        for intern, jobs in intern_preference.items():
            
            if pair[0] == intern:
            
                for count,data in enumerate(pref_ranking):
                    

                    if pair[1] == jobs[count]:
                        
                        data = pref_ranking[count][1]
                        data += 1
                        pref_ranking[count][1] = data


    for pair in allocated_pairs:
        for job, interns in job_preference.items():        
            if pair[1] == job:
                i=0
                while i < Intern.objects.all().count():
                                       
                    if pair[0] == interns[i]:
 
                        data = pref_ranking[i][2]
                        data += 1
                        pref_ranking[i][2] = data
                    
                    i += 1

                
                    
    return pref_ranking       
             
                    

               


                 
                
                
            