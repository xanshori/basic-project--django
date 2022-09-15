from . models import Profile
def searchprofile(request):
    search_query = ''
    if request.GET.get('search'):
        search_query =request.GET.get('search')
    profiles = Profile.objects.filter(name__icontains=search_query)
    return search_query,profiles