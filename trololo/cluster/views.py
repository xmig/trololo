import json
from rest_framework import viewsets
from models import ClusterInfo
from serializers import ClusterInfoSerializer
from django.shortcuts import render, redirect
from forms import Cluster_InfoModelForm

import logging
_logger = logging.getLogger("trololo")


class ClusterInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product categories to be viewed or edited.
    """
    queryset = ClusterInfo.objects.all()
    serializer_class = ClusterInfoSerializer


def cluster_data_list():
    cluster_list = ClusterInfo.objects.all()

    data_list = (str(x.host_ip) for x in cluster_list if x.in_cluster==True)
    return data_list


def cluster_info_page(request):
    cluster_list = ClusterInfo.objects.all()
    context = {'cluster_list': cluster_list}
    return render(request, 'cluster_info.html', context)


def cluster_info_add(request):
    cluster_info = ClusterInfo()
    if request.method == 'POST':
        form = Cluster_InfoModelForm(request.POST, instance=cluster_info)
        if form.is_valid():
            form.save()
            return redirect('/system/cluster_info/')
    else:
        form = Cluster_InfoModelForm(instance=cluster_info)
    context = {'form': form, 'object': cluster_info}
    return render(request, 'cluster_info_edit.html', context)


def load_balancer(request):
    if request.body:
        host = json.loads(request.body)
        if host:
            obj = ClusterInfo.objects.get(hostname=host["host"]["hostname"])
            obj.enabled = host["host"]["enabled"]
            obj.save()
            _logger.info("Load Balancer. Host {} {}".format(host["host"], 'ADDED' if obj.enabled else "EXCLUDED"))
    return render(request, 'cluster/load_balancer.html')