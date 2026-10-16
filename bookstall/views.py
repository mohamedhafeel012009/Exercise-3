from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import student

def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html',
                  {'students': students})

def student_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        student.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('student_list')

    return render(request, 'student_form.html')


def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.title = request.POST.get('title')
        student.author = request.POST.get('author')
        student.price = request.POST.get('price')
        student.save()

        return redirect('student_list')

    return render(request, 'student_form.html',
                  {'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

    return redirect('student_list')