from flask import Flask, request, jsonify
from AccountsRegistry import AccountsRegistry
from Konto import Konto_Osobiste

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
    
    return jsonify({"name": konto.imie, "surname": konto.nazwisko,"saldo":konto.saldo, "pesel": konto.pesel }), 200


@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):

    konto = AccountsRegistry.search_by_id(pesel)
    if konto == None:
        return jsonify({"error":"account not found"}),404
    
    data = request.get_json()

    for key in data:
        if key == "name":
            konto.imie=data["name"]
        elif key == "surname":
            konto.nazwisko=data["surname"]
        elif key == "pesel":
            konto.pesel=data["pesel"]

    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    AccountsRegistry.delete_account(pesel)
    return jsonify({"message": "Account deleted"}), 200
