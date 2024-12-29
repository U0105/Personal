from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {'full_name':'Hossein Abbasi'}
    return render(request,'website/index.html',context)

def contact_view(request):
    context = {'Phone':'+98 916 031 8705',
               'City':'Golestan 1 , Omidiyeh Khuzestan , Iran',
               'Email':'hosseinabbasi80.ha@gmail.com'}
    return render(request,'website/contact.html',context)

def about_view(request):
    context = {'Birthday':'25 March 2001',
               'Website':'https://github.com/U0105/Personal',
               'Phone':'+98 916 031 8705',
               'City':'Omidiyeh , Iran',
               'Age':'23',
               'Degree':'Diploma',
               'Email':'hosseinabbasi80.ha@gmail.com',
               'Freelance':'Available'}
    return render(request,'website/about.html',context)