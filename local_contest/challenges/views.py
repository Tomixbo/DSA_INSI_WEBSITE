from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import DefinedFile, Challenge, Level, Performance

from django.contrib.auth.decorators import login_required
from .utils import calculate_rank, calculate_score, update_ranks, update_score


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


@login_required
def challenge_detail(request, challenge_slug=None):
    update_ranks()
    user = request.user  # Obtenez l'utilisateur actuel
    rank, total_user = calculate_rank(user)
    if challenge_slug:
        defined_files = DefinedFile.objects.filter(level__challenge__slug=challenge_slug)
        test_results = {defined_file.id : defined_file.get_test_result_for_user(request) for defined_file in defined_files}
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
                            performance = Performance.objects.create(user=user, definedfile=defined_file, solved=True)
                            result = 'VALID'
                            # print("Your score : ",calculate_score(user))
                            rank, total_user = calculate_rank(user)
                            # print("Your rank : ", rank, " sur ", total_user)
                            update_score(user)
                            update_ranks()
                        else:
                            result = 'INVALID'

                    except DefinedFile.DoesNotExist:
                        result = f'INVALID (No defined file named {defined_file_name} found for challenge : {challenge.name})'
                    
                    
                else:
                    result = 'INVALID (No defined file name provided)'
            
            else:
                result = 'INVALID (No file uploaded)'
            return JsonResponse({'result': result})

        return render(request, 'challenge_detail.html', {'defined_files': defined_files, 'challenge': challenge, 'levels': levels, 'user': user, 'test_results': test_results, 'total_user': total_user})

    # Handle case when challenge name is not provided
    else:
        # Add logic here if needed
        return render(request, 'challenge_list.html', {'challenges': Challenge.objects.all(), 'user': user, 'total_user': total_user})

@login_required
def challenge_list(request):
    update_ranks()
    user = request.user
    challenges = Challenge.objects.filter(published=True)
    rank, total_user = calculate_rank(user)
    return render(request, 'challenge_list.html', {'challenges': challenges, 'total_user': total_user})


def get_user_rank(request, challenge_slug):
    user = request.user
    rank, total_user = calculate_rank(user)
    score = calculate_score(user)
    return JsonResponse({'rank': rank, 'total_user': total_user, 'score': score})