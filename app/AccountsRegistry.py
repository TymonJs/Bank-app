class AccountsRegistry:
    registry= []

    @classmethod
    def add_account(cls,account):
        cls.registry.append(account)

    @classmethod
    def get_accounts_count(cls):
        return len(cls.registry)

    @classmethod
    def search_by_id(cls,id):
        for acc in cls.registry:
            if acc.pesel==id:
                return acc

    

    