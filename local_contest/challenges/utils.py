from .models import CustomUser, Performance

def calculate_score(user):

        parameter_mapping = {'Alpha': 1, 'Beta': 2, 'Gamma': 3, 'Omega': 4}
        level_mapping = {'Level1': 1, 'Level2': 2, 'Level3': 3, 'Level4': 4, 'Level5': 5, 'Level6': 6, 'Level7': 7, 'Level8': 8, 'Level9': 9, 'Level10': 10}
        
        total_score = 0
        performances = Performance.objects.filter(user=user, solved=True)
        for performance in performances:
            defined_file_category = performance.definedfile.level.challenge.category
            defined_file_level = performance.definedfile.level.name
            parameter = parameter_mapping.get(defined_file_category, 0)
            level = level_mapping.get(defined_file_level, 0)
            total_score += parameter * level

        return total_score

def calculate_rank(user):
    user_score = user.score
    total_user = CustomUser.objects.all().count()
    higher_scores = CustomUser.objects.filter(score__gt=user_score).count()
    same_scores = CustomUser.objects.filter(score=user_score).count()
    # print("Higher_scores than you :", higher_scores)
    # print("Same_scores as you, you included : ", same_scores)
    rank = higher_scores + same_scores 
    if rank == 0:
         rank = CustomUser.objects.all().count()
    return (rank, total_user)

def update_ranks():
    users = CustomUser.objects.all()
    for user in users:
        user.rank = calculate_rank(user)[0]
        user.save(update_fields=['rank'])

def update_score(user):
    user.score = calculate_score(user)
    user.save(update_fields=['score'])