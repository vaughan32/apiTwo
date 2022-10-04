from django.shortcuts import render
from RestApi.models import Worker
from RestApi.serializers import WorkerSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# ALl Workers
@api_view(['GET','POST'])
def worker_list(request,format=None):
    if request.method == 'GET':
        all_workers = Worker.objects.all()
        all_workers_serializers = WorkerSerializers(all_workers,many=True)
        return Response(all_workers_serializers.data, status = status.HTTP_200_OK)

# Create Worker
    elif request.method == 'POST':
        create_all_workers = WorkerSerializers(data = request.data)
        if create_all_workers.is_valid():
            create_all_workers.save()
            return Response(create_all_workers.data, status.HTTP_201_CREATED)
        return Response(create_all_workers.errors,status=status.HTTP_400_BAD_REQUEST)


# Details Workers
@api_view(['GET','PUT','DELETE'])
def detail_workers(request,pk,format=None):
    try:
        worker = Worker.objects.get(id=pk)
    except Worker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Get A Worker
    if request.method == 'GET':
        get_worker = WorkerSerializers(worker)
        return Response(get_worker.data,status=status.HTTP_200_OK)

# Update A Worker
    elif request.method == 'PUT':
        update_worker = WorkerSerializers(worker, data = request.data)
        if update_worker.is_valid():
            update_worker.save()
            return Response(update_worker.data,status=status.HTTP_202_ACCEPTED)
        return Response(update_worker.errors,status=status.HTTP_400_BAD_REQUEST)
# Delete A Worker
    elif request.method == 'DELETE':
        worker.delete()
        all_workers = Worker.objects.all()
        all_workers_serializers = WorkerSerializers(all_workers,many=True)
        return Response(all_workers_serializers.data, status = status.HTTP_200_OK)





