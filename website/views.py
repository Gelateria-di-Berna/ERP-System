from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Location
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/location-management", methods=["GET", "POST"])
@login_required
def location_management():
    if request.method == "POST":
        location_name = request.form.get("location_name")
        location_address = request.form.get("location_address")
        if len(location_name) < 1:
            flash("Location name is too short!", category="error")
        elif len(location_address) < 1:
            flash("Location address is too short!", category="error")
        else:
            current_user.add_location(location_name, location_address)
            flash("Standort hinzugefügt!", category="success")
    
    locations = Location.query.all()
    return render_template("location_management.html", user=current_user, locations=locations)
    
@views.route("/delete-location", methods=["POST"])
@login_required
def delete_location():
    location_data = json.loads(request.data)
    locationId = location_data["locationId"]
    location = Location.query.get(locationId)  # Location anhand der ID aus der Datenbank abrufen
    if location:
        # Alle Benutzer von der Location entfernen (dies erfolgt automatisch aufgrund der Cascade-Konfiguration)
        location.users.clear()
        db.session.delete(location)  # Location aus der Datenbank entfernen
        db.session.commit()  # Änderungen in der Datenbank bestätigen
        flash("Location successfully deleted!", category="success")
    else:
        flash("Location not found!", category="error")
    return jsonify({})

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note_data = json.loads(request.data)
    noteId = note_data["noteId"]
    note = Note.query.get(noteId)
    
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})