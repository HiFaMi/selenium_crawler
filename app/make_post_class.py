import os
import django
django.setup()

from app.pictures.models import PostPicture

PRESENT_DIR = os.path.abspath('')
IMG_DIR = os.path.join(PRESENT_DIR, '.media/img')

dir_lists = os.listdir(IMG_DIR)


for dir_list in dir_lists:
    if os.path.isdir(os.path.join(IMG_DIR, dir_list)):
        class_user_name = dir_list
        img_lists = os.listdir(os.path.join(IMG_DIR, dir_list))
        new_img_counter = 0
        for img_list in img_lists:
            if PostPicture.objects.filter(post_picture='img/{}/{}'.format(class_user_name, img_list)) is not True:
                post = PostPicture.objects.create(
                    post_user=class_user_name,
                    post_picture='img/{}/{}'.format(class_user_name, img_list)
                )
                post.save()

                new_img_counter += 1

        print("new img about {}: -{}".format(dir_list, new_img_counter))
print("Done")
