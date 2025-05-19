from flask import Blueprint, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from .gemini_api import get_summary_from_text
from .utils import extract_audio_text
from .database import insert_summary, get_all_summaries
import datetime

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if not file:
        return "No file uploaded", 400
    filename = secure_filename(file.filename)
    filepath = os.path.join("uploads", filename)
    file.save(filepath)
   
    transcript = extract_audio_text(filepath)

    summary = get_summary_from_text(transcript)

    insert_summary(filename, summary)

    return jsonify({"summary": summary})
