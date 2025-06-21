from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ""
    for q in latest_question_list:
        output += f"{q.question_text}<br>"
        # answer list
        answer_list = Choice.objects.filter(question=q)
        list_answer = ", ".join([a.choice_text for a in answer_list])
        output += f"Pilihan: {list_answer}"
        output += "<br><br>"
    return HttpResponse(output)

def html_index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   answer_list = Choice.objects.all()
   context = { "latest_question_list": latest_question_list,
       "answer_list": answer_list
   }
   return render(request, "index.html", context)



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def address(requset):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Address</title>
        <style>
        body {font-family: sans-serif; margin:40px;}
        h1 {color: #333;}
    </style>
    </head>
    <body>
        <h1>Address</h1>
        <p>Cisaat, Sukabumi, Jawa Barat</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def phone(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Phone</title>
        <style>
        body {font-family: sans-serif; margin:40px;}
        h1 {color: #333;}
    </style>
    </head>
    <body>
        <h1>Phone</h1>
        <p>+6281311757392</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
    