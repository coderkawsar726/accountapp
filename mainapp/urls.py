from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.Menu, name='menu'),
	path('dashboard/', views.Dashboard, name='dashboard'),
	# LOAN URLS
	path('loan-index/', views.LoanIndex, name='loan_index'),
	path('loan-complete-index/', views.CompleteLoanClients, name='loan_complete_dashboard'),
	path('add-loan/', views.AddLoan.as_view(), name='add_loan'),
	path('detail-loan/<pk>/', views.DetailLoan, name='detail_loan'),
	path('complete-loan/<int:client_id>/', views.CompleteLoan, name='complete_loan'),
	path('detail-complete-loan/<pk>/', views.CompleteLoanDetail, name='detail_complete_loan'),
	# BORROW URLS
	path('borrow-index/', views.BorrowIndex, name='borrow_index'),
	path('borrow-complete-index/', views.CompleteBorrowClients, name='borrow_complete_dashboard'),
	path('add-borrow/', views.AddBorrow.as_view(), name='add_borrow'),
	path('add-client/', views.AddClient.as_view(), name='add_client'),
	path('detail-borrow/<pk>/', views.DetailBorrow, name='detail_borrow'),
	path('detail-complete-borrow/<pk>/', views.CompleteClientDetail, name='detail_complete_borrow'),
	path('complete-borrow/<int:client_id>/', views.CompleteBorrow, name='complete_borrow'),
	# NOTE URLS
	path('notes/', views.MyNotes.as_view(), name='note_dashboard'),
	path('add-note/', views.CreateNote.as_view(), name='add_note'),
	path('read-note/<pk>/', views.ReadNote.as_view(), name='read_note'),
	path('update-note/<pk>/', views.UpdateNote.as_view(), name='update_note'),
	path('delete-note/<pk>/', views.DeleteNote.as_view(), name='delete_note'),

	# TESTING URLS
	path('form/', views.FormView, name='form'),
	path('test/', views.TestView, name='testpage'),
]
