from fastapi import APIRouter

router = APIRouter()

@router.get('/run')
def run_task():
    return {'status': 'running', 'message': 'Команда выполняется!'}
