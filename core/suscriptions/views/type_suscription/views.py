from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.suscriptions.forms import TypeSuscriptionForm
from core.suscriptions.models import TypeSuscription


# Create your views here.
class TypeSuscriptionCreateView(CreateView):
    model = TypeSuscription
    form_class = TypeSuscriptionForm
    template_name = "type_suscription/create.html"
    success_url = reverse_lazy('suscriptions:type_suscription_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                # data = TypeSuscription.objects.get(pk=request.POST['id']).toJSON()
                # form = TypeSuscriptionForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna acción'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Tipo Suscripción'
        context['action'] = 'create'
        context['list_url'] = reverse_lazy('suscriptions:type_suscription_list')
        return context

class TypeSuscriptionUpdateView(UpdateView):
    model = TypeSuscription
    form_class = TypeSuscriptionForm
    template_name = "type_suscription/create.html"
    success_url = reverse_lazy('suscriptions:type_suscription_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                # data = TypeSuscription.objects.get(pk=request.POST['id']).toJSON()
                # form = TypeSuscriptionForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna acción'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición Tipo Suscripción'
        context['action'] = 'update'
        context['list_url'] = reverse_lazy('suscriptions:type_suscription_list')
        return context

class TypeSuscriptionDeleteView(DeleteView):
    model = TypeSuscription
    template_name = 'type_suscription/delete.html'
    success_url = reverse_lazy('suscriptions:type_suscription_list')

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Tipo Suscripción'
        context['action'] = 'delete'
        context['list_url'] = reverse_lazy('suscriptions:type_suscription_list')
        return context

class TypeSuscriptionListView(ListView):
    model = TypeSuscription
    template_name = "type_suscription/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # #Sobrescribo mi query
    # def get_queryset(self):
    #     return TypePerson.objects.filter(name__startswith="C")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = TypeSuscription.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    # Agrego mas variables
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Tipo Suscripciones'
        context['create_url'] = reverse_lazy('suscriptions:type_suscription_create')
        return context

# #Vistas basada en funciones, no es recomendable
# def diHola(request):
#     data = {
#         'title': "Lista Tipo Personas",
#         'type_people': TypePerson.objects.all()
#     }
#     return render(request, "type_suscription/list.html", data)
