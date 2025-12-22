from django.shortcuts import render, get_object_or_404
from .models import Document
from .forms import AccessForm

def access_doc(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    error = None

    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['pin'] == doc.pin:
                # pdf_preview nomi bilan yuboring
                return render(request, 'documents/view.html', {
                    'doc': doc,
                    'pdf_preview': doc.pdf_image.url  # url ni ham qo'shing
                })
            else:
                error = "PIN noto‘g‘ri"
    else:
        form = AccessForm()

    return render(request, 'documents/access.html', {
        'form': form,
        'error': error
    })