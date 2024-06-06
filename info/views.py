from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Appliance, PaintColor, Circuit, Room, CircuitDiagram
from .forms import ApplianceForm, PaintColorForm, CircuitForm, RoomForm, CircuitDiagramForm


# Appliance Views
class ApplianceListView(ListView):
    model = Appliance
    template_name = 'info/appliance_list.html'


class ApplianceDetailView(DetailView):
    model = Appliance
    template_name = 'info/appliance_detail.html'


class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = 'info/appliance_form.html'

    def get_success_url(self):
        return reverse('appliance_detail', kwargs={'pk': self.object.pk})


class ApplianceUpdateView(UpdateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = 'info/appliance_form.html'

    def get_success_url(self):
        return reverse('appliance_detail', kwargs={'pk': self.object.pk})


class ApplianceDeleteView(DeleteView):
    model = Appliance
    template_name = 'info/appliance_confirm_delete.html'

    def get_success_url(self):
        return reverse('appliance_list')


# PaintColor Views
class PaintColorListView(ListView):
    model = PaintColor
    template_name = 'info/paintcolor_list.html'


class PaintColorDetailView(DetailView):
    model = PaintColor
    template_name = 'info/paintcolor_detail.html'


class PaintColorCreateView(CreateView):
    model = PaintColor
    form_class = PaintColorForm
    template_name = 'info/paintcolor_form.html'

    def get_success_url(self):
        return reverse('paintcolor_detail', kwargs={'pk': self.object.pk})


class PaintColorUpdateView(UpdateView):
    model = PaintColor
    form_class = PaintColorForm
    template_name = 'info/paintcolor_form.html'

    def get_success_url(self):
        return reverse('paintcolor_detail', kwargs={'pk': self.object.pk})


class PaintColorDeleteView(DeleteView):
    model = PaintColor
    template_name = 'info/paintcolor_confirm_delete.html'

    def get_success_url(self):
        return reverse('paintcolor_list')


# Circuit Views
class CircuitListView(ListView):
    model = Circuit
    template_name = 'info/circuit_list.html'


class CircuitDetailView(DetailView):
    model = Circuit
    template_name = 'info/circuit_detail.html'


class CircuitCreateView(CreateView):
    model = Circuit
    form_class = CircuitForm
    template_name = 'info/circuit_form.html'

    def get_success_url(self):
        return reverse('circuit_detail', kwargs={'pk': self.object.pk})


class CircuitUpdateView(UpdateView):
    model = Circuit
    form_class = CircuitForm
    template_name = 'info/circuit_form.html'

    def get_success_url(self):
        return reverse('circuit_list')


class CircuitDeleteView(DeleteView):
    model = Circuit
    template_name = 'info/circuit_confirm_delete.html'

    def get_success_url(self):
        return reverse('circuit_list')


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'info/room_form.html'

    def get_success_url(self):
        return reverse('home')


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'info/room_form.html'

    def get_success_url(self):
        return reverse('home')


class CircuitDiagramCreateView(CreateView):
    model = CircuitDiagram
    form_class = CircuitDiagramForm
    template_name = 'info/circuitdiagram_form.html'

    def get_success_url(self):
        return reverse('circuit_detail', kwargs={'pk': self.object.pk})


class CircuitDiagramUpdateView(UpdateView):
    model = CircuitDiagram
    form_class = CircuitDiagramForm
    template_name = 'info/circuitdiagram_form.html'

    def get_success_url(self):
        return reverse('circuit_list')


class CircuitDiagramDeleteView(DeleteView):
    model = CircuitDiagram
    template_name = 'info/circuitdiagram_confirm_delete.html'

    def get_success_url(self):
        return reverse('circuit_list')
