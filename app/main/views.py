from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db, model
from ..models import Image
from flask_login import login_required, current_user
from .forms import InputImageForm
import numpy as np
from ..neural_network import colors_map, image_preprocessing


@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html', name=session.get('name'))

@main.route('/result', methods=['GET'])
@login_required
def result():
    return render_template('result.html')

@main.route('/upload-image', methods=['GET', 'POST'])
@login_required
def upload_image():
    form = InputImageForm()
    if form.validate_on_submit():
        img = form.image.data.read()
        img_file_path = f'app/static/colors_files/{str(datetime.utcnow())}.jpeg'.replace(' ', "")
        with open(img_file_path, 'wb') as f:
            f.write(img)
        image_array = image_preprocessing(image_path=img_file_path)
        prediction = model.predict(x=image_array)
        index = np.argmax(prediction)
        color = list(colors_map.keys())[index]
        session['color'] = color
        relative_path = img_file_path[11:]
        session['image_path'] = relative_path
        image = Image(image_owner=current_user.id, image_binary=img, 
                      image_color=color)
        db.session.add(image)
        db.session.commit()
        return redirect(url_for('main.result'))
    return render_template('upload-image.html', form=form)
