FROM python:3.8-slim-buster

ADD main.py .

RUN pip install pandas matplotlib datetime shapely geopandas contextily 

CMD ["python", "./main.py"]


