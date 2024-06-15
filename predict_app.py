import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request, jsonify, Flask
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mapping of class indices to labels (example)
acne_labels = {0: 'Comedones', 1: 'Cystic/Nodular', 2: 'Pustules/Papules'}
skin_type_labels = {0: 'Dry', 1: 'Normal', 2: 'Oily'}

def get_models():
    global acne_model, skin_type_model
    custom_objects = {'F1Score': tf.keras.metrics.F1Score()}
    
    # Load acne model
    acne_model = load_model('acneClass.h5', custom_objects=custom_objects)
    acne_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
                       loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Load skin type model
    skin_type_model = load_model('skintype.h5', custom_objects=custom_objects)
    skin_type_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
                            loss='categorical_crossentropy', metrics=['accuracy'])

def preprocess_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# Initialize and load the models once at the start
print("Loading Keras models...")
get_models()

@app.route("/predict_acne", methods=["POST"])
def predict_acne():
    try:
        message = request.get_json(force=True)
        if 'image' not in message:
            return jsonify({"error": "'image' key not found in request"}), 400
        
        encoded = message['image']
        base64Image = re.sub(r"^data:image/(png|jpeg);base64,", "", encoded)
        decoded = base64.b64decode(base64Image)
        image = Image.open(io.BytesIO(decoded))
        processed_image = preprocess_image(image, target_size=(224, 224))
        prediction = acne_model.predict(processed_image).tolist()[0]
        predicted_class_index = np.argmax(prediction)
        predicted_class_label = acne_labels[predicted_class_index]
        
        response = {'Prediction': predicted_class_label}
        return jsonify(response)
    
    except Exception as e:
        app.logger.error(f"Exception in /predict_acne: {str(e)}")
        return jsonify({"error": "An error occurred during prediction"}), 500

@app.route("/predict_skin_type", methods=["POST"])
def predict_skin_type():
    try:
        message = request.get_json(force=True)
        if 'image' not in message:
            return jsonify({"error": "'image' key not found in request"}), 400
        
        encoded = message['image']
        base64Image = re.sub(r"^data:image/(png|jpeg);base64,", "", encoded)
        decoded = base64.b64decode(base64Image)
        image = Image.open(io.BytesIO(decoded))
        processed_image = preprocess_image(image, target_size=(224, 224))
        prediction = skin_type_model.predict(processed_image).tolist()[0]
        predicted_class_index = np.argmax(prediction)
        predicted_class_label = skin_type_labels[predicted_class_index]
        
        response = {'Prediction': predicted_class_label}
        return jsonify(response)
    
    except Exception as e:
        app.logger.error(f"Exception in /predict_skin_type: {str(e)}")
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == '__main__':
    app.run(debug=True)
