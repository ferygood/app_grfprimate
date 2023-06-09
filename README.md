# app_TFprimate  

## Reproducibility

1. Clone the repository
```bash
git clone git@github.com:ferygood/app_TFprimate.git
```
2. Install package dependencies
```python
# create a virtualenv such as mkvirtualenv flask-tfprimate
pip install -r requirements.txt
```

3. Develop locally
```
# run debug mode
# uncomment app.run(debug=True)
python app.py
```

## Containerize
```bash
docker build . -t <image-name>
docker run -dp 8070:8070 <image-name or ID>
```