from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyForm, ReturnBorrowForm, BorrowCompleteForm, ReturnLoanForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import ClientInfo, Borrow, Loan, Salary, Note, ReturnBorrow, ReturnLoan
# Create your views here.


@login_required
def Menu(request):
	return render(request, 'menu.html', context={})

@login_required
def Dashboard(request):
	return render(request, 'dashboard.html', context={})

# LOAN FUNCTIONALITY
@login_required
def LoanIndex(request):
	loans = Loan.objects.filter(is_complete=False)
	context = {
		'loans': loans, 
	}
	return render(request, 'loan/dashboard.html', context)

class AddLoan(LoginRequiredMixin, CreateView):
	model = Loan
	fields = "__all__"
	template_name = 'loan/addnew.html'
	success_url = reverse_lazy('main:loan_index')


@login_required
def DetailLoan(request, pk):
	loan = Loan.objects.get(pk=pk, is_complete=False)
	
	return_detail = ReturnLoan.objects.filter(client=loan.id)
	total_return = ReturnLoan.objects.filter(client=loan.id).aggregate(total=Sum('return_amount'))['total'] or 0
	if return_detail:
		due = loan.ammount - total_return
	else:
		due = loan.ammount

	if request.method == 'POST':
		form = ReturnLoanForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.client = loan
			form.save()
			return redirect('main:detail_loan', pk=pk)
	else:
		form = ReturnLoanForm()
	context = {
		'loan': loan,
		'message': False, 
		'form':form,
		'total_return': total_return,
		'return_detail': return_detail,
		'due': due,
	}
	return render(request, 'loan/detail.html', context)


@login_required
def CompleteLoanClients(request):
	loans = Loan.objects.filter(is_complete=True)
	context = {
		'loans': loans, 
	}
	return render(request, 'loan/completeclients.html', context)


@login_required
def CompleteLoan(request, client_id):
	client = Loan.objects.get(id=client_id)
	if request.method == 'POST':
		form = BorrowCompleteForm(request.POST, instance=client)
		form.save()
		return redirect('main:loan_index')
	else:
		form = BorrowCompleteForm()
	return render(request, 'complete.html', {'client': client, 'form': form})


@login_required
def CompleteLoanDetail(request, pk):
	loan = Loan.objects.get(pk=pk, is_complete=True)
	
	return_detail = ReturnLoan.objects.filter(client=loan.id)
	total_return = ReturnLoan.objects.filter(client=loan.id).aggregate(total=Sum('return_amount'))['total'] or 0
	if return_detail:
		due = loan.ammount - total_return
	else:
		due = loan.ammount
	context = {
		'loan': loan, 
		'total_return': total_return,
		'return_detail': return_detail,
		'due': due,
	}
	return render(request, 'loan/completedetail.html', context)


# Borrow Function Start 

@login_required
def BorrowIndex(request):
	borrows = Borrow.objects.filter(is_complete=False)
	
	context = {
		'borrows': borrows, 
	}
	return render(request, 'borrow/dashboard.html', context)


@login_required
def CompleteBorrowClients(request):
	borrows = Borrow.objects.filter(is_complete=True)
	context = {
		'borrows': borrows, 
	}
	return render(request, 'borrow/completeclients.html', context)


@login_required
def CompleteClientDetail(request, pk):
	borrow = Borrow.objects.get(pk=pk, is_complete=True)
	
	return_detail = ReturnBorrow.objects.filter(client=borrow.id)
	total_return = ReturnBorrow.objects.filter(client=borrow.id).aggregate(total=Sum('return_amount'))['total'] or 0
	if return_detail:
		due = borrow.ammount - total_return
	else:
		due = borrow.ammount
	context = {
		'borrow': borrow, 
		'total_return': total_return,
		'return_detail': return_detail,
		'due': due,
	}
	return render(request, 'borrow/completedetail.html', context)


class AddBorrow(LoginRequiredMixin, CreateView):
	model = Borrow
	fields = "__all__"
	template_name = 'borrow/addnew.html'
	success_url = reverse_lazy('main:borrow_index')


class AddClient(LoginRequiredMixin, CreateView):
	model = ClientInfo
	fields = "__all__"
	template_name = 'borrow/addclient.html'
	success_url = reverse_lazy('main:borrow_index')


@login_required
def DetailBorrow(request, pk):
	borrow = Borrow.objects.get(pk=pk, is_complete=False)
	
	return_detail = ReturnBorrow.objects.filter(client=borrow.id)
	total_return = ReturnBorrow.objects.filter(client=borrow.id).aggregate(total=Sum('return_amount'))['total'] or 0
	if return_detail:
		due = borrow.ammount - total_return
	else:
		due = borrow.ammount

	if request.method == 'POST':
		form = ReturnBorrowForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.client = borrow
			form.save()
			return redirect('main:detail_borrow', pk=pk)
	else:
		form = ReturnBorrowForm()
	context = {
		'borrow': borrow, 
		'form':form,
		'total_return': total_return,
		'return_detail': return_detail,
		'due': due,
	}
	return render(request, 'borrow/detail.html', context)


@login_required
def CompleteBorrow(request, client_id):
	client = Borrow.objects.get(id=client_id)
	if request.method == 'POST':
		form = BorrowCompleteForm(request.POST, instance=client)
		form.save()
		return redirect('main:borrow_index')
	else:
		form = BorrowCompleteForm()
	return render(request, 'complete.html', {'client': client, 'form': form})




# NOTE MANAGEMENT 


class MyNotes(LoginRequiredMixin, ListView):
	model = Note
	template_name = 'note/dashboard.html'
	context_object_name = 'notes'

class CreateNote(LoginRequiredMixin, CreateView):
	model = Note 
	template_name = 'note/addnew.html'
	fields = "__all__"
	success_url = reverse_lazy('main:note_dashboard')

class ReadNote(LoginRequiredMixin, DetailView):
	model = Note 
	template_name = 'note/readnote.html'
	context_object_name = 'mynote'

class UpdateNote(LoginRequiredMixin, UpdateView):
	model = Note 
	template_name = 'note/addnew.html'
	fields = "__all__"
	
	def get_success_url(self, **kwargs):
		return reverse_lazy('main:read_note', kwargs={'pk':self.object.pk})

class DeleteNote(LoginRequiredMixin, DeleteView):
	model = Note 
	template_name = 'note/deletenote.html'
	success_url = reverse_lazy('main:note_dashboard')




# Testing View 

def FormView(request):
	if request.method == 'POST':
		form = MyForm(request.POST);
		if form.is_valid():
			form.save()
			return redirect('main:testpage')
	else:
		form = MyForm()
		return render(request, 'form.html', {'form':form})


def TestView(request):
	context = {}
	return render(request, 'testpage.html', context)
