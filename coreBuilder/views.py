from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Resumes
from .pdf import html2pdf
from django.http import HttpResponse

@login_required
def resumeForm(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        mobileNumber = request.POST.get('mobileNumber')
        email = request.POST.get('email')
        portfolioLink = request.POST.get('portfolioLink')
        linkedinLink = request.POST.get('linkedinLink')
        summary = request.POST.get('summary')
        collegeName = request.POST.get('collegeName')
        collegeBranch = request.POST.get('collegeBranch')
        collegeLocation = request.POST.get('collegeLocation')
        collegeStart = request.POST.get('collegeStart')
        collegeEnd = request.POST.get('collegeEnd')
        collegeAchivements = request.POST.get('collegeAchivements')
        skillsTechnical = request.POST.get('skillsTechnical')
        skillsTools = request.POST.get('skillsTools')
        certificate1 = request.POST.get('certificate1')
        certificate1Link = request.POST.get('certificate1Link')
        certificate2 = request.POST.get('certificate2')
        certificate2Link = request.POST.get('certificate2Link')
        companyName = request.POST.get('companyName')
        companyLocation = request.POST.get('companyLocation')
        companyPosition = request.POST.get('companyPosition')
        companyStart = request.POST.get('companyStart')
        companyEnd = request.POST.get('companyEnd')
        companyWorkDescription = request.POST.get('companyWorkDescription')
        projectName = request.POST.get('projectName')
        projectTime = request.POST.get('projectTime')
        projectHowYouSolved = request.POST.get('projectHowYouSolved')
        projectToolsUsed = request.POST.get('projectToolsUsed')
        achievements = request.POST.get('achievements')

        data={
            'firstName':firstName,
            'lastName':lastName,
            'mobileNumber':mobileNumber,
            'email':email,
            'portfolioLink':portfolioLink,
            'linkedinLink':linkedinLink,
            'summary':summary,
            'collegeName':collegeName,
            'collegeBranch':collegeBranch,
            'collegeLocation':collegeLocation,
            'collegeStart':collegeStart,
            'collegeEnd':collegeEnd,
            'collegeAchivements'  : collegeAchivements,
            'skillsTechnical':skillsTechnical,
            'skillsTools':skillsTools,
            'certificate1':certificate1,
            'certificate1Link':certificate1Link,
            'certificate2':certificate2,
            'certificate2Link':certificate2Link,
            'companyName':companyName,
            'companyLocation':companyLocation,
            'companyPosition':companyPosition,
            'companyStart':companyStart,
            'companyEnd':companyEnd,
            'companyWorkDescription':companyWorkDescription,
            'projectName':projectName,
            'projectTime':projectTime,
            'projectHowYouSolved':projectHowYouSolved,
            'projectToolsUsed':projectToolsUsed,
            'achievements':achievements
        }
        return render(request,'resume_html.html',{'data':data})
    return render(request, 'resumeForm.html')

@login_required
def saveResume(request):
    if request.method == "POST":
        user = request.user
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        mobileNumber = request.POST.get('mobileNumber')
        email = request.POST.get('email')
        portfolioLink = request.POST.get('portfolioLink')
        linkedinLink = request.POST.get('linkedinLink')
        summary = request.POST.get('summary')
        collegeName = request.POST.get('collegeName')
        collegeBranch = request.POST.get('collegeBranch')
        collegeLocation = request.POST.get('collegeLocation')
        collegeStart = request.POST.get('collegeStart')
        collegeEnd = request.POST.get('collegeEnd')
        collegeAchivements = request.POST.get('collegeAchivements')
        skillsTechnical = request.POST.get('skillsTechnical')
        skillsTools = request.POST.get('skillsTools')
        certificate1 = request.POST.get('certificate1')
        certificate1Link = request.POST.get('certificate1Link')
        certificate2 = request.POST.get('certificate2')
        certificate2Link = request.POST.get('certificate2Link')
        companyName = request.POST.get('companyName')
        companyLocation = request.POST.get('companyLocation')
        companyPosition = request.POST.get('companyPosition')
        companyStart = request.POST.get('companyStart')
        companyEnd = request.POST.get('companyEnd')
        companyWorkDescription = request.POST.get('companyWorkDescription')
        projectName = request.POST.get('projectName')
        projectTime = request.POST.get('projectTime')
        projectHowYouSolved = request.POST.get('projectHowYouSolved')
        projectToolsUsed = request.POST.get('projectToolsUsed')
        achievements = request.POST.get('achievements')

        r= Resumes()

        r.user = user
        r.firstName= firstName
        r.lastName = lastName
        r.mobileNumber = mobileNumber
        r.email = email
        r.portfolioLink = portfolioLink
        r.linkedinLink = linkedinLink
        r.summary = summary
        r.collegeName = collegeName
        r.collegeBranch = collegeBranch
        r.collegeLocation = collegeLocation
        r.collegeStart = collegeStart
        r.collegeEnd = collegeEnd
        r.collegeAchivements = collegeAchivements
        r.skillsTechnical = skillsTechnical
        r.skillsTools = skillsTools
        r.certificate1 = certificate1
        r.certificate1Link = certificate1Link
        r.certificate2 = certificate2
        r.certificate2Link = certificate2Link
        r.companyName = companyName
        r.companyLocation = companyLocation
        r.companyPosition = companyPosition
        r.companyStart = companyStart
        r.companyEnd = companyEnd
        r.companyWorkDescription = companyWorkDescription
        r.projectName = projectName
        r.projectTime = projectTime
        r.projectHowYouSolved = projectHowYouSolved
        r.projectToolsUsed = projectToolsUsed
        r.achievements = achievements
        r.save()
        return redirect('myResumes')
    return redirect('myResumes')

@login_required
def myResumes(request):
    user = request.user
    resumes = Resumes.objects.filter(user=user)
    return render(request,'myResumes.html',{'resumes':resumes})

@login_required
def editResume(request, id):
    resume = Resumes.objects.get(id=id)
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        mobileNumber = request.POST.get('mobileNumber')
        email = request.POST.get('email')
        portfolioLink = request.POST.get('portfolioLink')
        linkedinLink = request.POST.get('linkedinLink')
        summary = request.POST.get('summary')
        collegeName = request.POST.get('collegeName')
        collegeBranch = request.POST.get('collegeBranch')
        collegeLocation = request.POST.get('collegeLocation')
        collegeStart = request.POST.get('collegeStart')
        collegeEnd = request.POST.get('collegeEnd')
        collegeAchivements = request.POST.get('collegeAchivements')
        skillsTechnical = request.POST.get('skillsTechnical')
        skillsTools = request.POST.get('skillsTools')
        certificate1 = request.POST.get('certificate1')
        certificate1Link = request.POST.get('certificate1Link')
        certificate2 = request.POST.get('certificate2')
        certificate2Link = request.POST.get('certificate2Link')
        companyName = request.POST.get('companyName')
        companyLocation = request.POST.get('companyLocation')
        companyPosition = request.POST.get('companyPosition')
        companyStart = request.POST.get('companyStart')
        companyEnd = request.POST.get('companyEnd')
        companyWorkDescription = request.POST.get('companyWorkDescription')
        projectName = request.POST.get('projectName')
        projectTime = request.POST.get('projectTime')
        projectHowYouSolved = request.POST.get('projectHowYouSolved')
        projectToolsUsed = request.POST.get('projectToolsUsed')
        achievements = request.POST.get('achievements')
        resume.firstName= firstName
        resume.lastName = lastName
        resume.mobileNumber = mobileNumber
        resume.email = email
        resume.portfolioLink = portfolioLink
        resume.linkedinLink = linkedinLink
        resume.summary = summary
        resume.collegeName = collegeName
        resume.collegeBranch = collegeBranch
        resume.collegeLocation = collegeLocation
        resume.collegeStart = collegeStart
        resume.collegeEnd = collegeEnd
        resume.collegeAchivements = collegeAchivements
        resume.skillsTechnical = skillsTechnical
        resume.skillsTools = skillsTools
        resume.certificate1 = certificate1
        resume.certificate1Link = certificate1Link
        resume.certificate2 = certificate2
        resume.certificate2Link = certificate2Link
        resume.companyName = companyName
        resume.companyLocation = companyLocation
        resume.companyPosition = companyPosition
        resume.companyStart = companyStart
        resume.companyEnd = companyEnd
        resume.companyWorkDescription = companyWorkDescription
        resume.projectName = projectName
        resume.projectTime = projectTime
        resume.projectHowYouSolved = projectHowYouSolved
        resume.projectToolsUsed = projectToolsUsed
        resume.achievements = achievements
        resume.save()
        return redirect('myResumes')
    return render(request,'editResumeForm.html',{'resume':resume})

@login_required
def deleteResume(request,id):
    resume = Resumes.objects.get(id=id)
    resume.delete()
    return redirect('myResumes')

@login_required
def downloadResume(request,id):
    resume = Resumes.objects.get(id=id)
    if resume is not None:
        context = {
            "data":{
            'firstName':resume.firstName,
            'lastName':resume.lastName,
            'mobileNumber':resume.mobileNumber,
            'email':resume.email,
            'portfolioLink':resume.portfolioLink,
            'linkedinLink':resume.linkedinLink,
            'summary':resume.summary,
            'collegeName':resume.collegeName,
            'collegeBranch':resume.collegeBranch,
            'collegeLocation':resume.collegeLocation,
            'collegeStart':resume.collegeStart,
            'collegeEnd':resume.collegeEnd,
            'collegeAchivements':resume.collegeAchivements,
            'skillsTechnical':resume.skillsTechnical,
            'skillsTools':resume.skillsTools,
            'certificate1':resume.certificate1,
            'certificate1Link':resume.certificate1Link,
            'certificate2':resume.certificate2,
            'certificate2Link':resume.certificate2Link,
            'companyName':resume.companyName,
            'companyLocation':resume.companyLocation,
            'companyPosition':resume.companyPosition,
            'companyStart':resume.companyStart,
            'companyEnd':resume.companyEnd,
            'companyWorkDescription':resume.companyWorkDescription,
            'projectName':resume.projectName,
            'projectTime':resume.projectTime,
            'projectHowYouSolved':resume.projectHowYouSolved,
            'projectToolsUsed':resume.projectToolsUsed,
            'achievements':resume.achievements,
            }
        }
        pdf = html2pdf("resume-download.html", context)
    return HttpResponse(pdf, content_type="application/pdf")

def resumeTemplates(request):
    return render(request,'resumeTemplatesOptions.html')