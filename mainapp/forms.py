from django import forms
from .models import ClientInfo, Borrow, Loan, Salary, Note, ReturnBorrow, ReturnLoan


class MyForm(forms.ModelForm):
	class Meta:
		model = Salary
		fields = "__all__"

		
class ReturnBorrowForm(forms.ModelForm):
	return_amount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Return amount', 'type':'number'}))
	remark = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Remark note'}))
	class Meta:
		model = ReturnBorrow
		fields = ['return_amount', 'remark']

class BorrowCompleteForm(forms.ModelForm):
	class Meta:
		model = Borrow
		fields = ['is_complete']


class ReturnLoanForm(forms.ModelForm):
	return_amount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Return amount', 'type':'number'}))
	remark = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Remark note'}))
	class Meta:
		model = ReturnLoan
		fields = ['return_amount', 'remark']

class LoanCompleteForm(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ['is_complete']
