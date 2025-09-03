from django.shortcuts import render
from .forms import FacebookPostForm
import requests





def home(request):

    return render(request, 'home.html')




def facebook_post_view(request):
    message_sent = False
    error = None

    if request.method == 'POST':
        form = FacebookPostForm(request.POST, request.FILES)
        if form.is_valid():
            token = form.cleaned_data['token']
            message = form.cleaned_data['message']
            img_file = request.FILES.get('img')

            url = f'https://graph.facebook.com/me/photos'
            params = {
                'caption': message,
                'access_token': token,
            }

            if img_file:
                files = {
                    'source': img_file,
                }
                response = requests.post(url, data=params, files=files)

            else:
                error = "Please Choose Photo"
                response = None

            if response:
                result = response.json()
                if 'id' in result:
                    message_sent = True
                else:
                    error = result.get('error', {}).get('message', 'Error')
    else:
        form = FacebookPostForm()

    return render(request, 'facebook/facebook_post.html', {
        'form': form,
        'message_sent': message_sent,
        'error': error,
    })
