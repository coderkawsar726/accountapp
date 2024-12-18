from django import template
from mainapp.models import ReturnBorrow, Borrow, ReturnLoan, Loan
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def get_total_borrow_return(client_id):
	total_return = ReturnBorrow.objects.filter(client=client_id).aggregate(total=Sum('return_amount'))['total'] or 0
	return total_return

@register.simple_tag
def get_borrow_due(client_id):
	try:
		borrow = Borrow.objects.get(pk=client_id)
		total_returned = borrow.borrow_return_client.aggregate(Sum('return_amount')).get('return_amount__sum') or 0
		return borrow.ammount - total_returned
	except borrow.DoesNotExist:
		return 0

@register.simple_tag
def get_total_loan_return(client_id):
	total_return = ReturnLoan.objects.filter(client=client_id).aggregate(total=Sum('return_amount'))['total'] or 0
	return total_return

@register.simple_tag
def get_loan_due(client_id):
	try:
		loan = Loan.objects.get(pk=client_id)
		total_returned = loan.loan_return_client.aggregate(Sum('return_amount')).get('return_amount__sum') or 0
		return loan.ammount - total_returned
	except loan.DoesNotExist:
		return 0

