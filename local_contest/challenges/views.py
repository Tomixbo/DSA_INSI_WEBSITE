from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import DefinedFile, Challenge, Level

def fetch_defined_files(request, challenge_slug):
    if request.method == 'GET':
        # Retrieve challenge based on the challenge_slug
        challenge = get_object_or_404(Challenge, slug=challenge_slug)
        level_id = request.GET.get('level_id')
        defined_files = DefinedFile.objects.filter(level__challenge=challenge, level_id=level_id)
        form_html = render_to_string('defined_file_form.html', {'defined_files': defined_files})
        return JsonResponse({'form_html': form_html})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def challenge_detail(request, challenge_slug=None):
    if challenge_slug:
        defined_files = DefinedFile.objects.filter(level__challenge__slug=challenge_slug)
        challenge = get_object_or_404(Challenge, slug=challenge_slug)
        levels = Level.objects.filter(challenge=challenge)
        result = 'Upload your file first'
        if request.method == 'POST' :
            
            uploaded_file = request.FILES.get('uploaded_file')
            if uploaded_file:
                uploaded_content = uploaded_file.read().decode('utf-8')

                defined_file_name = request.POST.get('defined_file_name', None)

                if defined_file_name:
                    try:
                        defined_file = DefinedFile.objects.get(name=defined_file_name, level__challenge__name=challenge.name)
                        defined_content = defined_file.output_file.read().decode('utf-8')

                        if uploaded_content == defined_content:
                            result = 'VALID'
                        else:
                            result = 'INVALID'

                    except DefinedFile.DoesNotExist:
                        result = f'INVALID (No defined file named {defined_file_name} found for challenge : {challenge.name})'
                    
                    
                else:
                    result = 'INVALID (No defined file name provided)'
            
            else:
                result = 'INVALID (No file uploaded)'
            return JsonResponse({'result': result})

        return render(request, 'challenge_detail.html', {'defined_files': defined_files, 'challenge': challenge, 'levels': levels})

    # Handle case when challenge name is not provided
    else:
        # Add logic here if needed
        return render(request, 'challenge_list.html', {'challenges': Challenge.objects.all()})

def challenge_list(request):
    challenges = Challenge.objects.filter(published=True)
    return render(request, 'challenge_list.html', {'challenges': challenges})
