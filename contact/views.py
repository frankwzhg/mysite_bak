from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.mail import send_mail
from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@hotmail.com_'),
                ['siteowner@hotmail.com_']

            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site!'}
            )
    return render_to_response('contact_form.html', {'form': form})

