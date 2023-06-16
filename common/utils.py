from django.shortcuts import redirect

from petstagram.common.models import PhotoLike


def gets_user_liked_photos(photo_id):
    # TODO: fix when authentication
    return PhotoLike.objects.filter(photo_id=photo_id)


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'