from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import AutorForm, CategoriaForm, PostForm, PostSearchForm
from .models import Post

def home(request):
    # Renderiza inicio/templates/inicio/home.html
    return render(request, "inicio/home.html")

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "inicio/autor_form.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "inicio/categoria_form.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "inicio/post_form.html", {"form": form})

def buscar_post(request):
    form = PostSearchForm(request.GET or None)
    resultados = []
    query = ""
    if form.is_valid():
        query = form.cleaned_data.get("q", "")
        if query:
            resultados = Post.objects.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            ).select_related("autor").prefetch_related("categorias")
    return render(
        request,
        "inicio/post_search.html",
        {"form": form, "resultados": resultados, "query": query},
    )