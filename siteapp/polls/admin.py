from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Menampilkan 3 slot pilihan kosong

class QuestionAdmin(admin.ModelAdmin):
    # Mengatur tampilan field di halaman daftar pertanyaan
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
    # Mengelompokkan field di halaman edit
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Informasi Tanggal', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # Menambahkan pilihan langsung di bawah pertanyaan
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)