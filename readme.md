#venv
python3 -m venv venv

#load venv
source venv\Scripts\activate

#install module.
pip3 install -r requirements.txt

#Train Model:
python3 train_model.py

#Run
python3 app.py

#Test

curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"size":1200,"bedrooms":2,"age":4}'
