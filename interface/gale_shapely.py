from collections import deque
from hungarian_algorithm import algorithm

#formula run here to get every preference number with each job/intern
def pref_rank(pref):
    #Need to return preference and rank

    pref_rank = {}

    for intern, intern_preference in pref.items():
        
        #Creates a rank for each of the jobs and interns
        pref_rank.update({intern: {job: (rank+1) for rank, job in enumerate(intern_preference)}})

    return pref_rank
    
#Gale-Shapely algorithm
def gale_allocation(*, intern_preference, job_preference):
    
    pair = {}
    job_rank = pref_rank(job_preference)
    intern_set = list(intern_preference.keys())
    
    
    

    iterate_list ={}
    for intern, jobs in intern_preference.items():

        #using deques to improve efficiency
        iterate_list.update({intern: deque(jobs)})
    

    interns_left = set(intern_set)

    while len(interns_left) > 0:



        intern = interns_left.pop()
       
        job = iterate_list[intern].popleft()
 

        #Searches if the job is in the pair
        if job not in pair:

            #allocates job to pair
            pair[job] = intern
        

        else:
            intern0 = pair[job]
            job_intern_rank = job_rank[job][intern0] < job_rank[job][intern]
            
            if job_intern_rank == True:


                interns_left.add(intern)
            else:
                interns_left.add(intern0)
                pair[job] = intern
    

    return [(intern, job) for job, intern in pair.items()]

#Hungarian algorithm
#https://github.com/benchaplin/hungarian-algorithm
def hungarian_algorithm(preference):
   
    preference_rank = pref_rank(preference)
    matches_ranking = algorithm.find_matching(preference_rank, matching_type = 'min', return_type = 'list' )
    matches = [match[0] for match in matches_ranking]
    return matches

#Pareto algorithm
def pareto_optimal(intern_preferences, job_preferences):

    
   
    matching = []

    free_interns = set(intern_preferences.keys())
    free_jobs = set(job_preferences.keys())

    
    intern_order = list(intern_preferences.keys())
    
    for intern in intern_order:
        # Find the job that the intern most prefers among the free jobs
        preferred_jobs = intern_preferences[intern]
        for job in preferred_jobs:
            if job in free_jobs:
                
                matching.append((intern, job))
                free_interns.remove(intern)
                free_jobs.remove(job)
                break


    return matching

#Random Serial Dictatorship algorithm
def random_serial_dictatorship_matching(intern_preference, job_preference):
    interns = list(intern_preference.keys())
    jobs = list(job_preference.keys())
    matches = []
    for i in range(len(interns)):
        preferences = intern_preference[interns[i]]
        for j in range(len(preferences)):
            if preferences[j] in jobs:
                job = preferences[j]
                jobs.remove(job)
                matches.append((interns[i], job))
                break
    return matches





