from django.db import models





class Conto(models.Model):
    AMBITI = {"N": "numeraria",
              "E": "economica",
              "P": "patrimonio netto",

              }
    nome = models.CharField(max_length=80)
    ambito = models.CharField(max_length=1, choices=AMBITI)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Operazione(models.Model):
    nome = models.CharField(max_length=60)

    dare = models.ForeignKey(Conto, on_delete=models.CASCADE, related_name='operazioni_dare', null=True)
    avere = models.ForeignKey(Conto, on_delete=models.CASCADE, related_name='operazioni_avere', null=True)

    def __str__(self):
        return self.nome

class Movimento(models.Model):

    NATURE = {"B": "budget",
              "E": "effettiva"

              }
    dataMovimento=models.DateField()
    dataRegistrazione=models.DateField(auto_now_add=True)
    operazione=models.ForeignKey(Operazione, null=True, on_delete=models.SET_NULL)
    descrizione=models.CharField(max_length=120)
    importo=models.FloatField()
    natura=models.CharField(max_length=1, choices=NATURE)