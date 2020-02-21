from flask import Flask, escape, request, Response, send_from_directory
from flask_cors import CORS
import json

from budget_manager import BudgetManager

budget_manager = BudgetManager(db_path='budget.db')
app = Flask(__name__, static_url_path='', static_folder='public')
CORS(app)


@app.route('/')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return send_from_directory('public', 'index.html')


@app.route("/v1/budget/", methods=['POST'])
def set_budget():
    json_data = request.get_json(force=True, silent=True)

    date = json_data['date']
    amount = json_data['amount']

    if not budget_manager.check_date_exist(date):
        budget_manager.create_budget(date, amount)
        message = 'Create succeeded'
        code = BudgetManager.STATUS_CODE_CREATED
    else:
        budget_manager.update_budget(date, amount)
        message = 'Update succeeded'
        code = BudgetManager.STATUS_CODE_UPDATED

    resp = {
        'message': message,
        'code': code
    }

    return Response(json.dumps(resp), status=200, mimetype='application/json')


@app.route("/v1/budget/", methods=['GET'])
def get_budget():
    date = request.args.get('date')
    print(date)
    return 'ok'


@app.route("/v1/query/", methods=['POST'])
def query_budget():
    json_data = request.get_json(force=True, silent=True)

    start_date = json_data['start_date']  # YYYYMMDD
    end_date = json_data['end_date']  # YYYYMMDD

    total_amount = budget_manager.query_budget(start_date, end_date)

    resp = {
        'total_amount': total_amount
    }
    return Response(json.dumps(resp), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
