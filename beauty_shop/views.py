from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

def getlabel(queryArray):
    return ['AH1', 'AH2', 'AH3']

class AdviseAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        queryArray = data['array']
        res = getlabel(queryArray)
        return Response({
            'result': res
        })
