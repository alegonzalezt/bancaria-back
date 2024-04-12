from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.productos.models.cuentas_bancarias import CuentaBancaria
from apps.productos.serializers.cuentas_bancarias import CuentaBancariaSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class CuentasBancariasViews(viewsets.GenericViewSet):
    
    serializer_class = CuentaBancariaSerializer

    def get_permissions(self):
        """
        Asignacion de permisos por accion
        """
        if self.action in ['registro_cuenta']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(methods=['post'], detail=False, url_path="registro-cuenta")
    def registro_cuenta(self, request):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

    @action(methods=['get'], detail=False, url_path="detalle-cuenta")
    def detalle_cuenta(self, request):
        usuario_i = request.user
        try:
            cuenta_bancaria = CuentaBancaria.objects.get(usuario_cuenta=usuario_i)
            serializer = CuentaBancariaSerializer(cuenta_bancaria, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
