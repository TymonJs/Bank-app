from flask import Flask, request, jsonify
from app.AccountsRegistry import AccountsRegistry
from app.Konto import Konto_Osobiste

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    konto = Konto_Osobiste(data["name"], data["surname"], data["pesel"])
    AccountsRegistry.add_account(konto)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts/count", methods=['GET'])
def account_count():
    count = AccountsRegistry.get_accounts_count()
    return jsonify({"Account count": count}),200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):

    konto = AccountsRegistry.search_by_id(pesel)
    if konto == None:
        return jsonify({"error":"account not found"}),404
    
    return jsonify({"imie": konto.imie, "nazwisko": konto.nazwisko,"saldo":konto.saldo, "pesel": konto.pesel }), 200