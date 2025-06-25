# server/seed.py

#!/usr/bin/env python3

from server.app import app
from server.models import db, Customer, Item, Review

with app.app_context():
    print("Clearing old data...")
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()

    print("Seeding customers...")
    customer1 = Customer(name='Tal Yuri')
    customer2 = Customer(name='Raha Rosario')
    customer3 = Customer(name='Luca Mahan')
    db.session.add_all([customer1, customer2, customer3])
    db.session.commit()

    print("Seeding items...")
    item1 = Item(name='Laptop Backpack', price=49.99)
    item2 = Item(name='Insulated Coffee Mug', price=9.99)
    item3 = Item(name='6 Foot HDMI Cable', price=12.99)
    db.session.add_all([item1, item2, item3])
    db.session.commit()

    print("Seeding reviews...")
    db.session.add_all([
        Review(comment="zipper broke the first week", customer=customer1, item=item1),
        Review(comment="love this backpack!", customer=customer2, item=item1),
        Review(comment="coffee stays hot for hours!", customer=customer1, item=item2),
        Review(comment="best coffee mug ever!", customer=customer3, item=item2),
        Review(comment="cable too short", customer=customer3, item=item3),
    ])
    db.session.commit()

    print("Done seeding!")
