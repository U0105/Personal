from django.shortcuts import render

# Create your views here.
def resume_view(request):
    context = {'FileAnalyzer':'https://github.com/U0105/FileAnalyzer',
               'MyWebsite':'https://github.com/U0105/Personal',}
    return render(request,'resume/resume.html',context)