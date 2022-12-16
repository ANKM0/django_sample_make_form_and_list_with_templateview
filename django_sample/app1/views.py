from django.views.generic import TemplateView
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect

from .models import TestData


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    object_list = TestData.objects.all().order_by("number")
    max_num = object_list.count()

    # これがモデルフォームセット
    test_data_formset = forms.modelformset_factory(
        model=TestData,
        fields=["quantity"],
        extra=3,  # default-> 1
        max_num=max_num    # initial含めformは最大4となる
    )

    def get_context_data(self, **kwargs):
        # get処理だけ書く
        ctx = super().get_context_data(**kwargs)
        # 新規作成formを作る場合は
        # formset = self.test_data_formset(queryset=TestData.objects.none())
        ctx["formset"] = self.test_data_formset()
        ctx["object_list"] = self.object_list
        return ctx

    def post(self, request, *args, **kwargs) -> HttpResponse:
        formset = self.test_data_formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("app1:index")
        context = {
            "object_list": self.object_list,
            "formset": formset,
        }
        return render(request, self.template_name, context)
