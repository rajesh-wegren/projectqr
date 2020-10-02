from django.shortcuts import render
from qrcodeapp.models import Qrcode
from qrcodeapp.forms import QrForm


# Create your views here.
def home_page(request):
    return render(request=request, template_name='qrcodeapp/homepage.html')


def qr_data(request):
    qr_form = QrForm()
    if request.method == 'GET':

        if request.method == 'POST':
            form_data = QrForm(request.POST)
            if form_data.is_valid():
                form_data.save(commit=True)

    if request.method == "POST":
        form_data = QrForm(request.POST)
        if form_data.is_valid():
            # print(f'user_url:{form_data.cleaned_data["user_url"]}')
            print('user_url:', form_data.cleaned_data['user_url'])

            form_data.save(commit=True)

    my_dict = {'qr_form': qr_form}

    return render(request=request, template_name='qrcodeapp/qrcreate.html', context=my_dict)

    # form=QrForm()
    # my_dict={'form': form}
    # return render(request=request, template_name='qrcodeapp/qrcreate.html',context=my_dict)

    # if request.method == 'POST':
    #     form = QrForm(request.POST)
    #     my_dict = {'form': form}
    #     if form.is_valid():
    #         # print(' Enterted  the Qr code')
    #         print('user_url:', form.cleaned_data['user_url'])
    #         form.save(commit=True)
    #
    # return render(request=request, template_name='qrcodeapp/qrcreate.html', context=my_dict)
