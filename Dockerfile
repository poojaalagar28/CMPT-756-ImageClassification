# FROM python:3.7

# WORKDIR /main

# COPY requirements.txt ./requirements.txt

# RUN pip install -r requirements.txt

# EXPOSE 8501

# COPY . /main

# CMD [ "streamlit","run","main.py" ]

FROM python:3.7
WORKDIR /main
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /main
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]

