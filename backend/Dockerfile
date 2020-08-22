# FROM python:3-onbuild
# CMD ["mkdir", "backend"]
# COPY . ./backend
# CMD [ "python", "./backend/app.py" ]

FROM python:3-onbuild

WORKDIR /usr/src/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]