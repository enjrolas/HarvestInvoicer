from datetime import datetime, timedelta
from harvest import Harvest

h = Harvest( 'https://enjrolas.harvestapp.com', 'alex@nublabs.com', 'planeman' )
user = h.find_user( 'Test', 'Guy' )
if user:
        print "The user ID = %d" % user.id

        start = datetime.today()-timedelta(365);
        end = datetime.today();
        total = 0
        for entry in user.unbilled_entries( start, end ):
            print entry
            total += entry.hours

        total=0
        for expense in user.unbilled_expenses(start,end):
            print expense
            total+=
        print 'Total hours worked = %f' % total
