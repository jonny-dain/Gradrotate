import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import Admin



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:


                
                return view_func(request, *arg, **kwargs)
            else:
                if group == 'Admin':
                    return redirect('../../admin_interface')
                
                if group == 'Manager':
                    return redirect('../form/manager_dashboard')
                
                if group == 'Intern':
                    return redirect('../form/student_form')
                else:
                    return HttpResponse('You are not authorized to view this page')
                
        return wrapper_func
    return decorator



def update_progress(progress):
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'Intern':
                    if request.user.intern.progress < progress:
                        request.user.intern.progress = progress
                        request.user.intern.save()

              
            return view_func(request, *arg, **kwargs)
            
        return wrapper_func
    return decorator




def update_phase(view_func):
    def wrapper_func(request, *arg, **kwargs):
        admin = Admin.objects.all().first()
        if (admin.automate_phase == True):
            default=datetime.date.today()
            
            if (default >= admin.allocation_creation_date):
                admin.phase = 'Allocation'

            elif (default >= admin.intern_creation_date):
                admin.phase = 'Intern collection'
            
            else:
                admin.phase = 'Job creation'
                
            admin.save()


        return view_func(request, *arg, **kwargs)
    return wrapper_func






#Ensures the User stays in the phase forms - If they try and use the URL Bar
def required_phase(phase=[]):
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):
            admin = Admin.objects.all().first()

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name


            if admin.phase in phase:
                return view_func(request, *arg, **kwargs)
            else:
                if admin.phase == 'Allocation':

                    if group == 'Manager':
                        return redirect('../../../../form/manager_form/allocation/complete')
                    if group == 'Intern':
                        return redirect('../../../../form/student_form/allocation/complete')
                
                    

        return wrapper_func
    return decorator
    




