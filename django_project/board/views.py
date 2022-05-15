from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card, Board
from .serializers import CardSerializer, BoardSerializer


class CardsAPIView(APIView):

    def put(self, request, item):
        card = Card.objects.get(pk=item)
        if not card:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {"id": item, "title": request.data.get('title'), "progress": request.data.get('progress'), "board": request.data.get('board'), "order": request.data.get('order')}
        serializer = CardSerializer(instance=card, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item):
        card = Card.objects.get(pk=item)
        if not card:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CardsByType(APIView):

    def get(self, request, board,  progress):
        cards = Card.objects.filter(board=board).filter(progress=progress).order_by('order')
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CardsCreateAPIView(CreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class BoardAPIView(APIView):

    def get(self, request, item):
        boards = Board.objects.filter(author=item)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item):
        board = Board.objects.get(pk=item)
        if not board:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {"id": item, "title": request.data.get('name'), "created": board.created, "author": request.data.get('author')}
        serializer = BoardSerializer(instance=board, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item):
        board = Board.objects.get(pk=item)
        if not board:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BoardCreateAPIView(CreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
