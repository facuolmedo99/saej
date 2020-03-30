from django.shortcuts import redirect
from django.http import HttpResponse

def no_auth_user(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/home/')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

def allowed_user(allowed_roles = ['administrador']):
    def decorator(view_function):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request,*args,**kwargs)
            else:
                 return HttpResponse('No tienes permiso para entrar a esta seccion')
            
        return wrapper_func
    return decorator

def solo_admin(view_function):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'admin':
            return view_function(request,*args,**kwargs)
        if group == 'parte':
            return redirect('/home/')
        if group == 'mediador':
            return view_function(request,*args,**kwargs)

    return wrapper_func