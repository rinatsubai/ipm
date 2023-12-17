from django.db import models
from django.db.models import Count, Sum, Avg
from django.utils import timezone
from ipmclients.models import *
# from finance.models import *

# Create your models here.

class Status(models.Model):
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=512, default='table-primary')
    def __str__(self):
        return self.status_name
    class Meta:
        ordering = ["id"]
        verbose_name = "status"
        verbose_name_plural = "statuses"
    pass

class Project(models.Model):
    project_name = models.CharField(max_length=512, unique = True)
    def __str__(self):
        return self.project_name
    project_created = models.DateTimeField(null=True, default=timezone.now)
    project_finished = models.DateTimeField(null=True)
    project_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, default="Draft")
    project_client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, related_name='project')
    project_product = models.CharField(max_length=512)
    project_sum = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={'pk': self.pk})
    
    def get_project_transactions_sum(self):
        # qs = Project.objects.exclude(transaction = None)
        # qs2 = qs.transaction   
        # for q in qs:
        #     res = q.transaction.aggregate(Sum("amount"))
        #     print(tuple(res.values()))
        try:
            qs = Project.objects.exclude(transaction = None)
            qs2 = qs.filter(pk = self.pk)
            for qso in qs2:
                qs3 = qso.transaction.all()
                for q in qs3:
                    res = qs3.aggregate(Sum('amount'))
                    print(qso, res)
            return(res)
        except:
            res = 0
            return(res)
        
    def get_project_transactions_cost(self):
        # qs = Project.objects.exclude(transaction = None)
        # qs2 = qs.transaction   
        # for q in qs:
        #     res = q.transaction.aggregate(Sum("amount"))
        #     print(tuple(res.values()))
        try:
            qs = Project.objects.exclude(transaction = None)
            qs2 = qs.filter(pk = self.pk)
            for qso in qs2:
                qs3 = qso.transaction.filter(flow = "OUT")
                for q in qs3:
                    res = qs3.aggregate(Sum('amount'))
                    print(qso, res)
            return(res)
        except:
            res = 0
            return(res)
    
    class Meta:
        ordering = ["pk"]
        verbose_name = "project"
        verbose_name_plural = "projects"
    pass

# for q in qs2:
#         res = q.transaction.aggregate(Sum("amount"))
#         for r in res:
#             f = res["amount__sum"]
#             print(f)
            
# for q in qs2:
#         f = res["amount__sum"].aggregate(Sum("amount__sum"))
#         print(f)
            
# for q in qs2:
#     res = q.transaction.aggregate(Sum("amount"))
#     for r in res:
#         f = res["amount__sum"]
#         print(f)


# qs = Project.objects.exclude(transaction = None)
# for q in qs:
#     res = q.transaction.aggregate(Sum("amount"))
#     for r in res:
#         f = res["amount__sum"].aggregate(Sum("amount__sum"))
#         print(f)
        





# qsa = qs[1]
# qs3 = qsa.transaction.all()
# for q in qs3:
# f = q.amount
# print(f)
# qs3.aggregate(Sum('amount'))
