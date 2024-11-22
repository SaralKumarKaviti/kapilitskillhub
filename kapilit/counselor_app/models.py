from django.db import models
from django.utils import timezone

# Create your models here.

class Manager(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=150, unique=True)
	employee_id = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.name

class Counselor(models.Model):
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=150, unique=True)
	employee_id = models.CharField(max_length=15,unique=True)
	
	def __str__(self):
		return self.name

class Role(models.Model):
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=150, unique=True)
	employee_id = models.CharField(max_length=15,unique=True)
	role_type = models.CharField(max_length=50)
	added_on = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

class StudentEnrollment(models.Model):
    COURSE_CHOICES = [
        ('python_full_stack', 'Python Full Stack'),
        ('java_full_stack', 'Java Full Stack'),
        ('data_science', 'Data Science'),
        ('digital_marketing', 'Digital Marketing'),
        ('ui_ux', 'UI / UX'),
    ]
    EDU_STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]
    QUALIFICATIONS = [
        ('inter', 'Intermediate'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('btech', 'Bachelor Technology'),
        ('mtech', 'Master Technology'),
    ]
    LOCATIONS = [
        ('Nanakramguda-Hub', 'Nanakramguda-Hub'),
        ('Ameerpet', 'Ameerpet'),
    ]
    MODES_OF_ATTENDING = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    counselor = models.ForeignKey('Role', on_delete=models.CASCADE)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=50, choices=LOCATIONS)
    mode_of_attending = models.CharField(max_length=20, choices=MODES_OF_ATTENDING)
    qualification = models.CharField(max_length=150, choices=QUALIFICATIONS)
    branch = models.CharField(max_length=150)
    course_name = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    education_status = models.CharField(max_length=20, choices=EDU_STATUS_CHOICES)
    passed_year = models.CharField(max_length=4, null=True, blank=True)
    marks = models.CharField(max_length=10, null=True, blank=True)
    current_year = models.CharField(max_length=10, null=True, blank=True)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    enrollment_id = models.CharField(max_length=20,unique=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course_name}"

# class RegistrationStudentPaymentDetails(models.Model):
#     PAYMENT_MODES = [
#         ('offline','Offline'),
#         ('online','Online')
#     ]
#     manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
#     counselor = models.ForeignKey('Role', on_delete=models.CASCADE)
#     student = models.ForeignKey('StudentEnrollment',on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=150)
#     enrollment_id = models.CharField(max_length=50)
#     course_name = models.CharField(max_length=150)
#     payment_mode = models.CharField(max_length=150, choices=PAYMENT_MODES)
#     payment_status = models.CharField(max_length=50)
#     paymented_on = models.DateTimeField(auto_now_add=True)
#     payment_by = models.CharField(max_length=150)
#     transaction_id = models.CharField(max_length=150)
#     registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.student_name} {self.last_name} - {self.transaction_id}"



class StudentPaymentDetails(models.Model):
    PAYMENT_MODES = [
        ('offline','Offline'),
        ('online','Online')
    ]
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    counselor = models.ForeignKey('Role', on_delete=models.CASCADE)
    student = models.ForeignKey('StudentEnrollment',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150)
    enrollment_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=150)
    payment_mode = models.CharField(max_length=150, choices=PAYMENT_MODES)
    payment_status = models.CharField(max_length=50)
    paymented_on = models.DateTimeField(auto_now_add=True)
    payment_by = models.CharField(max_length=150)
    transaction_id = models.CharField(max_length=150)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.student_name} {self.last_name} - {self.transaction_id}"

class RegistrationPaymentDetails(models.Model):
    PAYMENT_MODES = [
        ('offline','Offline'),
        ('online','Online')
    ]
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    counselor = models.ForeignKey('Role', on_delete=models.CASCADE)
    student = models.ForeignKey('StudentEnrollment',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150)
    enrollment_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=150)
    payment_mode = models.CharField(max_length=150, choices=PAYMENT_MODES)
    register_payment_status = models.CharField(max_length=50)
    paymented_on = models.DateTimeField(auto_now_add=True)
    payment_by = models.CharField(max_length=150)
    transaction_id = models.CharField(max_length=150)
    register_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.student_name} {self.last_name} - {self.transaction_id}"

