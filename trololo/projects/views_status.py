from serializers import StatusSerializer
from rest_framework import status
from projects.models import  Status
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response



class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetail(generics.GenericAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_object(self, pk):
        try:
            return Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        status = self.get_object(pk)
        serializer = StatusSerializer(status, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        stat = self.get_object(pk)
        serializer = StatusSerializer(stat, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        st = self.get_object(pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
