from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    total_votes = sum(choice.votes for choice in choices)
    
    for choice in choices:
        if total_votes > 0:
            choice.percentage = (choice.votes / total_votes) * 100
        else:
            choice.percentage = 0
            
    context = {
        'question': question,
        'total_votes': total_votes
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Anda belum memilih salah satu pilihan.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def all_results(request):
    # 1. Ambil semua pertanyaan, urutkan dari yang terbaru
    questions = Question.objects.order_by('-pub_date')
    
    # 2. Lakukan kalkulasi untuk setiap pertanyaan
    for question in questions:
        # Ambil semua pilihan untuk pertanyaan saat ini
        choices = question.choice_set.all()
        # Hitung total suara untuk pertanyaan ini
        total_votes = sum(choice.votes for choice in choices)
        # Tempelkan total suara ke objek question agar bisa diakses di template
        question.total_votes = total_votes
        
        # Lakukan hal yang sama untuk persentase setiap pilihan
        for choice in choices:
            if total_votes > 0:
                choice.percentage = (choice.votes / total_votes) * 100
            else:
                choice.percentage = 0
                
    # 3. Kirim daftar pertanyaan yang sudah diolah ke template
    context = {
        'questions_with_results': questions,
    }
    return render(request, 'polls/all_results.html', context)