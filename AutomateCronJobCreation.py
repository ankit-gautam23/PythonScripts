from flask import Flask, request
from crontab import CronTab

app = Flask(__name__)

@app.route('/create-cronjob', methods=['POST'])
def create_cronjob():
    # Parse request parameters
    cron_command = request.form.get('command')
    cron_schedule = request.form.get('schedule')

    # Create a new cron job
    cron = CronTab(user='your_username')
    job = cron.new(command=cron_command)
    job.setall(cron_schedule)
    cron.write()

    return 'Cron job created successfully'

if __name__ == '__main__':
    app.run(debug=True)
