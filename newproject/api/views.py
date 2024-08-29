from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import BooksSerializer
from .models import Books

# Create your views here.

@api_view(['GET'])
def get_books(request):
    item = Books.objects.all()
    serialized_data = BooksSerializer(item, many=True)
    return Response(serialized_data.data)



@api_view(['POST'])
def create_book(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


@api_view(['GET','DELETE','PATCH'])
def delete_book(request, pk):
    try:
        book = Books.objects.get(pk=pk)
        print ("bookeName: ", book)
    except Books.DoesNotExist:
        print ("Book not found")
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BooksSerializer(book)
        print ("2222222222222")
        return Response(serializer.data)
    if request.method == 'PATCH':
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)