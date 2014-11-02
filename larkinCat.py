

#class larkinCat:
#  def __init__(self):
#    "init"

def categories():
  categories = (
    ('food'),
    ('check'),
    ('atm'),
    ('insurance'),
    ('phone'),
    ('cable'),
    ('store'),
    ('entertainment'),
    ('vacation'),
    ('car'),
    ('creditcard'),
    ('home'),
    ('paycheck'),
    ('stdntloan'),
    ('transfer'),
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
#medical
    ('Jefferson Regional','medical','bill'),
#check
    ('CHECK', 'check', 'n/a'), 
#atm
    ('Withdrawal','atm','withdrawl' ), 
#insurance
    ('State Farm','insurance','car'), 
#phone
    ('Payment Att','phone', 'n/a'), 
    ('Recurring Debit Card At&amp','phone','n/a'),
#cable
    ('Verizon','cable','cable'),
#store
    ('Target','store','retail'), 
    ('Home Depot','store','hardware'),
    ('Lowe','store','hardware'),
    ('Amazon','store','online'),
    ('Sears','store','retail'),
#entertainment
    ('The Little Gym','entertainment','girls'),
    ('Usc Recreation','entertainment','us'),
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
#car
    ('Onstar','car','misc'), 
    ('Get Go','car','gas'),
    ('Sheetz','car','gas'),
    ('Ally','car','payment'),
#creditcard
    ('Capital One','creditcard','creditcard'), 
    ('Credit Card','creditcard','creditcard'),
#home
    ('Protect Guardian','home','security'),
    ('Payment Pennsylvania-Ame','home','water'),
    ('Loan Paymt Lender','home','mortgage'),
    ('Firstenergy','utility','electric'),
#paycheck
    ('Payroll Plansource','paycheck','jodi'),
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
#misc
  )

  return keywords
