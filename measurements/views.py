from django.shortcuts import render, redirect, get_object_or_404
from .models import Measurement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.db.models import Min

def measurement_list(request):
    if request.user.is_authenticated:
        measurements = request.user.measurements.all()
    else:
        measurements = []  # No measurements for anonymous users
    return render(request, 'measurement_list.html', {'measurements': measurements})

@csrf_exempt  # Use with caution
def add_measurement(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=403)
        
        data = json.loads(request.body)
        try:
            measurement = Measurement(
                user=request.user,
                weight=data.get('weight'),
                height=data.get('height'),
                chest=data.get('chest'),
                waist=data.get('waist'),
                hips=data.get('hips'),
                thighs=data.get('thighs'),
                calves=data.get('calves'),
                left_arm=data.get('left_arm'),
                right_arm=data.get('right_arm'),
                unit=data.get('unit'),
                notes=data.get('notes'),
            )
            measurement.full_clean()  # This will raise a ValidationError if any field is invalid
            measurement.save()
            return JsonResponse({'success': True, 'measurement': measurement.to_dict()})
        except ValidationError as e:
            return JsonResponse({'success': False, 'errors': e.message_dict}, status=400)
    
    return JsonResponse({'success': False}, status=400)

@csrf_exempt  # Use with caution
def edit_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if request.method == 'POST':
        if measurement.user != request.user:
            return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)
        
        data = json.loads(request.body)
        try:
            for field, value in data.items():
                setattr(measurement, field, value)
            measurement.full_clean()  # This will raise a ValidationError if any field is invalid
            measurement.save()
            return JsonResponse({'success': True, 'measurement': measurement.to_dict()})
        except ValidationError as e:
            return JsonResponse({'success': False, 'errors': e.message_dict}, status=400)
    
    return JsonResponse({'success': False}, status=400)

@csrf_exempt  # Use with caution
def delete_measurement(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if measurement.user != request.user:
        return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)
    
    measurement.delete()
    
    # Check if there are any remaining measurements
    remaining_measurements = Measurement.objects.filter(user=request.user).exists()
    
    return JsonResponse({'success': True, 'has_measurements': remaining_measurements})