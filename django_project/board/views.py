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
            ord = request.data.get('order')
            try:
                    cards = Card.objects.filter(board=request.data.get('board')).filter(progress=request.data.get('progress')).filter(order__gte=ord).order_by('order')
            except Card.DoesNotExist:
                    cards = []     
            if len(cards)>0 and cards[0].order == ord:
                    for c in cards:
                        c.order = c.order  + 1
                        c.save()
            serializer.save()            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item):
        card = Card.objects.get(pk=item)
        if not card:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        card.delete()
        try:
            cards = Card.objects.filter(board=card.board).filter(progress=card.progress).filter(order__gt=card.order).order_by('order')
        except Card.DoesNotExist:
            cards = []    
        if len(cards)>0:
            for c in cards:
                print(c)
                c.order = c.order  - 1
                c.save()
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
