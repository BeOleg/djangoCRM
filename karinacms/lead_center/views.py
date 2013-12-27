from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import LeadForm, CampaignForm, leadCommentForm, UserForm, UserInfoForm, ProductForm, LeadStatusForm
from .models import Campaign, Lead, LeadComment, LeadStatus, UserInfo, Product
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.conf import settings

from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from .custom_permissions import PostOnly

class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leads being viewed and edited
    """
    model = Lead
    serializer_class = LeadSerializer
    permission_classes = [PostOnly]


def register(request):
	registered = False
	userForm = UserForm(request.POST or None)
	userInfoForm = UserInfoForm(request.POST or None)
	if userForm.is_valid() and userInfoForm.is_valid():
		user = userForm.save()
		user.set_password(user.password)
		user.save()
		userInfo = userInfoForm.save(commit=False)
		userInfo.user = user
		userInfo.save()
		registered = True
	
	context = {'userForm': userForm, 'userInfoForm': userInfoForm, 'registered': registered}
	return render(request, 'lead_center/register.html', context)

def user_login(request):
	msg = None
	next = None

	if request.method == 'POST':
		username = request.POST['username'];
		password = request.POST['password'];
		u = authenticate(username=username, password=password)
		if u and u.is_active:
			login(request, u)
			redirect_url = request.GET.get('next') or '/leads/'
			return HttpResponseRedirect(redirect_url)
		else:
			msg = 'Invalid credentials or inactive account'
		# context.form = userCredentialsForm
	context = {'msg': msg}
	return render(request, 'lead_center/login.html', context)

@login_required
def lead_form(request, campaign_name='eartohear.info'):
	campaign = None
	try:
		campaign = Campaign.objects.get(name=campaign_name)
		print campaign
	except Campaign.DoesNotExist:
		pass  # do stuff

	form = LeadForm(request.POST or None)

	context_dict = {'form': form, 'title': 'Create new lead'}
	if form.is_valid():
		# do stuff
		lead = form.save(commit=False)
		lead.campaign = campaign
		lead.save()
		context_dict['success'] = True

	return render(request, 'lead_center/lead_form.html', context_dict)

@login_required
def lead_edit_form(request, lead_id):
	leadData=None
	form=None
	leadEdited=False
	notFound=False
	title=None
	try:
		leadData = Lead.objects.get(id=lead_id)
		print leadData.id
	except Lead.DoesNotExist:
		pass #pass

	if leadData:
		title = 'Edit lead - ' + leadData.first_name + ' ' + leadData.last_name
		form = LeadForm(request.POST or None, instance=leadData)
		if form.is_valid():
			#save for and show success			
			leadData.save()
			form.save()
			leadEdited = True
	else:
		#no such lead
		title = 'No such lead'
		notFound = True
	context_dict = {'title': title, 'notFound': notFound, 'leadEdited': leadEdited, 'form': form}
	return render(request, 'lead_center/lead_form.html', context_dict)

@login_required
def product_list(request):
	productAdded = False
	products = Product.objects.annotate(lead_count=Count('product_leads'))
	#products = = Product.objects.all()

	form=ProductForm(request.POST or None)
	if form.is_valid():
		product = form.save()
		product.save()
		productAdded = True
	context_dict = {'products': products, 'form': form, 'productAdded': productAdded, 'obj_type': 'Product'}
	return render(request, 'lead_center/product_list.html', context_dict)

@login_required
def search_list(request):
	object_type = request.GET['object_type']
	query_string = request.GET['query_string']
	if object_type == 'Campaign':
		model_class = Campaign
		objStr = 'campaign'
	elif object_type == 'Product':
		model_class = Product
		objStr = 'product'
	elif object_type == 'Status':
		model_class = LeadStatus
		objStr = 'status'
	elif object_type == 'Lead':
		model_class = Lead
		objStr = 'lead'
	result_set = model_class.objects.filter(name__icontains=query_string)
	return render(request, 'lead_center/common/generic_list.html', {'obj': result_set, 'objStr': objStr})
	
@login_required
def delete_obj(request, obj_type, obj_id):
	if obj_type == 'campaign':
		title = 'Delete campagign?'
		model_class = Campaign
		redirect_url = 'campaign_list' 
	elif obj_type == 'product':
 		title = 'Delete product?'
 		model_class = Product
 		redirect_url = 'product_list'
 	elif obj_type == 'status':
 		title = 'Delete status?'
 		model_class = LeadStatus
 		redirect_url = 'status_list'
 	else:
 		raise Http404

	success = None
	try:
		obj = model_class.objects.get(pk=obj_id)
	except (Campaign.DoesNotExist, Product.DoesNotExist):
		raise Http404

	if request.method == "POST" and obj:
		obj.delete()
		return redirect(redirect_url)
	
	return render(request, 'lead_center/common/delete_obj.html', {'title': delete_obj, 'success': success, 'object': obj})


@login_required
def edit_obj (request, obj_type, obj_id):
	if obj_type == 'campaign':
		model = Campaign
		form_class = CampaignForm
		title = 'Edit campaign'
		redirect_url = 'campaign_list'
	elif obj_type == 'product':
		model = Product
		form_class = ProductForm
		title = 'Edit product'
		redirect_url = 'product_list'
	elif obj_type == 'status':
		model = LeadStatus
		form_class = LeadStatusForm
		title = 'Edit lead status'
		redirect_url = 'status_list'
	else:
		raise Http404

	success = None
	try:
		obj = model.objects.get(pk=obj_id)
	except model.DoesNotExist:
		raise Http404

	form = form_class(request.POST or None, instance=obj)
	
	if form.is_valid() and obj:
		form.save()
		return redirect(redirect_url)
	return render(request, 'lead_center/common/edit_obj.html', {'title': title, 'formTitle': obj.name, 'form': form})



@login_required
def campaign_list(request):
	campaignAdded = False
	campaigns = Campaign.objects.annotate(lead_count=Count('campaign_leads'))
	#products = = Product.objects.all()
	form=CampaignForm(request.POST or None)
	if form.is_valid():
		campaign = form.save()
		campaignAdded = True
	context_dict = {'campaigns': campaigns, 'form': form, 'campaignAdded': campaignAdded, 'obj_type': 'Campaign'}
	return render(request, 'lead_center/campaign_list.html', context_dict)

@login_required
def status_list(request):
	statusAdded = False
	statuses = LeadStatus.objects.annotate(lead_count=Count('status_leads'))
	#products = = Product.objects.all()
	form=LeadStatusForm(request.POST or None)
	if form.is_valid():
		status = form.save()
		statusAdded = True
	context_dict = {'statuses': statuses, 'form': form, 'statusAdded': statusAdded, 'obj_type': 'Status'}
	return render(request, 'lead_center/status_list.html', context_dict)


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/leads/')
	
def index(request):
	leads = Lead.objects.all().order_by('phone')
	context_dict = {'leads': leads}
	if request.session.has_key('last_visit'):
		last_visit = request.session.get('last_visit')
		visits = request.session.get('visits', 0)
		if(datetime.now() - datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
			request.session['last_visit'] = str(datetime.now())	
			request.session['visits'] = visits + 1
	else:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = 1
	return render(request, 'lead_center/index.html', context_dict)

@login_required
def lead_page(request, lead_name=None):
	split_name = lead_name.split('-')
	leads = None
	comment_list = None
	comment_success = False

	leads = Lead.objects.filter(first_name = split_name[0], last_name = split_name[1])

	form = leadCommentForm(request.POST or None)
	if leads:
		comment_list = LeadComment.objects.filter(lead = leads[0])
	if leads and form.is_valid():
		comment = form.save(commit=False)
		comment.lead = leads[0]#change this to many to many blat
		comment.save()
		comment_success = True
	context_dict = {'leads': leads, 'title': lead_name, 'form': form, 'comment_list': comment_list, 'comment_success': comment_success}
	return render(request, 'lead_center/lead_page.html', context_dict)