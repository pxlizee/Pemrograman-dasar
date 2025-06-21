from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
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
    