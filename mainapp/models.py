from django.db import models
import datetime



CLIENT_CATEGORY_LIST = [
	('', 'Select...'),
	('borrow', "Borrow"),
	('loan', "Loan"),
	('personal', "Personal"),
]

CURRENCY_CHOICE = [
	('SAR', 'SAR'),
	('BDT', 'BDT'),
]

MONTH_CHOICE = [
	('', 'Select...'),
	('1', 'January'),
	('2', 'February'),
	('3', 'March'),
	('4', 'April'),
	('5', 'May'),
	('6', 'June'),
	('7', 'July'),
	('8', 'August'),
	('9', 'September'),
	('10', 'October'),
	('11', 'November'),
	('12', 'December')
]

YEAR_SELECT = [
	('', 'Select...'),
	('2020', '2020'),
	('2021', '2021'),
	('2022', '2022'),
	('2023', '2023'),
	('2024', '2024'),
	('2025', '2025'),
	('2026', '2026'),
	('2027', '2027'),
	('2028', '2028'),
	('2029', '2029'),
	('2030', '2030')
]
CURRENT_MONTH = datetime.date.today().month
CURRENT_YEAR = datetime.date.today().year



class Borrow(models.Model):
	client_name = models.CharField(max_length=50)
	ammount = models.IntegerField()
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, default='SAR')
	remark = models.CharField(max_length=150)
	date = models.DateField(auto_now_add=True)
	is_complete = models.BooleanField(default=False)

	class Meta:
		ordering = ['-id']


	def __str__(self):
		return self.client_name

class ReturnBorrow(models.Model):
	client = models.ForeignKey(Borrow, on_delete=models.CASCADE, related_name='borrow_return_client')
	return_amount = models.IntegerField()
	remark = models.CharField(max_length=150)
	return_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.client.client_name

	class Meta:
		ordering = ['-id']


class Loan(models.Model):
	client_name = models.CharField(max_length=50)
	ammount = models.IntegerField()
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, default='SAR')
	remark = models.CharField(max_length=150)
	date = models.DateField(auto_now_add=True)
	is_complete = models.BooleanField(default=False)

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.client.client_name

class ReturnLoan(models.Model):
	client = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='loan_return_client')
	return_amount = models.IntegerField()
	remark = models.CharField(max_length=150)
	return_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.client.client_name

	class Meta:
		ordering = ['-id']



class Salary(models.Model):
	month = models.CharField(max_length=15, choices=MONTH_CHOICE, default=CURRENT_MONTH)
	year = models.CharField(max_length=15, choices=YEAR_SELECT, default=CURRENT_YEAR)
	main_salary = models.IntegerField()
	food_bill = models.IntegerField()

	def __str__(self):
		return self.month + " - " + self.year


class Note(models.Model):
	title = models.CharField(max_length=300)
	note = models.TextField()
	date = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-date',]
		
	def __str__(self):
		return self.title



class ClientInfo(models.Model):
	client = models.ForeignKey(Borrow, on_delete=models.CASCADE, related_name='borrow_client')
	client_email = models.EmailField(max_length=50, blank=True)
	client_contact = models.CharField(max_length=26)
	client_note = models.CharField(max_length=100)
	client_NID = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.client.client_name

