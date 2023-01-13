from collections import deque
from hungarian_algorithm import algorithm

#formula run here
def pref_rank(pref):
    #Need to return preference and rank

    pref_rank = {}

    for intern, intern_preference in pref.items():
        
        #Creates a rank for each of the jobs and interns
        pref_rank.update({intern: {job: (rank+1) for rank, job in enumerate(intern_preference)}})

    return pref_rank
    

def gale_allocation(*, intern_preference, job_preference):
    
    job_rank = pref_rank(job_preference)


    intern_set = list(intern_preference.keys())
    job_set = list(job_preference.keys())
    
    
    
    #create a deque for the iterate list.. this will get apprended to and deleted and remove items in the list
    iterate_list ={}
    for intern, jobs in intern_preference.items():

        #using deques to improve efficiency
        iterate_list.update({intern: deque(jobs)})


    #final pairings
    pair = {}

    interns_left = set(intern_set)

    while len(interns_left) > 0:

        #iterates through interns left and pops
        intern = interns_left.pop()
       
        job = iterate_list[intern].popleft()

        #Searches if the job is in the pair
        if job not in pair:

            #allocates job to pair
            pair[job] = intern
        

        else:
            intern0 = pair[job]
            job_intern = job_rank[job][intern0] < job_rank[job][intern]
            if job_intern:

                #if the rank is lower then the rank in the pair then add to the list else add the current intern
                interns_left.add(intern)
            else:
                interns_left.add(intern0)
                pair[job] = intern
    
    #Return pair of iterns and jobs... 
    return [(intern, job) for job, intern in pair.items()]


#https://github.com/benchaplin/hungarian-algorithm
def hungarian_algorithm(preference):



    preference_rank = pref_rank(preference)
    
    matches_ranking = algorithm.find_matching(preference_rank, matching_type = 'min', return_type = 'list' )

    matches = [match[0] for match in matches_ranking]
    
    return matches


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
