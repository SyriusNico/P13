from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from .forms import RegisterForm, EditProfileForm, EditMailForm, EditAddressForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


class PasswordsChangeView(PasswordChangeView):
	template_name = 'registration/change-password.html'
	success_url = reverse_lazy('success')


class AccountDetailView(TemplateView):
	template_name = 'registration/account-detail.html'


class UsernameChangeView(UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/change-username.html'
	success_url = reverse_lazy('success')

	def get_object(self):
		return self.request.user


class MailChangeView(UpdateView):
	form_class = EditMailForm
	template_name = 'registration/change-mail.html'
	success_url = reverse_lazy('success')

	def get_object(self):
		return self.request.user


class AddressView(UpdateView):
	form_class = EditAddressForm
	template_name = 'registration/address.html'
	success_url = reverse_lazy('success')

	def get_object(self):
		return self.request.user
