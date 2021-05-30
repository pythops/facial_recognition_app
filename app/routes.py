from pathlib import Path

from flask import Blueprint, current_app, redirect, render_template, url_for

from app.forms import AnchorPhotoForm, TestPhotoForm
from app.utils.photo import same_person

detection = Blueprint("home", __name__, template_folder="templates")


@detection.route("/", methods=["GET", "POST"])
def home():
    anchor_photo_form = AnchorPhotoForm()
    test_photo_form = TestPhotoForm()

    anchor_photo = None
    test_photo = None
    match = None

    if anchor_photo_form.validate_on_submit() and anchor_photo_form.submit_anchor.data:
        for i in Path(f"{current_app.root_path}/static/anchor").iterdir():
            i.unlink()
        f = anchor_photo_form.photo.data
        f.save(f"{current_app.root_path}/static/anchor/{f.filename}")
        return redirect(url_for("home.home"))

    if test_photo_form.validate_on_submit() and test_photo_form.submit_test.data:
        for i in Path(f"{current_app.root_path}/static/test").iterdir():
            i.unlink()
        f = test_photo_form.photo.data
        f.save(f"{current_app.root_path}/static/test/{f.filename}")
        return redirect(url_for("home.home"))

    for i in Path(f"{current_app.root_path}/static/anchor").iterdir():
        anchor_photo = f"anchor/{i.name}"

    for i in Path(f"{current_app.root_path}/static/test").iterdir():
        test_photo = f"test/{i.name}"

    if anchor_photo and test_photo:
        match = same_person(
            f"{current_app.root_path}/static/{anchor_photo}",
            f"{current_app.root_path}/static/{test_photo}",
        )

    return render_template(
        "index.html",
        anchor_photo_form=anchor_photo_form,
        test_photo_form=test_photo_form,
        anchor_photo=anchor_photo,
        test_photo=test_photo,
        match=match,
    )
