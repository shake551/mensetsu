from fastapi import APIRouter

router = APIRouter()


@router.get('/interview/random')
async def obtain_random_interviews():
    pass


@router.get('/interview/bookmark')
async def obtain_bookmarked_interviews():
    pass


@router.post('/interview/bookmark')
async def add_bookmark_interview():
    pass


@router.delete('/interview/bookmark')
async def delete_boookmark_interview():
    pass
