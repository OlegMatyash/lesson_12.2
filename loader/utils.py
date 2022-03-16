from exceptions import PictureWrongTypeError

def save_uploaded_picture(picture):

    filename = picture.filename

    file_type = filename.split('.')[-1]

    if file_type not in ["jpg", "jpeg", "png", "svg"]:
        raise PictureWrongTypeError

    picture.save(f"./uploads/images/{filename}")

    return f"uploads/images/{filename}"