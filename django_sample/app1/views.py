from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import TestData
from .forms import QuantityForm


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    form_class = QuantityForm

    def get(self, request, *args, **kwargs) -> HttpResponse:
        object_list = TestData.objects.all().order_by("number")
        context = {
            "object_list": object_list,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        quantity_list: list[str] = []
        error_list: int[str] = []

        object_list = TestData.objects.all().order_by("number")
        for quantity_id in range(1, object_list.count()+1):
            raw_quantity: str = request.POST.get(f"quantity_{quantity_id}")
            if raw_quantity == "":
                quantity_list += [-404]
            elif int(raw_quantity) < 0:
                quantity_list += [-403]
            else:
                quantity_list += [int(raw_quantity)]

        if len([i for i, x in enumerate(quantity_list) if x == -404]) == len(quantity_list):
            error_list += ["数を入力してください"]
        elif -403 in quantity_list:
            error_list += ["0以下の数が入力されています"]

        if len(error_list) > 0:
            object_list = TestData.objects.all().order_by("number")
            context = {
                "object_list": object_list,
                "error_list": error_list,
            }
            return render(request, self.template_name, context)

        for counter in range(0, len(quantity_list)):
            print("---------------")
            quantity: int = quantity_list[counter]
            print(f"quantity_list:{quantity_list}")
            print(f"quantity:{quantity}")

            if not quantity == -404 or quantity == 0:
                object = TestData.objects.get(number=counter+1)
                object.quantity = quantity
                object.save()
        return redirect("app1:index")
