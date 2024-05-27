from django.db import models
from django.conf import settings

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100)


class Party(models.Model):
    price = models.IntegerField()
    capacity = models.IntegerField()

    # 파티 계정 정보
    account_id = models.CharField(max_length=100)
    account_password = models.CharField(max_length=100)

    # 계좌 정보
    bank_account = models.CharField(max_length=100)

    # 파티가 개설된 상태면 연관된 다른 정보를 마음대로 삭제할 수 없도록 제약
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participate_parties')