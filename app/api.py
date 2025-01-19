from flask import Flask, request, jsonify
from .AccountRegistry import AccountRegistry
from .Konto_Osobiste import Konto_Osobiste

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    if AccountRegistry.search_by_id(data["pesel"]):
        return jsonify({"message": "Account of this pesel already exists"}),409
    konto = Konto_Osobiste(data["name"], data["surname"], data["pesel"])
    AccountRegistry.add_account(konto)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts/count", methods=['GET'])
def account_count():
    count = AccountRegistry.get_accounts_count()
    return jsonify({"Account count": count}),200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):

    konto = AccountRegistry.search_by_id(pesel)
    if konto == None:
        return jsonify({"error":"account not found"}),404
    
    return jsonify({"name": konto.imie, "surname": konto.nazwisko,"balance":konto.saldo, "pesel": konto.pesel }), 200


@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):

    konto = AccountRegistry.search_by_id(pesel)
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
    AccountRegistry.delete_account(pesel)
    return jsonify({"message": "Account deleted"}), 200

@app.route("/api/accounts/<pesel>/transfer",methods=["POST"])
def transfer(pesel):
    data = request.get_json()
    typ = data["type"]
    amount = data["amount"]
    account = AccountRegistry.search_by_id(pesel)
    if not account:
        return jsonify({"message":"Nie znaleziono konta"}),404
    
    elif typ == "incoming":
        account.przelew_przychodzący(amount)

    elif typ == "outgoing":
        transfer_successful = account.przelew_wychodzący(amount)
        if not transfer_successful:
            return jsonify({"message":"Transfer nieudany"}),422

    elif typ == "express":
        transfer_successful = account.przelew_ekspresowy(amount)
        if not transfer_successful:
            return jsonify({"message": "Transfer nieudany"}),422
    else:
        return jsonify({"message":"Transfer type not recognised"}),405
        
    return jsonify({"message":"Zlecenie przyjęto do realizacji"}),200

