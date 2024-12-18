from django.contrib import admin
from .models import ClientInfo, Borrow, Loan, Note, Salary, ReturnBorrow
# Register your models here.


admin.site.register(ClientInfo)
admin.site.register(Borrow)
admin.site.register(Loan)
admin.site.register(Salary)
admin.site.register(Note)
admin.site.register(ReturnBorrow)
