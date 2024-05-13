from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Hall_of_Fame, Event, Resources,Job
from .forms import ClubForm, HallOfFameForm, EventForm, ResourcesForm, JobForm
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'features/home.html')
 
def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'features/club_list.html', {'clubs': clubs})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request, 'features/club_detail.html', {'club': club})

def club_create(request):
    # if request.method == 'POST':
    #     form = ClubForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('club_list')
    if request.method == 'POST':
        form = ClubForm(request.POST or None)
        if form.is_valid():
            club = form.save(commit=False)
            club.added_by = request.user
            club.save()
            return redirect('features:club_list')
    else:
        form = ClubForm()
    return render(request, 'features/club_form.html', {'form': form})

def club_update(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('features:club_list')
    else:
        form = ClubForm(instance=club)
    return render(request, 'features/club_form.html', {'form': form})

def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        club.delete()
        return redirect('features:club_list')
    return render(request, 'features/club_confirm_delete.html', {'club': club})

# CRUD operations for Hall_of_Fame model
def hall_of_fame_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    hall_of_fame = Hall_of_Fame.objects.all()
    return render(request, 'features/hall_of_fame_list.html', {'hall_of_fame': hall_of_fame})

def hall_of_fame_detail(request, pk):
    entry = get_object_or_404(Hall_of_Fame, pk=pk)
    return render(request, 'features/hall_of_fame_detail.html', {'entry': entry})

def hall_of_fame_create(request):
    # if request.method == 'POST':
    #     form = HallOfFameForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('hall_of_fame_list')
    if request.method == 'POST':
        form = HallOfFameForm(request.POST or None)
        if form.is_valid():
            hall_of_fame = form.save(commit=False)
            hall_of_fame.added_by = request.user
            hall_of_fame.save()
            return redirect('features:hall_of_fame_list')
    else:
        form = HallOfFameForm()
    return render(request, 'features/hall_of_fame_form.html', {'form': form})

def hall_of_fame_update(request, pk):
    hall_of_fame_entry = get_object_or_404(Hall_of_Fame, pk=pk)
    if request.method == 'POST':
        form = HallOfFameForm(request.POST, instance=hall_of_fame_entry)
        if form.is_valid():
            form.save()
            return redirect('features:hall_of_fame_list')
    else:
        form = HallOfFameForm(instance=hall_of_fame_entry)
    return render(request, 'features/hall_of_fame_form.html', {'form': form})

def hall_of_fame_delete(request, pk):
    hall_of_fame_entry = get_object_or_404(Hall_of_Fame, pk=pk)
    if request.method == 'POST':
        hall_of_fame_entry.delete()
        return redirect('features:hall_of_fame_list')
    return render(request, 'features/hall_of_fame_confirm_delete.html', {'hall_of_fame_entry': hall_of_fame_entry})

# CRUD operations for Event model
def event_list(request):
    events = Event.objects.all()
    return render(request, 'features/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'features/event_detail.html', {'event': event})

def event_create(request):
    # if request.method == 'POST':
    #     form = EventForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('event_list')
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.added_by = request.user
            event.save()
            return redirect('features:event_list')
    else:
        form = EventForm()
    return render(request, 'features/event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('features:event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'features/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('features:event_list')
    return render(request, 'features/event_confirm_delete.html', {'event': event})

# CRUD operations for Resources model
def resources_list(request):
    resources = Resources.objects.all()
    return render(request, 'features/resources_list.html', {'resources': resources})

def resources_detail(request, pk):
    resource = get_object_or_404(Resources, pk=pk)
    return render(request, 'features/resources_detail.html', {'resource': resource})

def resources_create(request):
    # if request.method == 'POST':
    #     form = ResourcesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('resources_list')
    if request.method == 'POST':
        # form = ResourcesForm(request.POST or None, user=request.user)
        form = ResourcesForm(request.POST or None, request.FILES)
        if form.is_valid():
            resources = form.save(commit=False)
            resources.added_by = request.user
            resources.save()
            return redirect('features:resources_list')
    else:
        form = ResourcesForm()
    return render(request, 'features/resources_form.html', {'form': form})

def resources_update(request, pk):
    resource = get_object_or_404(Resources, pk=pk)
    if request.method == 'POST':
        form = ResourcesForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('features:resources_list')
    else:
        form = ResourcesForm(instance=resource)
    return render(request, 'features/resources_form.html', {'form': form})

def resources_delete(request, pk):
    resource = get_object_or_404(Resources, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('features:resources_list')
    return render(request, 'features/resources_confirm_delete.html', {'resource': resource})

# Jobs
def job_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    jobs = Job.objects.all()
    return render(request, 'features/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'features/job_detail.html', {'job': job})


def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST or None)
        if form.is_valid():
            job = form.save(commit=False)
            job.added_by = request.user
            job.save()
            return redirect('features:job_list')
    else:
        form = JobForm()
    return render(request, 'features/job_form.html', {'form': form})

def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('features:job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'features/job_form.html', {'form': form})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('features:job_list')
    return render(request, 'features/job_confirm_delete.html',{'job':job})