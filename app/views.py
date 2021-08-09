from django.shortcuts import render, redirect
import random
import time

def index(request):
    return render(request, 'index.html')

def juego(request):
        if request.POST['opcion'] == 'granja':
            numeroazar = random.randint(10, 20)
        
        if request.POST['opcion'] == 'cueva':
            numeroazar = random.randint(5, 10)
    
        if request.POST['opcion'] == 'casa':
            numeroazar = random.randint(2, 5)
        
        if request.POST['opcion'] == 'casino':
            numeroazar = random.randint(0, 50)
            operacion = random.randint(1, 2)
            if operacion == 1:
                numeroazar = numeroazar * 1
            else:
                numeroazar = numeroazar * -1

        if 'contador' in request.session:
            request.session['contador'] = request.session['contador'] + numeroazar
        else:
            request.session['contador'] = numeroazar 
            
        if not ('log' in request.session):
            request.session['log'] = []

        if 'prueba' in request.session:
            request.session['prueba'] = request.session['prueba'] + 1
        else:
            request.session['prueba'] = 1

        informacion_a_entregar = {
            
            'jugada'    : request.session['prueba'],
            'monedas'   : numeroazar,
            'ubicacion' : request.POST['opcion'],
            'total'     : request.session['contador'],
            'palabra'   : 'ganado' if numeroazar > 0 else 'perdido',
            'color'     : 'verde' if numeroazar > 0 else 'rojo',
            'fecha'     : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        }

        request.session['log'].append(informacion_a_entregar)
        request.session.save()
        print(request.POST)
        return redirect('/')

def reset(request):
    if 'contador' and 'log' and 'prueba' in request.session:
        del request.session['contador']
        del request.session['log']
        del request.session['prueba']
        print(request.POST)
    return redirect('/')

