import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .use_cases.create import CreateIngredientUseCase
from .schemas.create_ingredient import CreateIngredientSchema
from pydantic import ValidationError

def index(request):
    return HttpResponse("Ola Mundo!")

@csrf_exempt
@require_http_methods(["POST"])
def create_ingredient(request):
    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    try:
        payload = CreateIngredientSchema.model_validate(data)
        print(payload)
    except ValidationError as e:
        return JsonResponse({
            'detail': e.errors(),
            'statusCode': 'BODY_VALIDATION_ERROR'
        }, status = 400)

    use_case = CreateIngredientUseCase()

    try:
        ingredient = use_case.execute(payload)
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)

    return JsonResponse(ingredient, status=201)
