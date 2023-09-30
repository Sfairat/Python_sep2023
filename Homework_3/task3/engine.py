history_list = []


def add_money(card):
    add_sum = int(input("Укажите сумму пополнения: "))
    if (add_sum % 50 == 0) and (card.balance < 5_000_000):
        card.balance += add_sum
        print(f"Внесение денежных средств прошло успешно. Баланс {card.balance}.")
        card.count_of_operations += 1
        if card.count_of_operations % 3 == 0:
            card.balance += (add_sum / 100) * 3
        history_list.append(card.balance)
    elif (add_sum % 50 == 0) and (card.balance >= 5_000_000):
        card.balance += add_sum - ((add_sum / 100) * 10)
        print(f"Внесение денежных средств прошло успешно. Удержан налог на богатство 10%. Баланс {card.balance}.")
        card.count_of_operations += 1
        if card.count_of_operations % 3 == 0:
            card.balance += (add_sum / 100) * 3
        history_list.append(card.balance)
    else:
        print(f"Сумма внесения наличных должна быть кратна 50. Баланс {card.balance}.")


def withdraw_money(card):
    withdraw_sum = int(input("Укажите сумму для снятия: "))
    if (withdraw_sum % 50 == 0) and (card.balance < 5_000_000):
        if withdraw_sum > card.balance:
            print(f"На вашем счёте недостаточно средств. Баланс {card.balance}.")
        else:
            if 30 < (withdraw_sum / 100) * 1.5 < 600:
                card.balance -= (withdraw_sum + ((withdraw_sum / 100) * 1.5))
                print(
                    f"Снятие денежных средств прошло успешно. Комиссия за снятие наличных 1.5%. Баланс {card.balance}.")
            elif (withdraw_sum / 100) * 1.5 < 30:
                card.balance -= (withdraw_sum + 30)
                print(f"Снятие денежных средств прошло успешно. Комиссия за снятие наличных 30. Баланс {card.balance}.")
            elif (withdraw_sum / 100) * 1.5 > 600:
                card.balance -= (withdraw_sum + 600)
                print(
                    f"Снятие денежных средств прошло успешно. Комиссия за снятие наличных 600. Баланс {card.balance}.")
            card.count_of_operations += 1
            if card.count_of_operations % 3 == 0:
                card.balance += ((withdraw_sum / 100) * 3)
            history_list.append(card.balance)
    elif (withdraw_sum % 50 == 0) and (card.balance > 5_000_000):
        card.balance -= (withdraw_sum + ((withdraw_sum / 100) * 10))
        print(f"Снятие денежных средств прошло успешно. Удержан налог на богатство 10%. Баланс {card.balance}.")
        card.count_of_operations += 1
        if card.count_of_operations % 3 == 0:
            card.balance += ((withdraw_sum / 100) * 3)
        history_list.append(card.balance)
    else:
        print(f"Сумма снятия наличных должна быть кратна 50. Баланс {card.balance}.")


def end():
    exit()


def transaction_history():
    print(history_list)
