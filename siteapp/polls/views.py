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
    
    # Ambil semua pilihan yang terkait dengan pertanyaan
    choices = question.choice_set.all()
    
    # 1. Hitung total semua suara
    total_votes = sum(choice.votes for choice in choices)
    
    # 2. Tambahkan atribut 'percentage' ke setiap objek pilihan
    for choice in choices:
        if total_votes > 0:
            # Hitung persentase
            choice.percentage = (choice.votes / total_votes) * 100
        else:
            # Hindari pembagian dengan nol jika belum ada vote
            choice.percentage = 0
            
    # 3. Kirim 'question' dan 'total_votes' ke template
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
        # Jika tidak ada pilihan, tampilkan kembali halaman detail dengan pesan error
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Anda belum memilih salah satu pilihan.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Selalu redirect setelah POST berhasil untuk mencegah data di-post dua kali
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def address(request):
    # Pastikan juga file address.html ada di polls/templates/polls/
    return render(request, 'polls/address.html')
def phone(request):
    # Pastikan juga file phone.html ada di polls/templates/polls/
    return render(request, 'polls/phone.html')