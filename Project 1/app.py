from flask import Flask, request, jsonify
from  datetime import date, datetime, timezone
from dateutil import tz
import calendar

# create app instance
app = Flask(__name__)


@app.route("/api")
def index():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    # get current day info
    current_date = date.today()
    current_day = calendar.day_name[current_date.weekday()]

    # get utc
    current_utc = datetime.utcnow().replace(tzinfo=timezone.utc)

    # Get local timezone
    local_zone = tz.tzlocal()
    dt_local = current_utc.astimezone(local_zone)
    formatted_utc_time = dt_local.strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/zee467/Hng-Projects/blob/main/Project%201/app.py"
    github_repo_url = "https://github.com/zee467/Hng-Projects/tree/main"

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": formatted_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)