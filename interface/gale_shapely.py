from collections import deque

#formula run here
def pref_rank(pref):
    #Need to return preference and rank

    pref_rank = {}

    for intern, intern_preference in pref.items():

        pref_rank.update({intern: {job: rank for rank, job in enumerate(intern_preference)}})

    return pref_rank
    


def gale_allocation(*, intern_set, job_set, intern_preference, job_preference):
    
    job_rank = pref_rank(job_preference)
    print(str(job_rank))

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
