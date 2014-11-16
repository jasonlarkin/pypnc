

#class larkinCat:
#  def __init__(self):
#    "init"

def categories():
  categories = (
#core
    ('paycheck'),
    ('food'),
    ('phone'),
    ('cable'),
    ('car'),
    ('home'),
    ('stdntloan'),
    ('insurance'),
#other
    ('medical'),
    ('creditcard'),
    ('store'),
    ('entertainment'),
    ('vacation'),
#bank transactions
    ('check'),
    ('atm'),
    ('transfer'),
#misc
    ('misc_identified'),
    ('misc')
  )
  return categories

def keywords():    
  keywords = (
#food
    ('Giant-Eagle','food','grocery'),
    ('Giant Eagle','food','grocery'),
    ('Market Distric','food','grocery'),
    ('The Fresh Mark', 'food', 'grocery'), 
    ('Chipotle', 'food', 'out'),
    ('McDonald','food','out'),
    ('Burger King','food','out'),
    ('Bean Curd','food','out'),
    ('El Campesino','food','out'),
    ('Valleybrook Be','food','beer'),
    ('Bruegger', 'food', 'out'),
    ('Fiori','food','out'),
    ('Dunkin','food','out'),
    ('Wendy','food','out'),
    ('Cowtastic','food','out'),
    ('Bruster','food','out'),
    ('Starbucks','food','out'),
    ('Aladdins','food','out'),
    ('Carnegie Mellon Dining','food','out'),
    ('Quiznos','food','out'),
    ('Chili','food','out'),
    ('Handel','food','out'),
    ('Duffys','food','beer'),
    ('BEER-N-AT','food','beer'),
    ('Italian Village Pizza','food','out'),
    ('Jerome Bettis','food','out'),
    ('Lu Lus Noodles','food','out'),
    ('Mm Mm Pizza','food','out'),
    ('Houlihan','food','out'),
    ('Dairy Queen','food','out'),
    ('Ardolinos','food','out'),
    ('Panera','food','out'),
    ('Gloria Jeans','food','out'),
    ('Liquor','food','beer'),
    ('Chicken NOW','food','out'),
    ('Arbys','food','out'),
    ('Coldstone','food','out'),
    ('Beans and Cream','food','out'),
    ('Juniper Grill','food','out'),
    ('Hunan Inn','food','out'),
    ('Sharp Edge','food','out'),
    ('Red Robin','food','out'),
    ('Mrs. Fields','food','out'),
    ('Coal Fired','food','out'),
    ('AUNTIE ANNE','food','out'),
    ('VILLA FIK','food','out'),
    ('NOODLES & CO','food','out'),
#medical
    ('Jefferson Regional','medical','bill'),
    ('Kids Plus','medical','girls'),
    ('Walgreens','medical','store'),
    ('South Hills Family','medical','girls'), 
    ('Jefferson Reg Med','medical','bill'),
#check
    ('CHECK', 'check', 'n/a'), 
#atm
    ('Withdrawal','atm','withdrawl' ), 
#insurance
    ('State Farm','insurance','car'), 
#phone
    ('Payment Att','phone', 'n/a'), 
    ('Recurring Debit Card At&amp','phone','n/a'),
    ('At&amp;T*Bill','phone','n/a'),
    ('Recurring Check Card At','phone','n/a'),
#cable
    ('Verizon','cable','cable'),
#store
    ('Target','store','retail'), 
    ('Home Depot','store','hardware'),
    ('Lowe','store','hardware'),
    ('Amazon','store','online'),
    ('Sears','store','retail'),
    ('Old Navy','store','retail'),
    ('Carter','store','retail'),
    ('Ace ','store','hardware'),
    ('Kmart','store','retail'),
    ('Wal-Mart','store','retail'),
    ('Radioshack','store','retail'),
    ('Toys R US','store','retail'),
    ('BABIES R US','store','retail'),
#entertainment
    ('The Little Gym','entertainment','girls'),
    ('Usc Recreation','entertainment','us'),
    ('Mastodon','entertainment','us'),
    ('Redbox','entertainment','us'),
    ('Smart Toys','entertainment','girls'),
    ('Zoo','entertainment','girls'),
#vacation
    ('Dogfish Head','vacation','rehoboth'),
    ('Obies By The Sea','vacation','rehoboth'),
    ('Rehoboth Toy','vacation','rehoboth'),
    ('Funland  Rehoboth','vacation','rehoboth'),
    ('Starkeys Cones Sundaes','vacation','rehoboth'),
    ('Semras Mediterranean','vacation','rehoboth'),
    ('Purchase USPS 095720097 Rehoboth','vacation','rehoboth'),
    ('Louies Pizza','vacation','rehoboth'),
    ('Purchase Thrasher','vacation','rehoboth'),
    ('Purchase Starbucks #14253 Rehob','vacation','rehoboth'),
    ('Purchase Dos Locos Restaurant','vacation','rehoboth'),
    ('Purchase Sole Kids Inc Rehoboth','vacation','rehoboth'),
    ('Debit Card Purchase Ihop','vacation','rehoboth'),
    ('Debit Card Purchase Kilwin','vacation','rehoboth'),
    ('Five Guys Rehoboth','vacation','rehoboth'),
    ('Wawa 849 Rehoboth Bch De','vacation','rehoboth'),
    ('POS Purchase Food Lion #048 Reholoboth','vacation','rehoboth'),
    ('Chick-Fil-A #03141','vacation','rehoboth'),
    ('5354 Check Card Purchase Chick-Fil-A #03141','vacation','rehoboth'),
    ('Fishers Popcorn','vacation','rehoboth'),
    ('Giant Food Inc','vacation','rehoboth'),
#business
    ('Superpantry','business','jason'),
    ('Paradies','business','jason'),
    ('Pik N Go','business','jason'),
    ('Farmers Market','business','jason'),
#car
    ('Onstar','car','misc'), 
    ('Get Go','car','gas'),
    ('Sheetz','car','gas'),
    ('Ally','car','payment'),
    ('Power Of','car','maintenance'),
    ('Sunoco','car','gas'),
    ('Exxonmobil','car','gas'),
#creditcard
    ('Capital One','creditcard','creditcard'), 
    ('Credit Card','creditcard','creditcard'),
#home
    ('Protect Guardian','home','security'),
    ('GUARDIAN PRO','home','security'),
    ('Payment Pennsylvania-Ame','home','water'),
    ('PENNSYLVANIA-AME','home','water'),
    ('Loan Paymt Lender','home','mortgage'),
    ('LENDER LIVE','home','mortgage'),
    ('Firstenergy','home','electric'),
    ('American Water','home','water'),
    ('Gas Bill Peoples Natural','home','gas'),
#paycheck
    ('Payroll Plansource','paycheck','jodi'), #monthly
    ('PLANSOURCE ADMIN PAYROLL','paycheck','jodi'), #Activity
    ('Quickbooks','paycheck','jason'),
#student loans
    ('Stdnt Loan','stdntloan','jodi'),
    ('Great Lakes','stdntloan','jason'),
#transfer
    ('Transfer','transfer','misc'),
#deposit
    ('Mobile Deposit', 'deposit', 'deposit'),
#misc_identified
    ('Paypal','misc_identified','paypal'),
    ('Dropbox','misc_identified','dropbox'),
    ('Itunes','misc_identified','itunes'),
    ('Experian','misc_identified','credit report'),
    ('The UPS Store','misc_identified','amazon sales'),
    ('USPS','misc_identified','amazon sales'),
    ('Boomerang','misc_identified','gmail'),
    ('IRS','misc_identified','tax refund'),
    ('Jordantaxservice','misc_identified','tax'),
    ('Check Card Purchase Ecsi Carnegie Mellon','misc_identified','health ins'),
    ('PETERSTWP','misc_identified','recreation'),
#misc
  )

  return keywords
