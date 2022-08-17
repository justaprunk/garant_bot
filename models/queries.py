from .models import *
from .models import session


def get_user(chat_id):
    return session.query(User).filter_by(chat_id=chat_id).first()


def get_all_users():
    return session.query(User).filter_by(banned=False).all()


def get_all_users_count():
    return session.query(User).filter_by(banned=False).count()


def new_user(chat_id):
    user = get_user(chat_id)
    if user is None:
        user = User(chat_id=chat_id)
        user.save()
    return user


def get_offers_count():
    return session.query(Offer).count()


def new_offer(deal, review):
    offer = Offer(
        id=deal.id,
        customer_id=deal.customer_id,
        seller_id=deal.seller_id,
        amount=deal.amount,
        review=review,
    )
    offer.save()
    deal.delete()
    return offer


def get_deal(deal_id):
    return session.query(Deal).filter_by(id=deal_id).first()


def new_deal(customer_chat_id, seller_chat_id):
    deal = Deal(
        customer_id=customer_chat_id, seller_id=seller_chat_id, status=Deal.Status.new
    )
    deal.save()
    return deal


def new_withdrawal(chat_id, metamask_address, amount):
    withdrawal = Withdrawal(
        user_id=chat_id, metamask_address=metamask_address, amount=amount
    )
    withdrawal.save()
    return withdrawal