from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from uuid import uuid4
import random
import time


@login_required
def demo_pages(request):
    context = {
        'divClass': ' a'.join(str(uuid4()).split('-')),
        'divId': str(uuid4()),
        'inpClass': ' a'.join(str(uuid4()).split('-')),
        'inpId': str(uuid4()),
        'wraps': range(random.randint(1, 5))
    }
    return render(request, 'demoPages.html', context=context)


@login_required
def demo_controls(request):
    context = {
        'divClass': ' a'.join(str(uuid4()).split('-')),
        'divId': str(uuid4()),
        'inpClass': ' a'.join(str(uuid4()).split('-')),
        'inpId': str(uuid4()),
        'wraps': range(random.randint(1, 5))
    }
    return render(request, 'demoControls.html', context=context)


@login_required
def wait_page(request):
    try:
        wait_time = int(request.GET.get('time'))
        if wait_time < 1 or wait_time > 100:
            return render(request, 'wait.html', status=400, context={'status': 'time not in range 1-100'})
    except ValueError:
        return render(request, 'wait.html', status=400, context={'status': 'time not int'})
    time.sleep(wait_time)
    return render(request, 'wait.html', context={'status': f'ok after {wait_time}'})


@login_required
def wait_ajax(request):
    try:
        wait_time = request.GET.get('time')
        hidden = request.GET.get('hidden')
        if hidden is None or hidden != 'y':
            wait_time = int(wait_time)
            if wait_time < 1 or wait_time > 10:
                return render(request, 'ajax.html', status=400, context={'status': 'time not in range 1-10'})
            return render(request, 'ajax.html', context={'status': f'ok',
                                                         'times': wait_time})
        else:
            time.sleep(1)
            return JsonResponse(data={'status': 'ok'}, status=200)
    except ValueError:
        return render(request, 'ajax.html', status=400, context={'status': 'time not int'})


@login_required
def crash(request):
    raise Exception(f'you crashed this site,  {request.user.username}')


@login_required
def test_location(request):
    return render(request, 'location.html', context={'status': 'ok'})
