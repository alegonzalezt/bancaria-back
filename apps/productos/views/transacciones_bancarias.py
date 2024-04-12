from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.productos.models.cuentas_bancarias import CuentaBancaria
from rest_framework.permissions import AllowAny, IsAuthenticated


class TransaccionesBancariasViews(viewsets.GenericViewSet):

    def get_permissions(self):
        """
        Asignacion de permisos por accion
        """
        if self.action in ['consignar_dinero']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(methods=['patch'], detail=False, url_path="consignar-dinero")
    def consignar_dinero(self, request):
        data_consignar = self.request.data
        cuenta_bancaria = CuentaBancaria.objects.filter(
            numero_cuenta=data_consignar["numero_cuenta"]
        )

        try:
            if cuenta_bancaria:
                for cuenta in cuenta_bancaria:
                    cuenta.saldo_cuenta += data_consignar['saldo']
                    cuenta.save()
                    return Response({"mensaje": "Consignación efectuada."}, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje": "Cuenta no existe."}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({"mensaje": "Error al efectuar consignación."}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['patch'], detail=False, url_path="retirar-dinero")
    def retirar_dinero(self, request):
        usuario_i = request.user
        data_retirar = self.request.data
        saldo_retirar = data_retirar["saldo"]

        cuenta_bancaria = CuentaBancaria.objects.filter(
            numero_cuenta=data_retirar["numero_cuenta"],
            usuario_cuenta=usuario_i
        )

        try:
            if cuenta_bancaria:
                for cuenta in cuenta_bancaria:
                    if saldo_retirar > cuenta.saldo_cuenta:
                        return Response({"mensaje": "No cuenta con dinero suficiente en cuenta."}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        cuenta.saldo_cuenta -= saldo_retirar
                        cuenta.save()
                        return Response({"mensaje": "Retiro exitoso."}, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje": "Error al efectuar el retiro."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"mensaje": "Error al efectuar el retiro."}, status=status.HTTP_400_BAD_REQUEST)
