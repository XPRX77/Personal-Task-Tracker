FROM python:3.13-alpine
COPY . /Personal_task_tracker
WORKDIR /Personal_task_tracker
RUN pip install -r requirement.txt
CMD python main.py