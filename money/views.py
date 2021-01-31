from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Money
from .forms import MoneyForm
from django.db.models import Sum, Avg

#for graph
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import japanize_matplotlib

class MoneyListView(ListView):
    model = Money
    context_object_name = 'money_list'
    paginate_by = 3


    #db aggregate
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #sum
        total_amount = Money.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        context["total_amount"] = total_amount

        #average
        avg_amount = total_amount/3
        context["avg_amount"] = avg_amount

        #payment/per name=Taro
        pay_taro = Money.objects.filter(name='Taro').aggregate(Sum('amount'))['amount__sum'] or 0
        context["pay_taro"] = pay_taro

        #payment/per name=Koki
        pay_koki = Money.objects.filter(name='Koki').aggregate(Sum('amount'))['amount__sum'] or 0
        context["pay_koki"] = pay_koki

        #payment/per name=Kaze
        pay_kaze = Money.objects.filter(name='Kaze').aggregate(Sum('amount'))['amount__sum'] or 0
        context["pay_kaze"] = pay_kaze

        #deficiency/per name=Taro
        deficiency_taro = avg_amount - pay_taro
        context["deficiency_taro"] = deficiency_taro

        #deficiency/per name=Koki
        deficiency_koki = avg_amount - pay_koki
        context["deficiency_koki"] = deficiency_koki

        #deficiency/per name=Kaze
        deficiency_kaze = avg_amount - pay_kaze
        context["deficiency_kaze"] = deficiency_kaze

        #create graph
        x_list = ['Taro', 'Koki', 'Kaze']
        y_list = [pay_taro, pay_koki, pay_kaze]
        create_graph(x_list, y_list)
        graph = get_image()
        context['graph'] = graph

        return context

#graph
def create_graph(x_list, y_list):
    plt.cla()
    plt.title("現在の支払金額")
    plt.bar(x_list, y_list)
    plt.xlabel('名前')
    plt.ylabel('金額(円)')
    

#convertion
def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


class MoneyDetailView(DetailView):
    model = Money

class MoneyCreateView(CreateView):
    model = Money
    form_class = MoneyForm
    success_url = reverse_lazy('list')

class MoneyUpdateView(UpdateView):
    model = Money
    form_class = MoneyForm

    def get_success_url(self):
        money_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
        return url

class MoneyDeleteView(DeleteView):
    model = Money
    success_url = reverse_lazy('list')