from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Sum
from authentication.models import User
from user_dashboard.models import Ticket

@permission_required('authentication.is_manager', login_url='manager_login')
def manager_dashboard(request):
    # Get statistics
    total_users = User.objects.count()
    total_tickets = Ticket.objects.count()
    total_orders = 197  # Replace with actual order count
    total_revenue = 340282346638528  # Replace with actual revenue calculation
    
    context = {
        'active_tab': 'dashboard',
        'total_users': total_users,
        'total_tickets': total_tickets,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
    }
    return render(request, 'managerdashboard/dashboard.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def reports(request):
    context = {
        'active_tab': 'reports',
    }
    return render(request, 'managerdashboard/reports.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def orders(request):
    context = {
        'active_tab': 'orders',
    }
    return render(request, 'managerdashboard/orders.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def services(request):
    context = {
        'active_tab': 'services',
    }
    return render(request, 'managerdashboard/services.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def tickets(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    context = {
        'active_tab': 'tickets',
        'tickets': tickets,
    }
    return render(request, 'managerdashboard/tickets.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def users(request):
    users = User.objects.all().order_by('-date_joined')
    context = {
        'active_tab': 'users',
        'users': users,
    }
    return render(request, 'managerdashboard/users.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def subscribers(request):
    context = {
        'active_tab': 'subscribers',
    }
    return render(request, 'managerdashboard/subscribers.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def providers(request):
    context = {
        'active_tab': 'providers',
    }
    return render(request, 'managerdashboard/providers.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def payments(request):
    context = {
        'active_tab': 'payments',
    }
    return render(request, 'managerdashboard/payments.html', context)

@permission_required('authentication.is_manager', login_url='manager_login')
def settings(request):
    context = {
        'active_tab': 'settings',
    }
    return render(request, 'managerdashboard/settings.html', context)


