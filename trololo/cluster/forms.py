from django import forms
from models import ClusterInfo


class Cluster_InfoModelForm(forms.ModelForm):
    class Meta:
        model = ClusterInfo
        fields = ['host_ip', 'internal_ip', 'hostname', 'in_cluster']